"""Dash + FastAPI 示例：编辑内容后提交，生成“内容 + 当前时间”。"""

from datetime import datetime
import json
from urllib import error, request

from dash import Dash, Input, Output, State, dcc, html
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from flask import request as flask_request
from pydantic import BaseModel
from starlette.middleware.wsgi import WSGIMiddleware


class GenerateRequest(BaseModel):
    content: str


def build_message(content: str) -> str:
    """拼接用户内容和当前时间。"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    text = content.strip() or "（空内容）"
    return f"{text} | {timestamp}"


fastapi_app = FastAPI(title="Dash + FastAPI Demo")


@fastapi_app.post("/api/generate")
def generate(payload: GenerateRequest) -> dict[str, str]:
    return {"result": build_message(payload.content)}


@fastapi_app.get("/")
def root() -> RedirectResponse:
    """将根路径重定向到 Dash 页面，避免访问 / 时出现 404。"""
    return RedirectResponse(url="/dash/")


def call_generate_api(content: str) -> str:
    """由 Dash 回调调用 FastAPI 接口，返回生成结果。"""
    base_url = flask_request.host_url.rstrip("/")
    url = f"{base_url}/api/generate"
    payload = json.dumps({"content": content}).encode("utf-8")
    req = request.Request(url, data=payload, headers={"Content-Type": "application/json"}, method="POST")
    try:
        with request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return data.get("result", "生成失败：接口未返回结果")
    except error.URLError as exc:
        return f"生成失败：{exc}"


dash_app = Dash(
    __name__,
    requests_pathname_prefix="/dash/",
    routes_pathname_prefix="/dash/",
)

dash_app.layout = html.Div(
    [
        html.H2("Dash + FastAPI 内容生成器"),
        html.Button("编辑", id="edit-btn", n_clicks=0),
        dcc.Textarea(
            id="content-input",
            value="",
            placeholder="点击“编辑”后输入内容",
            style={"width": "100%", "height": 120, "marginTop": "12px"},
            disabled=True,
        ),
        html.Button("提交", id="submit-btn", n_clicks=0, style={"marginTop": "12px"}),
        html.Div(id="result", style={"marginTop": "16px", "fontWeight": "bold"}),
    ],
    style={"maxWidth": "720px", "margin": "32px auto", "fontFamily": "Arial, sans-serif"},
)


@dash_app.callback(
    Output("content-input", "disabled"),
    Input("edit-btn", "n_clicks"),
)
def enable_edit(n_clicks: int) -> bool:
    return n_clicks <= 0


@dash_app.callback(
    Output("result", "children"),
    Input("submit-btn", "n_clicks"),
    State("content-input", "value"),
    prevent_initial_call=True,
)
def submit_content(_: int, content: str) -> str:
    return call_generate_api(content or "")


@fastapi_app.get("/dash")
def dash_redirect() -> RedirectResponse:
    """将 /dash 重定向到 /dash/，避免相对资源路径异常。"""
    return RedirectResponse(url="/dash/")


fastapi_app.mount("/dash", WSGIMiddleware(dash_app.server))
