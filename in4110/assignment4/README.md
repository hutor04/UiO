# Assignment 4

## Folders

- **bin** contains runnable script *instap.py* with commanline tool.
- **data** input-output images.
- **instapy** package containing the implementation of the filters.
- **profiling_task** files related to the profiling task.
- **reports** all the required reports.
- **tests** the script for running speed tests of the filter implementation and the script
for unit testing.

## Comments to some modules
- **./instapy/instapy_api.py** contains functions *grayscale_image* and *sepia_image*
- **./instapy/file_rw.py** helper module for reading-writing images to/from files.
- **./tests/speed_tests.py** generates speed-tests reports for the implementations
of the image filters. If you run it, some files in **./tests** will be overwritten.
- **./tests/test_instapy.py** unit tests for *instapy* package.

## The Instapy Package
The package can be installed with

	python3 -m pip install . --user

The commandline interface can be called from the terminal using e.g.

	instapy -h

to provide a list of options
