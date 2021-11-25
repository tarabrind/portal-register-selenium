#!/bin/bash

PY_ENV=venv


cd `dirname "$0"`
source ${PY_ENV}/bin/activate
python3 app.py
