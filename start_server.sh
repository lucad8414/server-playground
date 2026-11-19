#!/bin/bash
echo "Started Bash script!"
uvicorn main:server --host 0.0.0.0 --port 8000

