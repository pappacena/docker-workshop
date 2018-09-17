FROM python:3.6

ADD . /usr/src/app/
WORKDIR /usr/src/app

RUN pip install -r dev-requirements.txt

WORKDIR /usr/src/app/main

CMD ["python", "manage.py", "runserver"]
