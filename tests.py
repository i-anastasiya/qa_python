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
        # добавляем книгу в books_genre
        collector = BooksCollector()
        book_name = 'Гарри Поттер и философский камень'
        collector.add_new_book('Гарри Поттер и философский камень')
        assert book_name in collector.get_books_genre()

    def test_set_book_genre(self):
        # устанавливаем книге жанр и проверяем, что книга с этим жанром есть в books_genre
        collector = BooksCollector()
        genre = 'Фантастика'
        book_name = 'Гарри Поттер и философский камень'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert book_name in collector.get_books_genre()

    def test_get_book_genre(self):
        # устанавливаем книге жанр и получаем жанр книги по её имени
        collector = BooksCollector()
        genre = "Фантастика"
        book_name = 'Гарри Поттер и философский камень'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre

    def test_get_books_with_specific_genre(self):
        #  добавляем книги с определенным жанром и выводим список книг с определённым жанром
        collector = BooksCollector()
        genre = 'Фантастика'
        book_name = 'Гарри Поттер и философский камень'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        genre_1 = 'Детективы'
        book_name_1 = 'Шерлок Холмс'
        collector.add_new_book(book_name_1)
        collector.set_book_genre(book_name_1, genre_1)

        result = collector.get_books_with_specific_genre('Фантастика')
        assert len(result) == 1
        assert 'Гарри Поттер и философский камень' in result

        result_1 = collector.get_books_with_specific_genre('Детективы')
        assert len(result_1) == 1
        assert 'Шерлок Холмс' in result_1

    def test_get_books_genre(self):
        # получаем словарь books_genre и сравниваем его
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
        # устанавливаем жанр книге и возвращаем книги, подходящие детям
        collector = BooksCollector()
        genre = 'Фантастика'
        book_name = 'Гарри Поттер и философский камень'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_books_for_children() == [book_name]

    def test_add_book_to_favorites(self):
        # добавляем книгу в избранное и проверяем, что она там есть
        collector = BooksCollector()
        book_name = 'Гарри Поттер и философский камень'
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        assert book_name in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites(self):
        #  добавляем и удаляем книгу из избранного, сначала проверяем что она там есть при добавлении, а потом проверяем
        #  ее отсутствие после удаления
        collector = BooksCollector()
        book_name = 'Гарри Поттер и философский камень'
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        assert book_name in collector.get_list_of_favorites_books()
        collector.delete_book_from_favorites(book_name)
        assert book_name not in collector.get_list_of_favorites_books()

    def test_get_list_of_favourites_books(self):
        #  добавляем несколько книг в избаранное, а потом проверяем, что обе книги есть в этом списке.
        collector = BooksCollector()
        book_name = 'Гарри Поттер и философский камень'
        book_name_1 = 'Шерлок Холмс'
        collector.add_new_book(book_name)
        collector.add_new_book(book_name_1)
        collector.add_book_in_favorites(book_name)
        collector.add_book_in_favorites(book_name_1)
        assert book_name and book_name_1 in collector.get_list_of_favorites_books()
