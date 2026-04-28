from decimal import Decimal, ROUND_HALF_UP
from typing import Any

from my_package.math_operations import add, subtract

sum = add(3, 4)
num = subtract(100, 1)

print(f"sum = {sum}, num = {num}")


def format_float_4_decimal(value: Any) -> float:
    if value is None:
        return 0.0

    try:
        if isinstance(value, Decimal):
            decimal_val = value
        else:
            decimal_val = Decimal(str(value))

        rounded = decimal_val.quantize(Decimal('0.0001'), rounding=ROUND_HALF_UP)
        return float(rounded)
    except (ValueError, TypeError, Exception):
        return 0.0


num = 9.00001
print(format_float_4_decimal(num))
