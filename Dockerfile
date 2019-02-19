FROM python:3.6-slim-stretch

RUN pip install pandas sklearn

RUN mkdir /app
COPY launcher.py /app
COPY mmlibrary.py /app

COPY mymodel.py /app/model.py
COPY binary.zip /app/mygem.bin

WORKDIR /app

ENTRYPOINT ["python3", "-u", "launcher.py"]
