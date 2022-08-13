FROM python:3.8-slim-buster

WORKDIR /myportal
# pip3 freeze > requirements.txt
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]


#docker run --publish 8000:8000 python-django