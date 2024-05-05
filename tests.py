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
        assert book_name in collector.books_genre
        assert len(book_name) >= 1 and len(book_name) <= 40

    def test_set_book_genre(self):
        # проверяется, что метод устанавливает жанр книги,
        # если название книги существует в словаре books_genre и жанр является допустимым.
        collector = BooksCollector()
        book_name = "Властелин колец"
        genre = "Фэнтези"
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre

    def test_get_book_genre(self):
        # проверяется, что метод возвращает жанр книги, если название книги существует в словаре books_genre.
        collector = BooksCollector()
        book_name = "Бегущий в лабиринте"
        genre = "Фантастика"
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.books_genre = {
            "Книга 1": "Фантастика",
            "Книга 2": "Детектив",
            "Книга 3": "Фэнтези",
            "Книга 4": "Роман",
            "Книга 5": "Детектив"
        }
        genre = "Детектив"
        expected_result = ["Книга 2", "Книга 5"]
        actual_result = collector.get_books_with_specific_genre(genre)
        self.assertEqual(expected_result, actual_result)

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
        self.assertEqual(expected_result, actual_result)

    def test_get_books_for_children(self):
        # создаём экземпляр класса BooksCollector
        collector = BooksCollector()

        # определяем список книг
        expected_books = ["Книга 1", "Книга 2"]

        # вызываем метод get_books_for_children и сохраняем результат
        actual_books = collector.get_books_for_children()

        # сравниваем ожидаемый и фактический результаты
        assert actual_books == expected_books

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        book_name = "Книга 1"

        # Проверяем, что книга ещё не в избранном
        self.assertFalse(book_name in collector.favorites)

        # Добавляем книгу в избранное
        collector.add_book_in_favorites(book_name)

        # Проверяем, что книга теперь в избранном
        self.assertTrue(book_name in collector.favorites)

    def test_delete_book_from_favorites(self):
        # Создаём экземпляр класса BooksCollector
        collector = BooksCollector()

        # Добавляем книгу в список избранного
        book_name = "Книга 1"
        collector.add_book_to_favorites(book_name)

        # Проверяем, что книга добавлена в список избранного
        self.assertIn(book_name, collector.favorites)

        # Удаляем книгу из списка избранного
        collector.delete_book_from_favorites(book_name)

        # Проверяем, что книга удалена из списка избранного
        self.assertNotIn(book_name, collector.favorites)

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        book_1 = "Книга 1"
        book_2 = "Книга 2"
        book_3 = "Книга 3"

        # Добавляем книги в список favorites
        collector.favorites.append(book_1)
        collector.favorites.append(book_2)
        collector.favorites.append(book_3)

        # Вызываем метод get_list_of_favorites_books
        list_of_books = collector.get_list_of_favorites_books()

        # Проверяем, что возвращаемый список содержит все добавленные книги
        self.assertCountEqual(list_of_books, [book_1, book_2, book_3])
