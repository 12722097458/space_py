# space_py
一个适合 Python 新手学习的项目，当前包含一个最小可运行的 FastAPI 示例。

## 项目结构

- `app/main.py`：FastAPI 应用入口
- `app/api/`：接口层，负责定义路由
- `app/services/`：业务逻辑层
- `app/schemas/`：数据模型层
- `tests/`：接口测试
- `scripts/`：练习脚本归档目录
- `tools/`：工具脚本

## 安装运行依赖

```bash
pip install -r requirements.txt
```

`requirements.txt` 现在同时包含 FastAPI 运行依赖，以及 `tools/phone_to_country.py` 这类工具脚本需要的基础依赖。

## 安装开发依赖

```bash
pip install -r requirements-dev.txt
```

## 启动项目

```bash
uvicorn app.main:app --reload
```

## 接口示例

- `GET /`
- `GET /add?a=1&b=2`
- `POST /echo`

根路径示例：

- `http://127.0.0.1:8000/`
- `http://127.0.0.1:8000/docs`
- `http://127.0.0.1:8000/add?a=1&b=2`

`POST /echo` 请求体示例：

```json
{
  "name": "Alice",
  "age": 18
}
```

`POST /echo` 返回示例：

```json
{
  "code": 0,
  "message": "success",
  "data": {
    "name": "Alice",
    "age": 18,
    "message": "你好，Alice，你今年 18 岁。"
  }
}
```

`POST /echo` 参数校验失败示例：

```json
{
  "name": "",
  "age": -1
}
```

预期现象：

- 返回状态码 `422`
- 返回中文字段校验错误信息

自定义错误返回示例：

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

## 运行测试

```bash
python -m pytest tests/test_app.py -v
```

## 代码格式化与检查

```bash
black app tests
ruff check app tests
```
