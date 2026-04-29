from pathlib import Path

import json

BASE_DIR = Path(__file__).resolve().parent.parent

input_file = BASE_DIR / 'resources/user_id_name.txt'
output_file = BASE_DIR / 'resources/users_data.json'

data = []
with open(input_file, 'r', encoding='utf-8') as f:
    # 跳过第一行表头
    header = f.readline()

    for line in f:
        line = line.strip()
        if not line:
            continue
        parts = line.split('\t')
        if len(parts) >= 2:
            # 去除前后的双引号
            user_id_str = parts[0].strip('"')
            name_str = parts[1].strip('"')

            try:
                user_id = int(user_id_str)
            except ValueError:
                continue

            # 组装为 MongoDB 需要的字典格式
            data.append({
                "user_id": user_id,
                "name": name_str,
                "competition_id": 3
            })

# 写入为标准 JSON 数组文件
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"转换成功！共生成了 {len(data)} 条数据，已保存为 {output_file}")