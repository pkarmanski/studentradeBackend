#!/bin/bash
mkdir LOGS
uvicorn --host 192.168.0.67 --port 8888 --workers 1 --log-config "./logging.conf" --log-level "info" --use-colors main:app