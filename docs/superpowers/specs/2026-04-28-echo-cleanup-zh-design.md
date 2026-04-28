# POST Echo、旧脚本清理与中文文档设计

## Goal
在当前 FastAPI 学习项目中新增一个适合新手理解的 `POST /echo` 示例接口，删除根目录中已经归档到 `scripts/` 的旧练习脚本，并将项目说明文档改为中文。

## Scope
- 新增 `POST /echo` 接口
- 增加对应的请求模型、响应模型和服务函数
- 保留现有 `GET /` 与 `GET /add` 行为不变
- 删除根目录旧练习脚本
- 将 `README.md` 改写为中文说明

## API Design
- `POST /echo`
  - 请求体：`name: str`、`age: int`
  - 响应体：原始字段与欢迎语，例如 `你好，Alice，你今年 18 岁。`

## Structure
- `app/api/demo.py`：增加 POST 路由
- `app/schemas/demo.py`：增加请求/响应模型
- `app/services/demo_service.py`：增加构造欢迎语的函数
- `tests/test_app.py`：增加 POST 接口测试
- `README.md`：中文化并补充 POST 示例

## Cleanup Rule
仅删除根目录中已在 `scripts/` 下存在副本的旧练习脚本：`HelloWorld.py`、`Test2.py`、`Test3.py`、`Test4.py`、`Test5.py`、`Test6.py`、`Test7.py`。

## Testing
使用 `pytest` 和 `TestClient` 验证：
- `GET /`
- `GET /add`
- `POST /echo`
