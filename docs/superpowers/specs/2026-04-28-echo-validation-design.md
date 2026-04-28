# Echo Validation Failure Design

## Goal
为 `POST /echo` 增加一个适合 Python 新手理解的请求体参数校验失败示例，展示 FastAPI 和 Pydantic 在请求模型约束不满足时返回 `422` 的行为。

## Scope
- 给 `DemoRequest` 增加最小字段约束
- 增加一个失败测试用例
- 更新 README，增加校验失败示例
- 保持现有成功示例和接口结构不变

## Validation Rules
- `name`：不能为空，且长度至少为 2
- `age`：必须大于等于 0

## Expected Failure Example
请求体：
```json
{
  "name": "",
  "age": -1
}
```

预期响应：
- 状态码 `422`
- 返回请求体校验错误详情

## Files
- `app/schemas/demo.py`：增加字段约束
- `tests/test_app.py`：增加失败测试
- `README.md`：增加失败示例说明
