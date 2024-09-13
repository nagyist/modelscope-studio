from __future__ import annotations

from typing import Any

from gradio.events import EventListener

from .....utils.dev import ModelScopeLayoutComponent, resolve_frontend_dir


class AntdStatisticCountdown(ModelScopeLayoutComponent):
    """
    """

    EVENTS = [
        EventListener("finish",
                      callback=lambda block: block._internal.update(
                          bind_finish_event=True)),
        EventListener("change",
                      callback=lambda block: block._internal.update(
                          bind_change_event=True)),
    ]

    # supported slots
    SLOTS = ['prefix', 'suffix', 'title']

    def __init__(
            self,
            value: int | float | None = None,
            props: dict | None = None,
            *,
            as_item: str | None = None,
            _internal: None = None,
            # gradio properties
            visible: bool = True,
            elem_id: str | None = None,
            elem_classes: list[str] | str | None = None,
            elem_style: dict | None = None,
            render: bool = True,
            **kwargs):
        super().__init__(visible=visible,
                         elem_id=elem_id,
                         elem_classes=elem_classes,
                         render=render,
                         as_item=as_item,
                         elem_style=elem_style,
                         **kwargs)
        self.props = props
        self.value = value

    FRONTEND_DIR = resolve_frontend_dir("statistic", "countdown")

    @property
    def skip_api(self):
        return True

    def preprocess(self, payload: str) -> str:
        return payload

    def postprocess(self, value: str) -> str:
        return value

    def example_payload(self) -> Any:
        return None

    def example_value(self) -> Any:
        return None
