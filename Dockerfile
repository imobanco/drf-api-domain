FROM python:3.8

ARG USER_ID
ARG GROUP_ID

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install netcat dependencies
RUN apt-get update -y && \
        apt-get install -y netcat

# Requirements have to be pulled and installed here, otherwise caching won't work
COPY requirements.txt requirements.txt
COPY requirements-dev.txt requirements-dev.txt
RUN pip install -r requirements-dev.txt

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

COPY . /app

RUN groupadd -g ${GROUP_ID} app_group
RUN useradd -l -u ${USER_ID} -g app_group app_user
RUN chown -R app_user /app/
USER app_user