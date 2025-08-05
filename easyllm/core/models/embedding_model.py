from openai import OpenAI
from .providers import PROVIDER_TABLE

class EmbeddingModel:
    """
    This class is used to interact with different LLM providers for embedding.

    Attributes:
        model_name (str): The name of the model to use.For example: "doubao-embedding-large-text-250515"
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
    def embedding_func(self, docs: list) -> list:
        vectors = [
            vec.embedding
            for vec in self.client.embeddings.create(input=docs, model=self.model_name).data
        ]
        return vectors
    def __call__(self, docs: list) -> list:
        """
        Allows the Model instance to be called as a function.

        Args:
            docs

        Returns:
            vector embeddings
        """
        if not isinstance(docs, list):
            docs = [docs] 
        return self.embedding_func(docs)
