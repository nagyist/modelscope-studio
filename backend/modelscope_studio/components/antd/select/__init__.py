from __future__ import annotations

from typing import Any

from gradio.events import EventListener

from ....utils.dev import ModelScopeDataLayoutComponent, resolve_frontend_dir
from .option import AntdSelectOption


# as inputs, outputs
class AntdSelect(ModelScopeDataLayoutComponent):
    """
    """
    Option = AntdSelectOption

    EVENTS = [
        EventListener("change",
                      callback=lambda block: block._internal.update(
                          bind_change_event=True)),
        EventListener("blur",
                      callback=lambda block: block._internal.update(
                          bind_blur_event=True)),
        EventListener("focus",
                      callback=lambda block: block._internal.update(
                          bind_focus_event=True)),
        EventListener("search",
                      callback=lambda block: block._internal.update(
                          bind_search_event=True)),
        EventListener("select",
                      callback=lambda block: block._internal.update(
                          bind_select_event=True)),
        EventListener("clear",
                      callback=lambda block: block._internal.update(
                          bind_clear_event=True)),
        EventListener("popup_scroll",
                      callback=lambda block: block._internal.update(
                          bind_popupScroll_event=True)),
        EventListener("dropdown_visible_change",
                      callback=lambda block: block._internal.update(
                          bind_dropdownVisibleChange_event=True)),
    ]

    # supported slots
    SLOTS = [
        'allowClear.clearIcon', 'maxTagPlaceholder', 'menuItemSelectedIcon',
        'notFoundContent', 'removeIcon', 'suffixIcon', 'options'
    ]

    def __init__(
            self,
            value: str | int | float | list[float | int | str] | None = None,
            props: dict | None = None,
            *,
            as_item: str | None = None,
            _internal: None = None,
            # gradio properties
            visible: bool = True,
            elem_id: str | None = None,
            elem_classes: list[str] | str | None = None,
            elem_style: dict | None = None,
            key: int | str | None = None,
            render: bool = True,
            **kwargs):
        super().__init__(value=value,
                         visible=visible,
                         elem_id=elem_id,
                         elem_classes=elem_classes,
                         render=render,
                         as_item=as_item,
                         key=key,
                         elem_style=elem_style,
                         **kwargs)
        self.props = props

    FRONTEND_DIR = resolve_frontend_dir("select")

    @property
    def skip_api(self):
        return False

    def api_info(self) -> dict[str, Any]:
        return {
            "anyOf": [
                {
                    "type": "string",
                },
                {
                    "type": "number",
                },
                {
                    "type": "array",
                    "items": {
                        "anyOf": [
                            {
                                "type": "string",
                            },
                            {
                                "type": "number",
                            },
                        ],
                    },
                },
            ]
        }

    def preprocess(
        self, payload: str | int | float | list[float | int | str] | None
    ) -> str | int | float | list[float | int | str] | None:
        return payload

    def postprocess(
        self, value: str | int | float | list[float | int | str] | None
    ) -> str | int | float | list[float | int | str] | None:

        return value

    def example_payload(self) -> None:
        return None

    def example_value(self) -> None:
        return None