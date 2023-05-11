
# Тестируем классы интернет-магазина
Вам нужно реализовать и протестировать классы интернет-магазина.
Все места, которые нужно дописать как в тестах, так и классах, отмечены `# TODO`.

При реализации обращайте внимание на типизацию аргументов методов и возвращаемых значений.
Так же обратите внимание на организацию тестов в файле с тестами:
- Тесты сгруппированы по классу, который они тестируют.
- Каждый тест называется именем соответствующего ему метода.

Вы можете начать как с реализации классов, так и с тестов.


# Дополнительные вопросы:
1. С чего проще начать выполнение домашнего задания: с тестов или с реализации классов?
Для меня оказалось проще начать с реализации классов. Понять, что должен делать класс, реализовать функционал, а затем написать тесты в зависимости от используемых в классах и методах инструментов
2. Почему для хранения товаров в корзине используется словарь, а не список?
Чтобы обеспечить уникальность лежащих в корзине продуктов
3. Зачем нужен __hash__ в классе Product? Изучите этот метод и объясните, почему он нужен.
Позволяет переопределить какие параметры экземпляра класса определяет уникальность этого экземпляра и не завязываться при этом на изменяемые, такие как количество и цена