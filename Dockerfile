#base image
FROM python:3.6
#set work dir
WORKDIR /src

#pipenv
RUN pip install pipenv
COPY Pipfile Pipfile.lock /src/
RUN pipenv install --deploy --system --ignore-pipfile --python 3.6
#copy project
COPY . /src/