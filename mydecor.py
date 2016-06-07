__author__ = 'warior'
__mastermind__ = ['http://habrahabr.ru/post/141411/', 'http://habrahabr.ru/post/141501/']


# Декоратор обычный )
def bread(func):
    def wrapper():
        print("</------\>")
        func()
        print("<\______/>")
    return wrapper


def ingredients(func):
    def wrapper():
        print("#помидоры#")
        func()
        print("~салат~")
    return wrapper


@bread
@ingredients
def sandwich(food="--ветчина--"):
    print(food)

sandwich()


# Декоратор аргументированный
def uni_dec(func):
    def wrapper(*args, **kwargs):
        print('Вошло:')
        print(args)
        print(kwargs)
        func(*args, **kwargs)
    return wrapper


@uni_dec
def data(a, b, prum, q):
    print(a, b)
    print(prum)
    print(q)

qwery = {'a': 12, 'c': 32}
data(1, 2, qwery, q=5)
