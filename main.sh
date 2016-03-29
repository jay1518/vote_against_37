#!/bin/bash
if [ -x "$(which pip)" ]; then
        echo '---'
else
        echo 'installing pip'
        curl -L 'https://bootstrap.pypa.io/get-pip.py' | python -
fi

SCRIPT_URL=https://raw.githubusercontent.com/ericls/vote_against_37/master/main.py

python -m pip install fake-factory requests
curl -L $SCRIPT_URL | python - --forever --timeout 3