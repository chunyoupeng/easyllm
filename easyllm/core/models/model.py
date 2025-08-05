from openai import OpenAI
from .providers import PROVIDER_TABLE
from easyllm.utils.prompt import parse_to_openai_messages

class LLM:
    """
    This class is used to interact with different LLM providers.

    Attributes:
        model_name (str): The name of the model to use.
        api_key (str): The API key for authentication.
        model_provider (str): The model provider.
    """
    def __init__(self, model_name, model_provider, api_key):
        """
        Initializes the Model instance.

        Args:
            model_name (str): The name of the model to use.
            model_provider (str): The name of the LLM provider.
            api_key (str): The API key for authentication.

        Raises:
            KeyError: If the model_provider is not found in the provider_table.
        """
        self.model_name = model_name
        self.api_key = api_key
        try:
            self.base_url = PROVIDER_TABLE[model_provider]
            self.client = OpenAI(api_key=api_key, base_url=self.base_url)
        except:
            print(f"Provider {model_provider} do not exist! Set to OpenAI base url")
            self.client = OpenAI(api_key=api_key)
    def chat(self, messages: list, json_mode=False) -> str:
        """
        Sends a chat request to the LLM and returns the response.

        Args:
            messages (list): A list of message dictionaries in the format expected by the LLM API.

        Returns:
            str: The content of the first choice in the response from the LLM.
        """
        json_type = None
        if json_mode:
            json_type = {"type": "json_object"}
        try:
            res = self.client.chat.completions.create(
                model=self.model_name, 
                messages=messages,
                response_format=json_type
            )
            return res.choices[0].message.content
        except Exception as e:
            raise e

    def __call__(self, message: str, json_mode=False) -> str:
        """
        Allows the Model instance to be called as a function.

        Args:
            message (str): The user's message.

        Returns:
            str: The response from the LLM after adding a system message and sending the chat request.
        """
        roles = ['# system', '# user', 'assistant']
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message},
        ]
        lines = message.split('\n')
        for l in lines:
            if l.lower() in roles:
                messages = parse_to_openai_messages(message)
        return self.chat(messages=messages, json_mode=json_mode)
