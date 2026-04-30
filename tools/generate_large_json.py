import json
import random
import string

# Calculate approximate size needed
#TARGET_SIZE_BYTES = 1024 * 1024 * 1024  # 生成了1.57GB
#TARGET_SIZE_BYTES = 512 * 1024 * 1024  # 生成了807MB
TARGET_SIZE_BYTES = 750 * 1024 * 1024  # 生成了1.15GB

# Generate random string data
def random_string(length=100):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Build large data structure
data = []
entry_size_estimate = 300  # Approximate bytes per entry
num_entries = TARGET_SIZE_BYTES // entry_size_estimate

print(f"Generating ~{num_entries} entries to reach ~1GB...")

for i in range(num_entries):
    entry = {
        "id": i,
        "name": random_string(50),
        "description": random_string(200),
        "value": random.randint(1, 1000000),
        "tags": [random_string(10) for _ in range(5)],
        "metadata": {
            "created": f"2024-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}",
            "updated": f"2024-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}",
            "count": random.randint(0, 9999)
        }
    }
    data.append(entry)

    if i % 100000 == 0 and i > 0:
        print(f"Generated {i} entries...")

print(f"Writing {len(data)} entries to large_file.json...")

with open('large_file.json', 'w', encoding='utf-8') as f:
    json.dump(data, f)

import os
file_size = os.path.getsize('large_file.json')
print(f"Done! File size: {file_size / (1024*1024*1024):.2f} GB ({file_size} bytes)")
