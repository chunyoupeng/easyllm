"""Easy LLM - A lightweight library for working with LLMs"""
from .core.models.embedding_model import EmbeddingModel
from .core.models.model import LLM
__all__ = ["LLM", "EmbeddingModel"]
__version__ = "0.1.0"