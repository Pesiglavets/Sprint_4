import pytest
from main import BooksCollector

# Базовая фикстура, для создания экземпляра BooksCollector
@pytest.fixture
def collector():
    collector = BooksCollector()
    return collector