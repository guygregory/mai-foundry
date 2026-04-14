import os
import requests
from dotenv import load_dotenv

load_dotenv()


def require_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise SystemExit(
            f"Missing required environment variable: {name}\n"
            "Set it in your shell or add it to a .env file in this folder."
        )
    return value


endpoint = require_env("AZURE_ENDPOINT").rstrip("/")
api_key = require_env("AZURE_API_KEY")
deployment_name = require_env("DEPLOYMENT_NAME")

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
