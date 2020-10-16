FROM python:3

ADD proxyscrape.py /

RUN pip install urllib3, requests, lxml

CMD [ "python", "./proxyscrape.py" ]
