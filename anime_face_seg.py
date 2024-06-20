import gradio as gr
from anime_image_2_chracter_class import Image2form

I2f = Image2form()

def process_image(image, img_type, h, w, top_space, head, confidence_level, mask):

    result, pil_w_img = I2f.image_data_form(image, img_type, h=int(h), w=int(w), top_space=int(top_space), head=int(head),confidence_level=float(confidence_level), mask=mask, del_flag=True)
    return pil_w_img

iface = gr.Interface(
    fn=process_image,
    inputs=[
        gr.components.Image(type="pil", label="Input Image"),
        gr.components.Dropdown(choices=["pil", "other"], value="pil",label="Image Type"),
        gr.components.Slider(minimum=1, maximum=2048, value=1024, label="Height"),
        gr.components.Slider(minimum=1, maximum=2048, value=756, label="Width"),
        gr.components.Slider(minimum=0, maximum=100, value=20, label="Top Space"),
        gr.components.Slider(minimum=1, maximum=512, value=256, label="Head size"),
        gr.components.Slider(minimum=0.1, maximum=1.0, value=0.5, label="Face detection confidence level"),
        gr.components.Checkbox(value=False, label="Mask"),
    ],
    outputs=gr.components.Image(type="pil", label="Processed Image"),
    title="Anime Character Cropping from Image",
    description="Cropping an anime character form input-image and upscale/resize."
)

iface.launch(share=True)

