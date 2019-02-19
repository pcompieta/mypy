FROM python:3.6-alpine

RUN mkdir /app
COPY launcher.py /app
COPY mmlibrary.py /app
COPY mymodel.py /app
WORKDIR /app

ENTRYPOINT ["python3", "-u", "launcher.py"]
