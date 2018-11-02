FROM python:3-alpine

WORKDIR /usr/src/app

RUN pip install pipenv

COPY Pipfile* ./

RUN pipenv install

COPY . .

ENV FLASK_APP todo.py
CMD ["pipenv", "run", "flask", "run", "--host=0.0.0.0"]