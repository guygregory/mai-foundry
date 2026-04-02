import os
import time
import base64
import requests
from dotenv import load_dotenv
load_dotenv()

endpoint = os.environ["AZURE_ENDPOINT"]
api_key = os.environ["AZURE_API_KEY"]
deployment_name = os.environ["DEPLOYMENT_NAME"]

url = f"{endpoint}/mai/v1/images/generations"

payload = {
    "model": deployment_name,
    "prompt": "A photorealistic image of a mountain lake at sunrise",
    "width": 1024,
    "height": 1024,
}

start_time = time.perf_counter()
response = requests.post(
    url,
    headers={
        "Content-Type": "application/json",
        "api-key": api_key,
    },
    json=payload,
)
response.raise_for_status()
elapsed = time.perf_counter() - start_time

result = response.json()

image_data = [
    output
    for output in result.get("data", [])
    if "b64_json" in output
]

if image_data:
    image_base64 = image_data[0]["b64_json"]
    output_path = "output.png"
    with open(output_path, "wb") as f:
        f.write(base64.b64decode(image_base64))
    print(f"Image saved to {output_path}")
else:
    print("Unexpected response format:", result)

if image_data and "revised_prompt" in image_data[0]:
    revised_prompt = image_data[0]["revised_prompt"]
    print(f"Revised prompt: {revised_prompt}")

print()
print(f"Generation time: {elapsed:.2f}s")

if result.get("created"):
    created = result["created"]
    model = result.get("model", "N/A")
    size = result.get("size", "N/A")
    
    print(f"Created: {created}")
    print(f"Model: {model}")
    print(f"Size: {size}")
