FROM python:3

WORKDIR /backend

ADD . .

RUN python3 -m pip install -U pip
RUN pip install -r requirements.txt

CMD ["python3", "run.py"]