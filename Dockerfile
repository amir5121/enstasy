FROM python:3.6-alpine
# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

ENV INSTALL_PATH /srv

ADD ./requirements.txt /srv/enstasy/requirements.txt

RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

# RUN chmod +x run.sh
# RUN chmod +x uwsgi.sh
# RUN chmod +x telegram_bot.sh

RUN apk add --no-cache --virtual .build-deps \
  build-base postgresql-dev libffi-dev gcc g++ jpeg-dev zlib-dev \
  && pip install --upgrade pip \
  && pip install -r requirements.txt \
  && find /usr/local \
  \( -type d -a -name test -o -name tests \) \
  -o \( -type f -a -name '*.pyc' -o -name '*.pyo' \) \
  -exec rm -rf '{}' + \
  && runDeps="$( \
  scanelf --needed --nobanner --recursive /usr/local \
  | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
  | sort -u \
  | xargs -r apk info --installed \
  | sort -u \
  )" \
  && apk add --virtual .rundeps $runDeps \
  && apk del .build-deps

ENV DJANGO_ENV=prod
ENV DOCKER_CONTAINER=1
