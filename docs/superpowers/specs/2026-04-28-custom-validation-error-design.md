# Custom Validation Error Design

## Goal
为当前 FastAPI 学习项目增加一个全局的中文请求参数校验错误提示示例，在请求体验证失败时，将默认错误格式转换成更适合新手理解的中文响应结构。

## Scope
- 保持 `POST /echo` 的成功行为不变
- 保持状态码 `422` 不变
- 增加全局请求体验证异常处理器
- 将默认验证错误转换为中文消息列表
- 更新测试与 README 示例

## Response Format
校验失败时返回：

```json
{
  "message": "请求参数校验失败",
  "errors": [
    "name 长度不能少于 2",
    "age 不能小于 0"
  ]
}
```

## Design Notes
- 使用 FastAPI 对请求体验证失败抛出的异常进行统一处理
- 只做最小中文映射，覆盖当前 `name` 最小长度和 `age` 最小值的示例
- 不引入额外依赖，不新增复杂错误系统

## Files
- `app/main.py`：注册全局异常处理器
- `tests/test_app.py`：校验中文错误返回
- `README.md`：补充中文错误返回示例
