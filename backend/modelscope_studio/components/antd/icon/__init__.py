from __future__ import annotations

from gradio.events import EventListener

from ....utils.dev import ModelScopeComponent, resolve_frontend_dir
from .iconfont_provider import AntdIconfontProvider


class AntdIcon(ModelScopeComponent):
    """
    """

    IconfontProvider = AntdIconfontProvider

    EVENTS = [
        EventListener("click",
                      callback=lambda block: block._internal.update(
                          bind_click_event=True))
    ]

    # supported slots
    SLOTS = []

    def __init__(
            self,
            value: str | None = "GithubOutlined",
            props: dict | None = None,
            *,
            spin: bool = False,
            rotate: int | float | None = None,
            component: str | None = None,
            as_item: str | None = None,
            _internal: None = None,
            # gradio properties
            visible: bool = True,
            elem_id: str | None = None,
            elem_classes: list[str] | str | None = None,
            elem_style: dict | None = None,
            render: bool = True,
            **kwargs):
        super().__init__(value=value,
                         visible=visible,
                         elem_id=elem_id,
                         elem_classes=elem_classes,
                         render=render,
                         as_item=as_item,
                         elem_style=elem_style,
                         **kwargs)
        self.props = props
        self.spin = spin
        self.rotate = rotate
        self.component = component

    FRONTEND_DIR = resolve_frontend_dir("icon")

    @property
    def skip_api(self):
        return True

    def preprocess(self, payload: str | None) -> str | None:
        return payload

    def postprocess(self, value: str | None) -> str | None:

        return str(value)

    def example_payload(self) -> str:
        return "GithubOutlined"

    def example_value(self) -> str:
        return "GithubOutlined"
