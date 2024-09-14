from __future__ import annotations

from gradio.events import EventListener

from .....utils.dev import ModelScopeLayoutComponent, resolve_frontend_dir


class AntdTourStep(ModelScopeLayoutComponent):
    """
    """
    EVENTS = [
        EventListener("close",
                      callback=lambda block: block._internal.update(
                          bind_close_event=True)),
        EventListener("next_button_props_click",
                      callback=lambda block: block._internal.update(
                          bind_nextButtonProps_click_event=True)),
        EventListener("prev_button_props_click",
                      callback=lambda block: block._internal.update(
                          bind_prevButtonProps_click_event=True)),
    ]

    # supported slots
    SLOTS = [
        'closeIcon', "cover", "title", "description",
        "nextButtonProps.children", "prevButtonProps.children"
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

    FRONTEND_DIR = resolve_frontend_dir("tour", "step")

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