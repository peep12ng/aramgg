FROM python:3.9

WORKDIR /backend

ADD . .

RUN python3 -m pip install -U pip
RUN pip install -r requirements.txt
ENV RIOT_API_KEY={RIOT_API_KEY}

CMD ["/bin/bash", "/backend/docker-entrypoint.sh"]