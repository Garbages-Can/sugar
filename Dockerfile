FROM python

WORKDIR /app

ADD . /app

RUN pip3 install -r requirements.txt \
    && python3 setup.py install

