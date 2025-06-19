#!/bin/sh
Green="\\033[32m"
Red="\\033[31m"
Plain="\\033[0m"

set -e

echo -e "${Green} [INFO] 开始运行... ${Plain}"
python3 main.py --auto