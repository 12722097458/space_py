# Project Initialization and Structure Design

## Goal
将当前学习型 Python 项目整理为一个适合新手理解的、层次清晰的 FastAPI 项目结构，同时保留原有练习脚本并集中归档。

## Scope
- 将 FastAPI 应用拆分为入口层、接口层、服务层、模型层
- 保留现有 demo 行为不变
- 将根目录旧练习脚本迁移到 `scripts/`
- 增加开发依赖文件
- 更新 README，说明目录结构与使用方式

## Target Structure
- `app/main.py`：应用入口与路由注册
- `app/api/demo.py`：demo 路由
- `app/services/demo_service.py`：业务逻辑
- `app/schemas/demo.py`：响应模型
- `tests/test_app.py`：接口测试
- `scripts/`：旧练习脚本归档
- `requirements.txt`：运行依赖
- `requirements-dev.txt`：开发依赖

## Design Decisions
- 保持最小依赖，只引入 FastAPI、Uvicorn 及基础开发工具
- 保持现有接口路径 `/` 与 `/add`，避免破坏已有测试和使用方式
- 不引入数据库、配置系统、中间件等复杂内容

## Testing
- 继续使用 `pytest` 与 `fastapi.testclient.TestClient`
- 验证根路由和加法路由结果
