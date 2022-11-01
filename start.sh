#!/bin/bash
mkdir LOGS
uvicorn --host 192.168.56.1 --port 8888 --workers 1 --log-config "./logging.conf" --log-level "info" --use-colors main:app