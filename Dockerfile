FROM python:3.7-slim-buster AS base
ARG PYTHON_ENV
ENV PYTHON_ENV ${PYTHON_ENV}
ENV HOME /app
RUN pip install poetry
WORKDIR ${HOME}

FROM base AS dependencies
COPY poetry.lock pyproject.toml ${HOME}/
RUN poetry config settings.virtualenvs.create false \
    && poetry install $(test "$PYTHON_ENV" = production && echo "--no-dev")  --no-interaction --no-ansi

FROM dependencies AS source
COPY src/ ${HOME}/src

FROM source AS release
CMD gunicorn --bind 0.0.0.0:${PORT} src.wsgi:APP

FROM source AS development
CMD python -m src.server