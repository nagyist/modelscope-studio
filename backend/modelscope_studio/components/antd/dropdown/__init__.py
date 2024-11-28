from __future__ import annotations

from typing import Any, Literal

from gradio.events import EventListener

from ....utils.dev import ModelScopeLayoutComponent, resolve_frontend_dir
from .button import AntdDropdownButton


class AntdDropdown(ModelScopeLayoutComponent):
    """
    Ant Design: https://ant.design/components/dropdown
    """
    Button = AntdDropdownButton
    EVENTS = [
        EventListener("open_change",
                      callback=lambda block: block._internal.update(
                          bind_openChange_event=True)),
        EventListener("menu_click",
                      callback=lambda block: block._internal.update(
                          bind_menu_click_event=True)),
        EventListener("menu_deselect",
                      callback=lambda block: block._internal.update(
                          bind_menu_deselect_event=True)),
        EventListener("menu_open_change",
                      callback=lambda block: block._internal.update(
                          bind_menu_openChange_event=True)),
        EventListener("menu_select",
                      callback=lambda block: block._internal.update(
                          bind_menu_select_event=True)),
    ]

    # supported slots
    SLOTS = [
        "menu.expandIcon", 'menu.overflowedIndicator', "menu.items",
        "dropdownRender"
    ]

    def __init__(
            self,
            props: dict | None = None,
            *,
            arrow: dict | bool | None = None,
            auto_adjust_overflow: bool = True,
            auto_focus: bool | None = None,
            disabled: bool | None = None,
            destroy_popup_on_hide: bool | None = None,
            dropdown_render: str | None = None,
            get_popup_container: str | None = None,
            menu: dict | None = None,
            overlay_class_name: str | None = None,
            overlay_style: dict | None = None,
            placement: Literal['topLeft', 'top', 'topRight', 'bottomLeft',
                               'bottom', 'bottomRight'] = "bottomLeft",
            trigger: list[Literal['click', 'hover',
                                  'contextMenu']] = ['hover'],
            open: bool | None = None,
            inner_elem_style: dict | None = None,
            root_class_name: str | None = None,
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
        self.arrow = arrow
        self.auto_adjust_overflow = auto_adjust_overflow
        self.auto_focus = auto_focus
        self.disabled = disabled
        self.destroy_popup_on_hide = destroy_popup_on_hide
        self.dropdown_render = dropdown_render
        self.get_popup_container = get_popup_container
        self.menu = menu
        self.overlay_class_name = overlay_class_name
        self.overlay_style = overlay_style
        self.placement = placement
        self.trigger = trigger
        self.open = open
        self.inner_elem_style = inner_elem_style
        self.root_class_name = root_class_name

    FRONTEND_DIR = resolve_frontend_dir("dropdown")

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
