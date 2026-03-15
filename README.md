# Python 示例项目

这个项目包含两个脚本：

1. `hello.py`：打印 `hello world`。
2. `dash_fastapi_app.py`：使用 Dash + FastAPI，点击“编辑”输入内容，点击“提交”后通过 FastAPI 后端接口生成“输入内容 + 当前时间”。

## 1) 运行 Hello World
# Python Hello World

这个项目包含一个简单的 Python 脚本，用于打印 `hello world`。

## 运行方式

```bash
python3 hello.py
```

## 2) 运行 Dash + FastAPI 示例

> 说明：当前环境建议使用 `python3 -m pip` 与 `python3 -m uvicorn`，避免 `uvicorn` 命令不在 PATH 中。

安装依赖：

```bash
python3 -m pip install -r requirements.txt
```

启动服务：

```bash
python3 -m uvicorn dash_fastapi_app:fastapi_app --reload
```

或直接执行启动脚本：

```bash
./run_dash_fastapi.sh
```

打开浏览器访问：

- 根路径（自动跳转到 Dash）：`http://127.0.0.1:8000/`
- Dash 页面：`http://127.0.0.1:8000/dash`
- FastAPI 文档：`http://127.0.0.1:8000/docs`
- FastAPI 生成接口：`POST http://127.0.0.1:8000/api/generate`
