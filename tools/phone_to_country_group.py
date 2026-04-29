from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent


def generate_grouped_statistics(input_excel_path, output_excel_path):
    print("开始读取解析结果并进行多维度分组统计...")
    input_excel_path = Path(input_excel_path)
    output_excel_path = Path(output_excel_path)

    if not input_excel_path.is_absolute():
        input_excel_path = BASE_DIR / input_excel_path
    if not output_excel_path.is_absolute():
        output_excel_path = BASE_DIR / output_excel_path

    try:
        # 读取已经解析好的明细数据
        df = pd.read_excel(input_excel_path)
    except Exception as e:
        print(f"读取文件失败，请确保文件名正确: {e}")
        return

    # 核心逻辑：按照 国家、省份、市 进行联合分组统计
    # value_counts 会自动计算组合的数量
    # reset_index(name='数量') 会将统计结果重命名为“数量”列
    df_grouped = df.value_counts(subset=['国家', '省份', '市']).reset_index(name='数量')

    # 可选优化：对结果进行排序，先按国家排，再按省份排，最后按数量降序，这样查看更直观
    df_grouped = df_grouped.sort_values(
        by=['国家', '省份', '数量'],
        ascending=[False, True, False]
    )

    # 导出到 Excel
    output_excel_path.parent.mkdir(parents=True, exist_ok=True)
    with pd.ExcelWriter(output_excel_path, engine='openpyxl') as writer:
        df_grouped.to_excel(writer, index=False, sheet_name='地区分布统计')

    print(f"统计完成！层级分布结果已保存至: {output_excel_path}")


# ==========================================
# 运行入口
# ==========================================
if __name__ == "__main__":
    # 【输入文件】：这里填解析出的明细 Excel 文件名
    input_file = "resources/upandaai手机号解析.xlsx"

    # 【输出文件】：汇总后的结果文件名
    output_file = "resources/pandaai国家省市分布统计结果.xlsx"

    generate_grouped_statistics(input_file, output_file)