#!/bin/bash
SCRIPT_URL=https://raw.githubusercontent.com/loggerhead/vote_against_37/master/main.py

pip3 install fake-factory requests
curl -L $SCRIPT_URL | python3 -