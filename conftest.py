import pytest
from main import BooksCollector

# Базовая фикстура, для создания экземпляра BooksCollector
@pytest.fixture
def collector():
    collector = BooksCollector()
    return collector

# Фикстура с предзаполненными книгами
@pytest.fixture
def collector_with_books(collector):
    books_data = [('Фантастика 1', 'Фантастика'), ('Фантастика 2', 'Фантастика'), ('Ужасы 1', 'Ужасы'), ('Комедия 1', 'Комедии'), ('Книга без жанра', '')]

    for name, genre in books_data:
        collector.add_new_book(name)
        if genre:
            collector.set_book_genre(name, genre)

    return collector
