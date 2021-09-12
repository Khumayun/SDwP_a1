import random

from task1 import decorator_1
from task2 import decorator_2
from task3 import decorator_3
from task4 import decorator_4, decorator_4_classed

test1 = lambda a, b, c: '\nx1: '+str((-b+(b**2-4*a*c)**(1/2))/(2*a))+'\nx1: ' + str((-b+(b**2-4*a*c)**(1/2))/(2*a))


@decorator_1
def pascal(n):
    top = [1]
    for _ in range(n):
        print(top)
        top = [l+r for l, r in zip(top+[0], [0]+top)]


@decorator_1
def func():
    # print("I am ready to Start")
    result = 0
    n = random.randint(10, 751)
    for i in range(n):
        result += (i ** 2)


@decorator_1
def funx(n=2, m=5):
    # print("I am ready to do serious stuff")
    max_val = float('-inf')
    n = random.randint(10, 751)
    res = [pow(i, 2) for i in range(n)]
    for i in res:
        if i > max_val:
            max_val = i


@decorator_2
def funh(bar1, bar2=""):
    """
    This function does something useful
    :param bar1: description
    :param bar2: description
    """
    print("some\nmultiline\noutput")


rank = []


@decorator_3
def fund(b):
    print('in a fund function', b)


@decorator_3
def funr(b):
    print('in a funr function', b)
    for i in range(1000):
        pass


@decorator_3
def funn(b):
    print('in a funn function', b)
    for i in range(100000):
        pass


@decorator_4
def test(b):
    print(1/b)


@decorator_4_classed
def test2(b):
    print(1/b)


if __name__ == '__main__':
    pascal(2)                                                    # task1
    funx()                                                       # task1
    func()                                                       # task1
    # func()                                                             # task2
    # func()                                                             # task2
    # func()                                                             # task2
    # funx()                                                             # task2
    # funh(None, bar2='')                                                # task2
    # fund('dumper wrapped function called fund')                     # task3
    # funr('we')                                                      # task3
    # funn('vvfl')                                                    # task3
    # print('PROGRAM | RANK | TIME ELAPSED')                          # task3
    # rank = sorted(rank, key=lambda x: x['elapsed'], reverse=True)   # task3
    # for i, item in enumerate(rank, start=1):                        # task3
    #     print(item['name'], '\t\t', i, '\t', item['elapsed']+'s')   # task3
    # test(0)                                                     # task4
    # test2(0)                                                    # task4
