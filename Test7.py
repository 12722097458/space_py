# from my_package import math_operations
# math_operations.add(1, 2)
from decimal import Decimal, ROUND_HALF_UP
from typing import Any

from my_package.math_operations import add, subtract
sum = add(3, 4)
num = subtract(100, 1)

print(f"sum = {sum}, num = {num}")


def format_float_4_decimal(value: Any) -> float:
    """
    格式化浮点数，保留4位小数（四舍五入）

    Args:
        value: 可以是 int, float, str, Decimal, None

    Returns:
        float: 保留4位小数的浮点数
    """
    if value is None:
        return 0.0

    try:
        # 转换为Decimal进行精确计算
        if isinstance(value, Decimal):
            decimal_val = value
        else:
            decimal_val = Decimal(str(value))

        # 使用四舍五入保留4位小数
        rounded = decimal_val.quantize(Decimal('0.0001'), rounding=ROUND_HALF_UP)
        return float(rounded)
    except (ValueError, TypeError, Exception):
        return 0.0



num = 9.00001
print(format_float_4_decimal(num))