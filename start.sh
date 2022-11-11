#!/bin/bash
mkdir LOGS
rm ./APP/database/users.db
uvicorn --host 192.168.0.106 --port 8888 --workers 1 --log-config "./logging.conf" --log-level "info" --use-colors main:app