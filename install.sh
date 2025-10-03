#!/bin/bash

ROOT_UID=0
DEST_DIR=

# Destination directory
if [ "$UID" -eq "$ROOT_UID" ]; then
  DEST_DIR="/usr/share/icons"
else
  DEST_DIR="$HOME/.local/share/icons"
fi

mkdir -p "$DEST_DIR"

if [ -d "$DEST_DIR/Twilight-cursors" ]; then
  rm -r "$DEST_DIR/Twilight-cursors"
fi

cp -pr dist $DEST_DIR/Twilight-cursors

echo "Finished..."

