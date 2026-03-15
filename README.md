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

- Dash 页面：`http://127.0.0.1:8000/dash`
- FastAPI 文档：`http://127.0.0.1:8000/docs`
- FastAPI 生成接口：`POST http://127.0.0.1:8000/api/generate`
