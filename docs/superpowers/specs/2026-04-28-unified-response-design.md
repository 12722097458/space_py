# Unified Response Design

## Goal
为当前 FastAPI 学习项目增加一个统一响应格式示例，让成功响应和错误响应都返回相同的外层结构，便于新手理解接口返回设计。

## Scope
- 统一 `GET /`、`GET /add`、`POST /echo` 的成功响应格式
- 统一请求参数校验失败时的错误响应格式
- 保持当前接口路径不变
- 保持当前业务数据内容不变，只调整返回外层结构

## Response Format
成功响应：

```json
{
  "code": 0,
  "message": "success",
  "data": {
    "result": 7
  }
}
```

错误响应：

```json
{
  "code": 422,
  "message": "请求参数校验失败",
  "data": null,
  "errors": [
    "name 长度不能少于 2",
    "age 不能小于 0"
  ]
}
```

## Design Notes
- 成功和失败都保留 `code`、`message`、`data` 三个顶层字段
- 错误响应额外增加 `errors` 字段，用于展示具体错误列表
- 使用简单包装模型，避免引入复杂泛型或额外依赖

## Files
- `app/schemas/demo.py`：定义统一响应模型
- `app/api/demo.py`：更新成功响应
- `app/main.py`：更新校验失败响应
- `tests/test_app.py`：更新成功和失败测试
- `README.md`：更新示例文档
