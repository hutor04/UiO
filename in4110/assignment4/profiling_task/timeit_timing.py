import timeit

setup_1 = """
from test_slow_rectangle import random_array, loop, snake_loop
def array_creation():
    array = random_array(1e5)
"""
t_1 = timeit.Timer(stmt='array_creation()', setup=setup_1)

setup_2 = """
from test_slow_rectangle import random_array, loop, snake_loop
array = random_array(1e5)
def snk_loop():
    snake_loop(array)
"""
t_2 = timeit.Timer(stmt='snk_loop()', setup=setup_2)

setup_3 = """
from test_slow_rectangle import random_array, loop, snake_loop
array = random_array(1e5)
def run_loop():
    loop(array)
"""
t_3 = timeit.Timer(stmt='run_loop()', setup=setup_3)

print('Average for 10 runs:')
print(f'random_array: {t_1.timeit(number=10) / 10}')
print(f'snake_loop: {t_2.timeit(number=10) / 10}')
print(f'loop: {t_3.timeit(number=10) / 10}')
