# Load model directly
import os
import requests

import pandas as pd
import numpy as np

from PIL import Image
from transformers import AutoProcessor, AutoModelForCausalLM 

### Setting up environment variables for huggingface and google API ####
os.environ['HUGGINGFACE_API_KEY'] = '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'
os.environ['GOOGLE_API_KEY'] = 'AIzaSyD_Dbg1456tZpRKFBZQbF3DmWMucf-iPhw'

model = AutoModelForCausalLM.from_pretrained("microsoft/Florence-2-large", trust_remote_code=True)
processor = AutoProcessor.from_pretrained("microsoft/Florence-2-large", trust_remote_code=True)

prompt = "Tell me about the scenery in the image"

url = "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/car.jpg?download=true"
image = Image.open(requests.get(url, stream=True).raw)

inputs = processor(text=prompt, images=image, return_tensors="pt")

generated_ids = model.generate(
    input_ids=inputs["input_ids"],
    pixel_values=inputs["pixel_values"],
    max_new_tokens=1024,
    num_beams=3,
    do_sample=False
)
generated_text = processor.batch_decode(generated_ids, skip_special_tokens=False)[0]

parsed_answer = processor.post_process_generation(generated_text, task="<OD>", image_size=(image.width, image.height))

print(parsed_answer)