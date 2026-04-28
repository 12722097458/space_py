# FastAPI Demo Design

## Goal
在现有学习型 Python 项目中引入一个最小可运行的 FastAPI 示例，提供基础欢迎接口和一个演示函数接口，并在 README 中说明安装、启动和访问方式。

## Scope
- 新增 FastAPI 应用入口
- 新增一个 demo 计算函数与对应 HTTP 接口
- 新增基础依赖文件
- 新增最小测试，覆盖 demo 行为
- 更新 README 使用说明

## Structure
- `app/main.py`：FastAPI 应用入口与路由
- `tests/test_app.py`：接口行为测试
- `requirements.txt`：运行依赖
- `README.md`：项目说明与启动指南

## API Design
- `GET /`
  - 返回欢迎信息与项目状态
- `GET /add?a=1&b=2`
  - 返回 `a + b` 的结果

## Error Handling
- 参数类型校验由 FastAPI 默认处理
- demo 不额外引入复杂异常处理

## Testing
- 使用 `fastapi.testclient.TestClient`
- 覆盖 `/` 和 `/add` 两个接口
