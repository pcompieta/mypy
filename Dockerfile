FROM python:3.6-alpine

RUN mkdir /app
COPY my.py /app
COPY mmlibrary.py /app
COPY mymodel.py /app
WORKDIR /app

ENTRYPOINT ["python3", "-u", "my.py"]
