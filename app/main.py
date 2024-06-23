import json
import xml.etree.ElementTree as ET


class Book:
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content

    def display(self, display_type: str) -> None:
        if display_type == "console":
            print(self.content)
        elif display_type == "reverse":
            print(self.content[::-1])
        else:
            raise ValueError(f"Unknown display type: {display_type}")


class Printer:
    @staticmethod
    def print_book(book, print_type: str) -> None:
        if print_type == "console":
            print(f"Printing the book: {book.title}...")
            book.display("console")
        elif print_type == "reverse":
            print(f"Printing the book in reverse: {book.title}...")
            book.display("reverse")
        raise ValueError(f"Unknown print type: {print_type}")


class Serializer:
    @staticmethod
    def serialize(book: Book, serialize_type: str) -> str:
        if serialize_type == "json":
            return json.dumps({"title": book.title, "content": book.content})
        elif serialize_type == "xml":
            root = ET.Element("book")
            for tag in ("title", "content"):
                ET.SubElement(root, tag).text = getattr(book, tag)
            return ET.tostring(root, encoding="unicode")

        raise ValueError(f"Unknown serialize type: {serialize_type}")

    def deserialize(self):
        ...


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            book.display(method_type)
        elif cmd == "print":
            Printer.print_book(book, method_type)
        elif cmd == "serialize":
            return Serializer.serialize(book, method_type)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
