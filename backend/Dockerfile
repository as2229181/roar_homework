FROM python:3.11-alpine3.18

COPY ./app /app
COPY ./scripts /scripts
WORKDIR /app

EXPOSE 8000

RUN apk update && \
	apk add --update --no-cache --virtual .tmp-build-deps \
	build-base  musl-dev gcc libffi-dev python3-dev && \
	pip install poetry && \
	poetry config virtualenvs.create false && \
	poetry install --no-dev && \
	apk del .tmp-build-deps


ENV PATH="/scripts:/py/bin:$PATH"

CMD [ "run.sh" ]