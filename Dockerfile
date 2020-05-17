#base image
FROM python:3.6
#set work dir
WORKDIR /src

#install dependencies
RUN pip install pipenv
COPY Pipfile Pipfile.lock /src/
RUN pipenv install --system 

#copy project
COPY . ./