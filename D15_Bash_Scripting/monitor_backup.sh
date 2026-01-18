#!/bin/bash

# 1. Define Variables (Source and Destination)
SOURCE_FILE="/mnt/c/Users/Harsh/PycharmProjects/Devops/D13_System_health_montioring/system_monitor.log"
BACKUP_DIR="/mnt/c/Users/Harsh/PycharmProjects/Devops/backups"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
BACKUP_FILE="log_backup_$TIMESTAMP.log"

# 2. Create the backup folder if it doesn't exist
mkdir -p $BACKUP_DIR

# 3. Copy the log file to the backup folder
if [ -f "$SOURCE_FILE" ]; then
    cp "$SOURCE_FILE" "$BACKUP_DIR/$BACKUP_FILE"
    > "$SOURCE_FILE"
    echo "✅ Backup success: $BACKUP_FILE"
else
    echo "❌ Error: Source file not found!"
    exit 1
fi

find "$BACKUP_DIR" -name "log_backup_*.log" -type f -mtime +7 -delete

echo "Cleanup complete: Removed Backups older than 7 days"
