#!/bin/bash
DIRECTORY="/home/sandworm/Workspace/Work/sharepoint_automation"
DOWNLOADS="/home/sandworm/Downloads"

rm "$DOWNLOADS/CURRENT*"
/usr/bin/python "$DIRECTORY/main.py"
sleep 1
echo "downloading..."
sleep 1
echo "copying file..."
sleep 1
mv "$DIRECTORY/CURRENT.mp4" "$DIRECTORY/$(date +%d-%m-%y).mp4"
mv "$DOWNLOADS/CURRENT.mp4" "$DIRECTORY/CURRENT.mp4"
