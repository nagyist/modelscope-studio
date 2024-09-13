from __future__ import annotations

from typing import Any

from gradio.events import EventListener

from ....utils.dev import ModelScopeLayoutComponent, resolve_frontend_dir
from .item import AntdListItem


class AntdList(ModelScopeLayoutComponent):
    """
    """
    Item = AntdListItem
    EVENTS = [
        EventListener("pagination_change",
                      callback=lambda block: block._internal.update(
                          bind_pagination_change_event=True)),
        EventListener("pagination_show_size_change",
                      callback=lambda block: block._internal.update(
                          bind_pagination_showSizeChange_event=True)),
    ]

    # supported slots
    SLOTS = ['footer', 'header', 'loadMore']

    def __init__(
            self,
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

    FRONTEND_DIR = resolve_frontend_dir("list")

    @property
    def skip_api(self):
        return True

    def preprocess(self, payload: None) -> None:
        return payload

    def postprocess(self, value: None) -> None:
        return value

    def example_payload(self) -> Any:
        return None

    def example_value(self) -> Any:
        return None
