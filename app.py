import os
import streamlit as st
from PIL import Image

from transformers import AutoProcessor, AutoModelForCausalLM

from IPython.display import display
from IPython.display import Markdown
import textwrap

import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI

os.environ['HUGGINGFACE_API_KEY'] = ''
os.environ['GOOGLE_API_KEY'] = ''

@st.cache_resource
def load_model():
    model = AutoModelForCausalLM.from_pretrained("microsoft/Florence-2-large", trust_remote_code=True)
    processor = AutoProcessor.from_pretrained("microsoft/Florence-2-large", trust_remote_code=True)
    return processor, model

def get_caption(image, task_prompt, processor, model, text_input=None):
    if text_input is None:
        prompt = task_prompt
    else:
        prompt = task_prompt + text_input
    inputs = processor(text=prompt, images=image, return_tensors="pt")
    generated_ids = model.generate(
      input_ids=inputs["input_ids"],
      pixel_values=inputs["pixel_values"],
      max_new_tokens=1024,
      early_stopping=False,
      do_sample=False,
      num_beams=3,
    )
    generated_text = processor.batch_decode(generated_ids, skip_special_tokens=False)[0]
    parsed_answer = processor.post_process_generation(
        generated_text,
        task=task_prompt,
        image_size=(image.width, image.height)
    )

    return parsed_answer

def analyze_captions(caption):
    def to_markdown(text):
        text = text.replace('•', ' *')
        return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))
    model = genai.GenerativeModel('gemini-1.5-pro')
    response = model.generate_content("Is the following image caption describing an ad campaign? Answer it in Yes or No\n\n" + caption)
    return to_markdown(response.text)

# Streamlit app
def main():
    st.title("Ad Campaign Recognition")
    st.write("Upload an image (PNG or JPEG) to generate a caption.")

    # Upload image
    uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpeg", "jpg"])

    if uploaded_file is not None:
        # Display uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Load model and processor
        processor, model = load_model()

        # Generate and display caption
        caption = get_caption(image, '<MORE_DETAILED_CAPTION>', processor, model)
        result = analyze_caption(caption)
        st.write("Generated Caption:")
        st.write(caption)

if __name__ == "__main__":
    main()
