from __future__ import annotations

from typing import Any, Literal

from gradio.events import EventListener

from .....utils.dev import ModelScopeLayoutComponent, resolve_frontend_dir


class AntdCollapseItem(ModelScopeLayoutComponent):
    """
    Ant Design: https://ant.design/components/collapse
    """

    EVENTS = [
        EventListener("item_click",
                      callback=lambda block: block._internal.update(
                          bind_itemClick_event=True)),
    ]

    # supported slots
    SLOTS = ['extra', "label", "children"]

    def __init__(
            self,
            label: str | None = None,
            key: str | float | int | None = None,
            props: dict | None = None,
            *,
            class_names: dict | None = None,
            collapsible: Literal['header', 'icon', 'disabled'] | None = None,
            extra: str | None = None,
            force_render: bool = False,
            show_arrow: bool = True,
            styles: dict | None = None,
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
        self.label = label
        self.props = props
        self.key = key
        self.class_names = class_names
        self.collapsible = collapsible
        self.extra = extra
        self.force_render = force_render
        self.show_arrow = show_arrow
        self.styles = styles

    FRONTEND_DIR = resolve_frontend_dir("collapse", "item")

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