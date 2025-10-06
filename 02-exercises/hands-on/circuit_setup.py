# Option 2: CircuIT APIs (Azure OpenAI) setup
# Run this cell if you have CircuIT API access

import warnings
warnings.filterwarnings('ignore')

import openai
import traceback
import requests
import base64
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Open AI version to use
openai.api_type = "azure"
openai.api_version = "2024-12-01-preview"

# Get API_KEY wrapped in token - using environment variables
client_id = os.getenv('CISCO_CLIENT_ID')
client_secret = os.getenv('CISCO_CLIENT_SECRET')

url = "https://id.cisco.com/oauth2/default/v1/token"

payload = "grant_type=client_credentials"
value = base64.b64encode(f"{client_id}:{client_secret}".encode("utf-8")).decode("utf-8")
headers = {
    "Accept": "*/*",
    "Content-Type": "application/x-www-form-urlencoded",
    "Authorization": f"Basic {value}",
}

token_response = requests.request("POST", url, headers=headers, data=payload)
token_data = token_response.json()

from openai import AzureOpenAI

client = AzureOpenAI(
    azure_endpoint="https://chat-ai.cisco.com",
    api_key=token_data.get('access_token'),
    api_version="2024-12-01-preview"
)

app_key = os.getenv("CISCO_OPENAI_APP_KEY")

def get_chat_completion(messages, model="gpt-4o", temperature=0.0):
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        user=f'{{"appkey": "{app_key}"}}'
    )
    return response.choices[0].message.content

print("✅ CircuIT API setup complete! Ready for activities.")