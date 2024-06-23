import json
import xml.etree.ElementTree as Et
from abc import ABC, abstractmethod

from app.book import Book


class Serializer(ABC):
    @staticmethod
    @abstractmethod
    def serialize(book: Book) -> str:
        pass


class JSONSerializer(Serializer):
    @staticmethod
    def serialize(book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XMLSerializer:
    @staticmethod
    def serialize(book: Book) -> str:
        root = Et.Element("book")
        for tag in ("title", "content"):
            Et.SubElement(root, tag).text = getattr(book, tag)
        return Et.tostring(root, encoding="unicode")
