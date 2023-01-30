# Чтобы лучше понять, что такое фикстура 
# разберитесь с таким понятием в питоне как Декоратор
# Декоратор — это функция, которая позволяет обернуть другую функцию
# для расширения её функциональности без непосредственного изменения её кода.

def decorator_function(func):
    def wrapper():
        print('Функция-обёртка!')
        print('Оборачиваемая функция: {}'.format(func))
        print('Выполняем обёрнутую функцию...')
        func()
        print('Выходим из обёртки')
    return wrapper

@decorator_function
def hello_world():
    print('Hello world!')

hello_world()

# наверное сначала нужно понять, что всё в питоне это объект, со своими свойствами и методами. 
# Потом узнать, что функции, это объекты тоже. 
# Потом узнать, что функции бывают разных классов. 
# А уже от теории, которую осмыслят, двигаться к декоратору. 
# Так как курс очень поверхностный и не все курсанты понимают 
# почему в одном случае пишется some_func(), а в другом some_func без всех этих скобок.