# Assignment 2

- *move.sh* - implementation of the "move" command.
- *timetracker.sh* - implementation of the "track" command and time tracker.

## Usage of move

- source move.sh
- move src dst [filter]

src - source directory (must exist). dst - destination directory (if does not exist a directory with the given name is created, this directory will include
subdirectories named using the current date-time). Filter is optional. E.g. *.txt. If filter is not provided all the files are moved.

## Usage of track

- source timetracker.sh
- commands as described in the assignment