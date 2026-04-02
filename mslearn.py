import os
import requests

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

response = requests.post(
    url,
    headers={
        "Content-Type": "application/json",
        "api-key": api_key,
    },
    json=payload,
)
response.raise_for_status()

result = response.json()
print(result)
