from abc import ABC, abstractmethod
from app.display import ConsoleDisplay, ReverseDisplay

from app.book import Book


class Printer(ABC):
    @staticmethod
    @abstractmethod
    def print_book(book: Book) -> None:
        pass


class ConsolePrinter:
    @staticmethod
    def print_book(book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        ConsoleDisplay.display(book)


class ReversePrinter:
    @staticmethod
    def print_book(book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        ReverseDisplay.display(book)
