import cProfile
from test_slow_rectangle import random_array, snake_loop

array = random_array(1e5)

pr = cProfile.Profile()
res = pr.run('snake_loop(array)')  # res contains the statistics
res.print_stats()