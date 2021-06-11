# pull official base image
FROM python:3.7.4

ARG DEVELOPMENT=False

# set working directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY ./poetry.lock ./pyproject.toml ./
RUN pip install --no-cache poetry \
    && poetry config virtualenvs.create false \
    && poetry install $(test "${DEVELOPMENT:=True}" = False && echo "--no-dev") --no-interaction --no-ansi

# add app
COPY ./news_provider .
