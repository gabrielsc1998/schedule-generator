FROM python:3.12.0

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONFAULTHANDLER=1

RUN pip install --no-cache-dir --upgrade pip

RUN useradd -ms /bin/bash python && \
    chown -R python:python /var/log

USER python

WORKDIR /home/python/app

ENV PATH $PATH:/home/python/.local/bin

CMD ["tail", "-f", "/dev/null"]