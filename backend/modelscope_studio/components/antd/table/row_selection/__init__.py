from __future__ import annotations

from gradio.events import EventListener

from .....utils.dev import ModelScopeLayoutComponent, resolve_frontend_dir
from .selection import AntdTableRowSelectionSelection


# as inputs, outputs
class AntdTableRowSelection(ModelScopeLayoutComponent):
    """
    """
    Selection = AntdTableRowSelectionSelection

    EVENTS = [
        EventListener("change",
                      callback=lambda block: block._internal.update(
                          bind_change_event=True)),
        EventListener("select",
                      callback=lambda block: block._internal.update(
                          bind_select_event=True)),
        EventListener("select_all",
                      callback=lambda block: block._internal.update(
                          bind_selectAll_event=True)),
        EventListener("select_invert",
                      callback=lambda block: block._internal.update(
                          bind_selectInvert_event=True)),
        EventListener("select_none",
                      callback=lambda block: block._internal.update(
                          bind_selectNone_event=True)),
        EventListener("select_multiple",
                      callback=lambda block: block._internal.update(
                          bind_selectMultiple_event=True)),
    ]

    # supported slots
    SLOTS = [
        'columnTitle',
        'renderCell',
        'selections',
    ]

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

    FRONTEND_DIR = resolve_frontend_dir("table", "row-selection")

    @property
    def skip_api(self):
        return True

    def preprocess(self, payload: None) -> None:
        return payload

    def postprocess(self, value: None) -> None:

        return value

    def example_payload(self) -> None:
        return None

    def example_value(self) -> None:
        return None
