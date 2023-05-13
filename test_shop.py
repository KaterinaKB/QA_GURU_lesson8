"""
Протестируйте классы из модуля homework/models.py
"""
import pytest
from models import Product, Cart


@pytest.fixture
def product_book():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture()
def product_plate():
    return Product("Plate", 50, "Blue ceramic plate", 500)


@pytest.fixture
def cart():
    return Cart()


@pytest.fixture()
def cart_with_product(product_book, product_plate, cart):
    cart.add_product(product_book, 10)
    cart.add_product(product_plate, 10)
    return cart


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product_book):
        # TODO напишите проверки на метод check_quantity
        assert product_book.check_quantity(1000) is True

    def test_product_check_quantity_more_than_available(self, product_book):
        assert product_book.check_quantity(1001) is False

    def test_product_buy(self, product_book):
        # TODO напишите проверки на метод buy
        product_book.buy(5)

        assert product_book.quantity == 995

    def test_product_buy_more_than_available(self, product_book):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(
            ValueError,
            match=f'Requested quantity of product "book" is not available. In stock: 1000. To buy reduce the quantity by 5 units',
        ):
            product_book.buy(1005)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_cart_add_product(self, cart, product_book):
        cart.add_product(product_book, 2)

        assert cart.products[product_book] == 2

    def test_cart_add_product_with_default_quantity(self, cart, product_book):
        cart.add_product(product_book)

        assert cart.products[product_book] == 1

    def test_cart_add_product_already_in_cart(self, cart, product_book):
        cart.add_product(product_book)

        cart.add_product(product_book)

        assert cart.products[product_book] == 2

    def test_cart_remove_product(self, cart_with_product, product_book):
        cart_with_product.remove_product(product_book, 1)

        assert cart_with_product.products[product_book] == 9

    def test_cart_remove_product_without_remove_count(
        self, cart_with_product, product_book
    ):
        cart_with_product.remove_product(product_book)

        assert product_book not in cart_with_product.products

    def test_cart_remove_product_count_more_than_in_cart(
        self, cart_with_product, product_book
    ):
        cart_with_product.remove_product(product_book, 100)

        assert product_book not in cart_with_product.products

    def test_cart_remove_product_same_count_as_in_cart(
        self, cart_with_product, product_book
    ):
        cart_with_product.remove_product(product_book, 10)

        assert product_book not in cart_with_product.products

    def test_cart_clear(self, cart_with_product):
        cart_with_product.clear()

        assert cart_with_product.products == {}

    def test_cart_get_total_price(self, cart_with_product):
        total_price = cart_with_product.get_total_price()

        assert total_price == 1500.0

    def test_cart_buy(self, cart_with_product, product_book, product_plate):
        cart_with_product.buy()

        assert (
            product_book.quantity == 990
            and product_plate.quantity == 490
            and cart_with_product.products == {}
        )

    def test_cart_buy_more_than_available(
        self, cart_with_product, product_book, product_plate
    ):
        cart_with_product.add_product(product_plate, 500)

        with pytest.raises(
            ValueError,
            match=f'Requested quantity of product "Plate" is not available. In stock: 500. To buy reduce the quantity by 10 units',
        ):
            cart_with_product.buy()
