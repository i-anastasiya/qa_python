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
        # проверяется, что метод добавляет новую книгу в словарь books_genre,
        # если название книги не существует в словаре и длина названия книги находится в диапазоне от 1 до 40 символов.
        collector = BooksCollector()
        book_name = "Голодные игры"
        collector.add_new_book(book_name)
        assert book_name in collector.get_books_genre()
        assert len(book_name) >= 1 and len(book_name) <= 40

    def test_set_book_genre(self):
        # проверяется, что метод устанавливает жанр книги,
        # если название книги существует в словаре books_genre и жанр является допустимым.
        collector = BooksCollector()
        book_name = "Властелин колец"
        genre = "Фэнтези"

        # Проверка наличия книги в словаре
        if book_name in collector.books_genre:
            # Установка жанра книги
            collector.set_book_genre(book_name, genre)
            assert collector.get_book_genre(book_name) == genre

    def get_book_genre(self):
        # проверяется, что метод возвращает жанр книги, если название книги существует в словаре books_genre.
        collector = BooksCollector()
        book_name = "Бегущий в лабиринте"
        genre = "Фантастика"
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()

        # Добавляем книги в словарь books_genre
        collector.add_new_book("Книга 1", "Фантастика")
        collector.add_new_book("Книга 2", "Детективы")
        collector.add_new_book("Книга 3", "Комедии")

        result = collector.get_books_with_specific_genre("Фантастика")
        assert result == ["Книга 1"]

        result = collector.get_books_with_specific_genre("Ужасы")
        assert result == []

        result = collector.get_books_with_specific_genre("Детективы")
        assert result == ["Книга 2"]

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
        expected_books = ['Мультфильмы', 'Комедии']
        assert collector.get_books_for_children(expected_books)

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        book_name = "Книга 1"
        # Добавляем книгу в избранное
        assert collector.is_book_in_favorites(book_name)

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        book_name = "Книга 1"
        collector.delete_book_from_favorites()
        assert book_name not in collector.favorites

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()

        # Добавляем книги в список favorites
        book_1 = "Книга 1"
        book_2 = "Книга 2"
        book_3 = "Книга 3"

        collector.add_book_to_favorites(book_1)
        collector.add_book_to_favorites(book_2)
        collector.add_book_to_favorites(book_3)

        # Вызываем метод get_list_of_favorites_books
        list_of_books = collector.get_list_of_favorites_books()

        # Проверяем, что возвращаемый список содержит все добавленные книги
        assert set(list_of_books) == {book_1, book_2, book_3}
