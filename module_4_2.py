def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()


test_function()
# inner_function()
# При попытке вызова функции `inner_function` вне функции `test_function`
# возникнет ошибка `NameError`, так как `inner_function` определена только внутри функции `test_function`
# и не доступна в глобальной области видимости.