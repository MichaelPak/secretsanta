FROM python:2.7-alpine

RUN apk update && \
 apk add postgresql-libs git && \
 apk add --virtual .build-deps gcc musl-dev postgresql-dev && \
 pip install pipenv

WORKDIR /usr/src/
COPY Pipfile .
COPY Pipfile.lock .
RUN set -ex && pipenv install --deploy

COPY app/ /usr/src/app/
COPY conf/run.sh .
COPY manage.py .

ENTRYPOINT ["run.sh"]
