import pytest
from main import BooksCollector

class TestBooksCollector:

    # Добавление двух книг
    def test_add_new_book_two_books_added(self, collector):
        collector.add_new_book('Книга 1')
        collector.add_new_book('Книга 2')

        assert len(collector.get_books_genre()) == 2
        
    # Добавление дубликата книги
    def test_add_new_book_duplicate_name_not_added(self, collector):
        collector.add_new_book('Книга 1')
        collector.add_new_book('Книга 1')

        assert len(collector.get_books_genre()) == 1      

    # Корректный жанр
    @pytest.mark.parametrize('genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_set_book_genre_valid_genre_not_set(self, collector, genre):
        collector.add_new_book('Черновик')
        collector.set_book_genre('Черновик', genre)
        assert collector.get_book_genre('Черновик') == genre