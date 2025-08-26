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

    # Некорректный жанр
    @pytest.mark.parametrize('invalid_genre', ['Боевик', 'Исекай', 'Наука', ''])
    def test_set_book_genre_invalid_genre_not_set(self, collector, invalid_genre):
        collector.add_new_book('Черновик')
        collector.set_book_genre('Черновик', invalid_genre)
        assert collector.get_book_genre('Черновик') == ''

    # Несуществующая книга возвращает None
    def test_get_book_genre_nonexistent_book_returns_none(self, collector_with_books):
        assert collector_with_books.get_book_genre('Несуществующая книга') is None

    # Посчет количества книг определенного жанра
    @pytest.mark.parametrize('target_genre, expected_count', [('Фантастика', 2), ('Ужасы', 1), ('Комедии', 1), ('Мультфильмы', 0)])
    def test_get_books_with_specific_genre_valid_genre_returns_books(self, collector_with_books, target_genre, expected_count):
        result = collector_with_books.get_books_with_specific_genre(target_genre)
        assert len(result) == expected_count
        
    # Проверка словаря с книгами по жанру
    def test_get_books_genre_valid_books_returns_all(self, collector_with_books):
        books_genre = collector_with_books.get_books_genre()
        assert len(books_genre) == 5
        assert 'Фантастика 1' in books_genre
        assert 'Ужасы 1' in books_genre
        
    # Проверка книг подходящих детям
    @pytest.mark.parametrize('book_name, expected_in_children', [('Фантастика 1', True), ('Ужасы 1', False), ('Комедия 1', True), ('Книга без жанра', False)])
    def test_get_books_for_children_various_genres_filtered(self, collector_with_books, book_name, expected_in_children):
        children_books = collector_with_books.get_books_for_children()
        if expected_in_children:
            assert book_name in children_books
        else:
            assert book_name not in children_books