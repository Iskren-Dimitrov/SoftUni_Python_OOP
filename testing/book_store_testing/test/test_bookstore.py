from unittest import TestCase, main

from project.bookstore import Bookstore


class TestBookstore(TestCase):
    def setUp(self):
        self.store = Bookstore(10)
        self.books = {"Java": 5, "Python": 4}

    def test_initialization_class_attributes(self):
        self.assertEqual(10, self.store.books_limit)
        self.assertEqual({}, self.store.availability_in_store_by_book_titles)
        self.assertEqual(0, self.store.total_sold_books)

    def test_book_limit_when_is_equal_to_zero(self):
        with self.assertRaises(ValueError) as ve:
            self.store.books_limit = 0

        self.assertEqual(f"Books limit of 0 is not valid", str(ve.exception))

    def test_book_limit_when_is_bigger_than_zero(self):
        result = self.store.books_limit = 15

        self.assertEqual(15, result)

    def test_len_method(self):
        self.store.availability_in_store_by_book_titles = self.books

        self.assertEqual(9, len(self.store))

    def test_receive_book_method_when_raise_exception(self):
        self.store.availability_in_store_by_book_titles = self.books

        with self.assertRaises(Exception) as ex:
            self.store.receive_book("Php", 5)

        self.assertEqual("Books limit is reached. Cannot receive more books!", str(ex.exception))

    def test_receive_book_method_when_book_title_not_in_dictionary(self):
        result = self.store.availability_in_store_by_book_titles = self.books

        self.store.receive_book("c++", 1)

        self.assertEqual({"Java": 5, "Python": 4, "c++": 1}, result)

    def test_total_number(self):
        result = self.store.receive_book("Python", 2)

        self.assertEqual(f"2 copies of Python are available in the bookstore.", result)
        self.assertEqual({"Python": 2}, self.store.availability_in_store_by_book_titles)

    def test_when_sell_book_and_book_title_not_in_dictionary(self):
        with self.assertRaises(Exception) as ex:
            self.store.sell_book("name", 1)

        self.assertEqual(f"Book name doesn't exist!", str(ex.exception))

    def test_when_sell_book_number_books_is_greater_than_books_in_dictionary(self):
        self.store.availability_in_store_by_book_titles = self.books

        with self.assertRaises(Exception) as ex:
            self.store.sell_book("Python", 6)

        self.assertEqual(f"Python has not enough copies to sell. Left: 4", str(ex.exception))

    def test_when_we_can_sell_successfully(self):
        self.store.availability_in_store_by_book_titles = self.books

        result = self.store.sell_book("Python", 2)

        self.assertEqual(f"Sold 2 copies of Python", result)
        self.assertEqual(2, self.store.total_sold_books)

    def test_correct__str__method(self):
        self.store.availability_in_store_by_book_titles = self.books

        self.assertEqual(f"Total sold books: 0\n"
                         f"Current availability: 9\n"
                         f" - Java: 5 copies\n"
                         f" - Python: 4 copies",
                         self.store.__str__())


if __name__ == "__main__":
    main()
