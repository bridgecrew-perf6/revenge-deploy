#!/bin/bash

#生产环境中运行

TORNADO_DIR="/home/jovyan/work/revenge_server/revenge"

#启动程序
exec python3 $TORNADO_DIR/manage.py celery worker -l info


