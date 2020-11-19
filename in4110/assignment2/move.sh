#!/bin/bash

function move {
    # Check if source and destination directories are provided
if [ $# -lt 2 ]; then
    echo "You must provide src and dst arguments"
    exit 1
fi

# Assign arguments to variables
src=$1
dst=$2
filter="*"

# If the thrid argument (filter) is provided, use the provided filter
if [ $# -eq 3 ]; then
    filter=$3
fi

# Check if source directory exists
if [ ! -d $src ]; then
    echo "Source directory does not exist. Enter a new directory"
    exit 1
fi

# Check if target directory exists, if not create a new one
if [ ! -d $dst ]; then
    echo "Target directory does not exist. Creating a new directory..."
    mkdir $dst
fi

# Specify paths for a folder with date
dstFullPath=$(realpath $dst)
dateFolder="$(date +'%Y-%m-%d-%H-%M')"
dstFinal="$dstFullPath/$dateFolder"

# List the contents of the source folder, apply the filter, if no matches found ignore error
# provided by ls command. Only files are selected.
srcfiles=( $(cd $src && ls -p -1 -d "$PWD/"$filter | grep -v '/$' 2>/dev/null) )

# Check if ls returned something
if [ ${#srcfiles[@]} -gt 0 ]; then
    echo "Moving ${#srcfiles[@]} file(s)..."

    # Check if the dated directory exists, if not create it
    if [ ! -d $dstFinal ]; then
    echo "Creating a new dated directory in destination..."
    mkdir $dstFinal
    fi

    # Move files from the source to the destination directory
    for i in "${srcfiles[@]}"
        do
            if [ ! -d $i ]; then
                mv $i "$dstFinal/$(basename -- $i)"
            fi
        done
    
    else

    # Show message if the source directory does not include files or files that match the specified pattern
    echo "No files in the src matching the filter..."
fi

echo "Done"
}
