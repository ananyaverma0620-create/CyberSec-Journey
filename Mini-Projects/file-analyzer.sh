#!/bin/bash

if [ -z "$1" ]; then
    echo "Usage: $0 <directory_path>"
    exit 1
fi

DIR="$1"

if [ ! -d "$DIR" ]; then
    echo "Directory does not exist!"
    exit 1
fi

echo "Files and sizes:"
find "$DIR" -type f -exec du -h {} +

FILE_COUNT=$(find "$DIR" -type f | wc -l)
echo "Total files: $FILE_COUNT"

TOTAL_SIZE=$(du -sh "$DIR" | cut -f1)
echo "Total size: $TOTAL_SIZE"

LARGEST_FILE=$(find "$DIR" -type f -exec du -b {} + | sort -nr | head -n 1 | cut -f2)
LARGEST_SIZE=$(du -h "$LARGEST_FILE" | cut -f1)

echo "Largest file: $LARGEST_FILE"
echo "Size: $LARGEST_SIZE"
