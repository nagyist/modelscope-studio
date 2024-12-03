import gradio as gr

import modelscope_studio.components.antd as antd
import modelscope_studio.components.base as ms

with gr.Blocks() as demo:
    with ms.Application():
        with antd.ConfigProvider():
            antd.Calendar()
            antd.Divider("Card")
            with antd.Card():
                antd.Calendar(fullscreen=False)

if __name__ == "__main__":
    demo.queue().launch()