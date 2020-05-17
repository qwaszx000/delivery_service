#base image
FROM python:3.6
#set work dir
WORKDIR /src

# install mysqlclient
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev jpeg-dev zlib-dev \
    && apk add --no-cache mariadb-dev mariadb-client

#install dependencies
RUN pip3 install pipenv
RUN apk add libjpeg
RUn apt-get install libopenjpeg2 libjpeg-dev zlib1g-dev libpng12-dev
COPY Pipfile Pipfile.lock /src/

RUN pipenv uninstall pillow
RUN pip uninstall pillow
RUN pip install pillow
RUN pipenv install --system  --python 3.6

#copy project
COPY . /src/