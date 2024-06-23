from app.book import Book
from app.display import ConsoleDisplay, ReverseDisplay
from app.printer import ConsolePrinter, ReversePrinter
from app.serializers import JSONSerializer, XMLSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    display_mapping = {
        "console": ConsoleDisplay(),
        "reverse": ReverseDisplay()
    }
    print_mapping = {
        "console": ConsolePrinter(),
        "reverse": ReversePrinter()
    }
    serialize_mapping = {
        "json": JSONSerializer(),
        "xml": XMLSerializer()
    }

    for cmd, method_type in commands:
        if cmd == "display":
            display_mapping[method_type].display(book)
        elif cmd == "print":
            print_mapping[method_type].print_book(book)
        elif cmd == "serialize":
            return serialize_mapping[method_type].serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
