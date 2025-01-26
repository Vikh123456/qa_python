import pytest

from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.books_genre) == 2


    def test_add_new_book_add_same_book_name(self):
        collector = BooksCollector()
        collector.add_new_book('Как зарабатывать 500к в наносек')
        collector.add_new_book('Как зарабатывать 500к в наносек')
        assert len(collector.books_genre) == 1

    @pytest.mark.parametrize("name", ["test", ''])
    def test_add_new_book_does_not_fit_in_name_limit(self, name):
        collector = BooksCollector()
        book = ''.join([name for _ in range(12)])
        collector.add_new_book(book)
        assert not collector.books_genre

    @pytest.mark.parametrize('book, genre', [('Дюна', 'Фантастика'),
                                             ('Молчание ягнят', 'Ужасы'),
                                             ('Убийство в восточном экспрессе', 'Детективы'),
                                             ('Винни Пух', 'Мультфильмы'),
                                             ('Американский пирог', 'Комедии')])
    def test_set_book_genre_add_existed_book(self, book, genre):
        collector = BooksCollector()
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)
        assert collector.books_genre.get(book) == genre

    def test_get_book_genre_add_existed_book(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер','Ужасы')
        assert collector.get_book_genre('Гарри Поттер') == 'Ужасы'

    def test_get_books_with_specific_genre_get_one(self, prepare_books_data):
        collector = prepare_books_data
        comedies = collector.get_books_with_specific_genre('Комедии')
        assert len(comedies) == 1
        assert 'Терминатор' in comedies

    def test_get_books_genre_without_adding(self):
        collector = BooksCollector()
        assert not collector.get_books_genre()

    def test_get_books_for_children_allowed_genre(self, prepare_books_data):
        collector = prepare_books_data
        children_books = collector.get_books_for_children()
        assert len(children_books) == 1
        assert 'Терминатор' in children_books

    def test_delete_book_from_favorites_one_book(self, prepare_books_data):
        collector = prepare_books_data
        collector.add_book_in_favorites('Наруто')
        collector.delete_book_from_favorites('Наруто')
        assert len(collector.favorites) == 0
        assert 'Наруто' not in collector.favorites

    def test_get_list_of_favorites_books_add_one_book(self, prepare_books_data):
        collector = prepare_books_data
        collector.add_book_in_favorites('Наруто')
        favorites = collector.get_list_of_favorites_books()
        assert len(favorites) == 1
        assert 'Наруто' in favorites
