FROM python:3.7

ADD requirements.txt /usr/src/app/requirements.txt
RUN pip install -r /usr/src/app/requirements.txt
ADD pinger.py /usr/src/app/pinger.py
CMD ["python", "/usr/src/app/pinger.py"]
