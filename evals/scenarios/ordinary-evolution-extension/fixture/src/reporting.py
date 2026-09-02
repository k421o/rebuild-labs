from __future__ import annotations

import json
from collections.abc import Callable

Row = dict[str, str | int]
Renderer = Callable[[list[Row]], str]
RENDERERS: dict[str, Renderer] = {}


def register_renderer(name: str, renderer: Renderer) -> None:
    RENDERERS[name] = renderer


def render_report(name: str, rows: list[Row]) -> str:
    return RENDERERS[name](rows)


def render_json(rows: list[Row]) -> str:
    return json.dumps(rows, sort_keys=True)


register_renderer("json", render_json)
