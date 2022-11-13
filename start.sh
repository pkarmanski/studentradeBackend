#!/bin/bash
mkdir LOGS
rm ./APP/database/users.db
uvicorn --host localhost --port 8888 --workers 1 --log-config "./logging.conf" --log-level "info" --use-colors main:app