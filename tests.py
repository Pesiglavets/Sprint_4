import pytest
from main import BooksCollector

class TestBooksCollector:

    # Добавление двух книг
    def test_add_new_book_two_books_added(self, collector):
        collector.add_new_book('Книга 1')
        collector.add_new_book('Книга 2')

        assert len(collector.get_books_genre()) == 2