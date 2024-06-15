from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book(self):
        collector = BooksCollector()
        book_name = 'Гарри Поттер и философский камень'
        collector.add_new_book('Гарри Поттер и философский камень')
        assert book_name in collector.get_books_genre()

    def test_set_book_genre(self):
        collector = BooksCollector()
        genre = 'Фантастика'
        book_name = 'Гарри Поттер и философский камень'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre

    def test_get_book_genre(self):
        collector = BooksCollector()
        genre = "Фантастика"
        book_name = 'Гарри Поттер и философский камень'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        genre = collector.books_genre['Гарри Поттер и философский камень'] = "Фантастика"
        genre_1 = collector.books_genre['Шерлок Холмс'] = "Детектив"
        book_name = collector.favorites.append('Гарри Поттер и философский камень')
        collector.set_book_genre(book_name, genre)
        collector.set_book_genre(book_name, genre_1)

        result = collector.get_books_with_specific_genre("Фантастика")
        assert len(result) == 1
        assert 'Гарри Поттер и философский камень' in result

        result = collector.get_books_with_specific_genre("Детектив")
        assert result == []

    def test_get_books_genre(self):
        collector = BooksCollector()
        collector.books_genre = {
            "Книга 1": "Фантастика",
            "Книга 2": "Детектив",
            "Книга 3": "Фэнтези",
            "Книга 4": "Научная фантастика",
            "Книга 5": "Детектив"
        }
        expected_result = {
            "Книга 1": "Фантастика",
            "Книга 2": "Детектив",
            "Книга 3": "Фэнтези",
            "Книга 4": "Научная фантастика",
            "Книга 5": "Детектив"
        }
        actual_result = collector.get_books_genre()
        assert actual_result == expected_result

    def test_get_books_for_children(self):
        collector = BooksCollector()
        genre = 'Фантастика'
        book_name = 'Гарри Поттер и философский камень'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_books_for_children() == [book_name]

    def test_add_book_to_favorites(self):
        collector = BooksCollector()
        book_name = 'Гарри Поттер и философский камень'
        collector.add_book_in_favorites('Гарри Поттер и философский камень')
        collector.favorites.append(book_name)
        assert book_name in collector.favorites

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        book_name = 'Гарри Поттер и философский камень'
        collector.delete_book_from_favorites('Гарри Поттер и философский камень')
        assert book_name not in collector.favorites

    def test_get_list_of_favourites_books(self):
        collector = BooksCollector()
        book_name = 'Гарри Поттер и философский камень'
        collector.add_book_in_favorites('Гарри Поттер и философский камень')
        collector.favorites.append(book_name)
        assert book_name in collector.get_list_of_favorites_books()
