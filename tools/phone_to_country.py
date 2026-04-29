from pathlib import Path

import pandas as pd
import phonenumbers
from phone import Phone

try:
    from phonenumbers import geocoder
except ModuleNotFoundError as exc:
    if exc.name == "phonenumbers.geodata":
        geocoder = None
    else:
        raise

# 首先下载依赖  pip install pandas openpyxl phone phonenumbers
# 【终极修复方案】：常见区号兜底映射表
# 防止第三方库版本过低或号码严格校验失败时，返回空白
# resources/users-panda.xlsx


COUNTRY_CODE_MAP = {
    "86": "中国", "852": "香港", "853": "澳门特区", "886": "台湾地区",
    "61": "澳大利亚", "60": "马来西亚", "65": "新加坡", "44": "英国",
    "1": "美国/加拿大", "81": "日本", "82": "韩国", "33": "法国", "49": "德国"
}


def get_country_name(parsed_num, language):
    if geocoder is None:
        return ""
    return geocoder.country_name_for_number(parsed_num, language)


def get_description(parsed_num, language):
    if geocoder is None:
        return ""
    return geocoder.description_for_number(parsed_num, language)


BASE_DIR = Path(__file__).resolve().parent.parent


def process_phones(input_excel_path, output_excel_path):
    print("开始读取 Excel 并解析...")
    input_excel_path = Path(input_excel_path)
    output_excel_path = Path(output_excel_path)

    if not input_excel_path.is_absolute():
        input_excel_path = BASE_DIR / input_excel_path
    if not output_excel_path.is_absolute():
        output_excel_path = BASE_DIR / output_excel_path

    try:
        df = pd.read_excel(input_excel_path, dtype={'country_code': str, 'phone': str})
    except Exception as e:
        print(f"读取文件失败: {e}")
        return

    results = []
    p = Phone()

    for index, row in df.iterrows():
        country_code = str(row['country_code']).replace('.0', '').strip()
        phone_num = str(row['phone']).replace('.0', '').replace(' ', '').strip()

        if pd.isna(phone_num) or phone_num == 'nan' or phone_num == '':
            continue

        if country_code in ['61', '44', '60'] and phone_num.startswith('0'):
            phone_num = phone_num.lstrip('0')

        full_number_str = f"+{country_code}{phone_num}"

        # 【修改点 1】：初始化时，直接用字典兜底。认识区号就直接填国家！
        res = {
            "区号": country_code,
            "手机号": phone_num,
            "国家": COUNTRY_CODE_MAP.get(country_code, "未知"),
            "省份": "-",
            "市": "-"
        }

        try:
            parsed_num = phonenumbers.parse(full_number_str, None)

            country_zh = get_country_name(parsed_num, "zh")
            if country_zh:  # 如果解析出来不是空字符串，就用库的精准结果覆盖
                res["国家"] = country_zh

            # 中国大陆号码处理
            if country_code == "86":
                p_info = p.find(phone_num)
                if p_info:
                    res["省份"] = p_info.get('province', '-')
                    res["市"] = p_info.get('city', '-')

            # 港澳台及微型国家处理
            elif country_code in ['852', '853', '886', '65']:
                res["省份"] = res["国家"]

            # 其他国际号码处理（含澳大利亚）
            else:
                geo_desc_zh = get_description(parsed_num, "zh")
                geo_desc_en = get_description(parsed_num, "en")

                # 尝试获取更细化的省份或州
                if geo_desc_zh and geo_desc_zh != res["国家"]:
                    res["省份"] = geo_desc_zh
                elif geo_desc_en and geo_desc_en != get_country_name(parsed_num, "en"):
                    if "," in geo_desc_en:
                        parts = geo_desc_en.split(",")
                        res["市"] = parts[0].strip()
                        res["省份"] = parts[1].strip()
                    else:
                        res["省份"] = geo_desc_en

        except Exception as e:
            pass  # 即便报错，前面已经有了兜底数据，不会为空

        results.append(res)

    output_df = pd.DataFrame(results)[["区号", "手机号", "国家", "省份", "市"]]
    output_excel_path.parent.mkdir(parents=True, exist_ok=True)
    output_df.to_excel(output_excel_path, index=False)
    print(f"处理成功！文件已保存至: {output_excel_path}")

# 使用示例（替换为你实际的文件路径）
if __name__ == "__main__":
    input_file = "resources/users-panda.xlsx"  # 这里填入你的原始 Excel 文件路径
    output_file = "resources/upandaai手机号解析.xlsx"  # 输出的文件路径
    process_phones(input_file, output_file)




