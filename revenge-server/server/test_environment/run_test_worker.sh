#!/bin/bash

#测试环境中运行

TORNADO_DIR="/home/simba/github/revenge_deploy/revenge_server/revenge"
VIRTUALENV_BIN="/home/simba/github/revenge_deploy_env3/bin"

#进入虚拟环境
source  $VIRTUALENV_BIN/activate

#启动程序
exec python3 $TORNADO_DIR/manage.py celery worker --beat -l info


