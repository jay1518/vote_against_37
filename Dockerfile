FROM python:3

# Chinese Localisation
ENV CHINESE_LOCAL_PIP_CONFIG="--index-url http://pypi.douban.com/simple --trusted-host pypi.douban.com"

COPY ./ /tmp
RUN pip install --requirement /tmp/requirements.txt ${CHINESE_LOCAL_PIP_CONFIG}

WORKDIR /tmp

ENTRYPOINT python3 main.py --count 10