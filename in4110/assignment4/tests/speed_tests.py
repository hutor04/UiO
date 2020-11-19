#!/usr/bin/env python
from instapy.python_color2gray import python_color2gray
from instapy.numpy_color2gray import numpy_color2gray
from instapy.numba_color2gray import numba_color2gray
from instapy.cython_color2gray import cython_color2gray
from instapy.python_color2sepia import python_color2sepia
from instapy.numpy_color2sepia import numpy_color2sepia
from instapy.numba_color2sepia import numba_color2sepia
from instapy.cython_color2sepia import cython_color2sepia
from instapy.file_rw import read_file
import time
import numpy as np

# Settings
functions_to_test = [python_color2gray, numpy_color2gray, numba_color2gray, cython_color2gray]
report_file_names = ['python_report_color2gray.txt', 'numpy_report_color2gray.txt', 'numba_report_color2gray.txt',
                     'cython_report_color2gray.txt']
functions_to_test_2 = [python_color2sepia, numpy_color2sepia, numba_color2sepia, cython_color2sepia]
report_file_names_2 = ['python_report_color2sepia.txt', 'numpy_report_color2sepia.txt', 'numba_report_color2sepia.txt',
                       'cython_report_color2sepia.txt']

report_directory = '../reports/'
file_to_transform = read_file('../data/rain.jpg')


def time_it(func, *args):
    """
    Measures runtime of a function.
    Args:
        func (func): Function to be measured.
        *args (any): Arguments to be provided to the function.

    Returns:
        float: Time elapsed during the runtime of the provided function.
    """
    s = time.time()
    func(*args)
    e = time.time()
    return e - s


def time_it_multiple_runs(func, reps, *args):
    """
    Measure the runtime of a function specified number of times.
    Args:
        func (func): Function to be timed.
        reps (int): Number of repetitions.
        *args (any): Arguments that should be passed to the function.

    Returns:
        list:float: Timing of each repetition.
    """
    duration = []
    for i in range(reps):
        duration.append(time_it(func, *args))
    return duration


def time_it_verbose(funcs, reps, img, verbose=True):
    """
    Carry out experiments, save reports to files.
    Args:
        funcs (list:func): Functions to be tested.
        reps (int): Number of times to repeat the experiment.
        img (numpy.ndarray): Input image.
        verbose (bool): If set to true prints output of experiments to terminal.

    Returns:
        list:str: Reports describing the experiment.
    """
    reports = []
    avgs = []
    for idx, func in enumerate(funcs):
        report = ''
        report += f'Timing: {func.__name__}\n'
        report += f'Timing performed using: {img.shape}\n'
        timing = time_it_multiple_runs(func, reps, img)
        avg = np.mean(timing)
        avgs.append(avg)
        report += f'Average runtime running {func.__name__} after {reps} runs is: {avg}\n'
        if len(avgs) > 0:
            for i in range(idx):
                diff = avgs[i] / avg if avgs[i] > avg else avg / avgs[i]
                phrasing = 'faster' if avgs[i] > avg else 'slower'
                report += f'Average runtime running {func.__name__} is {diff} times {phrasing} than {funcs[i].__name__}.\n'
        report += f"{'=' * 10}\n"
        reports.append(report)
        if verbose:
            print(report)
    return reports


def save_reports(base, file_names, reports):
    """
    Saves reports to files.
    Args:
        base (str): Path to directory with reports.
        file_names (list:str): List of filenames.
        reports (list:str): List with reports.

    Returns:
        None
    """
    for report, file_name in zip(reports, file_names):
        with open(f'{base}{file_name}', 'w') as f:
            f.write(report)


if __name__ == '__main__':
    reps = time_it_verbose(functions_to_test, 10, file_to_transform, True)
    save_reports(report_directory, report_file_names, reps)

    reps_2 = time_it_verbose(functions_to_test_2, 10, file_to_transform, True)
    save_reports(report_directory, report_file_names_2, reps_2)
