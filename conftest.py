import pytest

from main import BooksCollector


@pytest.fixture()
def prepare_books_data():
    collector = BooksCollector()
    for book in ["Моана", "Терминатор", "Наруто"]:
        collector.add_new_book(book)
    collector.set_book_genre('Моана', 'Ужасы')
    collector.set_book_genre('Терминатор', 'Комедии')
    collector.set_book_genre('Наруто', 'Детективы')
    return collector