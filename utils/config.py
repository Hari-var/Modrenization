import os
from dotenv import load_dotenv
from .AzureSecrets import get_azure_secret_value
import json

load_dotenv()

azure_secrets_url = os.environ["Azure_Secrets_URL"]

class Content_generator_model_config:
    AI_content_version = get_azure_secret_value("AI-content-version")
    AI_content_endpoint = get_azure_secret_value("AI-content-endpoint")
    AI_content_key = get_azure_secret_value("AI-content-key")
    AI_content_model = get_azure_secret_value("AI-content-model")