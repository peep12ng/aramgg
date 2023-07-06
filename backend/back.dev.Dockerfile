FROM python:3.9

WORKDIR /backend

ADD . .

RUN python3 -m pip install -U pip
RUN pip install -r requirements.txt
ENV RIOT_API_KEY=RGAPI-4b765b72-435b-4e69-b1ee-0be1fa72e5ba

CMD ["uwsgi", "app.ini"]