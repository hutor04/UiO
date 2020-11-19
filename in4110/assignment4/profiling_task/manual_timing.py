from test_slow_rectangle import random_array, loop, snake_loop
import time
import numpy as np

def manual_timer(reps=3):
    results = []
    for rep in range(3):
        print(f'Test no. {rep + 1}')
        curr_result = []

        t0 = time.time()
        array = random_array(1e5)
        t1 = time.time()
        elapsed = t1-t0
        curr_result.append(elapsed)
        print(f'Runtime of array creation: {elapsed}')

        t0 = time.time()
        array = snake_loop(array)
        t1 = time.time()
        elapsed = t1-t0
        curr_result.append(elapsed)
        print(f'Runtime of snake_loop: {elapsed}')

        t0 = time.time()
        array = loop(array)
        t1 = time.time()
        elapsed = t1-t0
        curr_result.append(elapsed)
        print(f'Runtime of loop: {elapsed}')

        results.append(curr_result)
    avrgs = np.mean(results, axis=0)
    print('=' * 10)
    print(f'Average for {reps} runs:\nrandom_array: {avrgs[0]}\nsnake_loop: {avrgs[1]}\nloop: {avrgs[2]}')


if __name__ == '__main__':
    manual_timer()