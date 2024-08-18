FROM python:3.12
RUN apt update && apt install -y libmariadb-dev
COPY . /django-code
RUN cd /django-code && ls . && pip install -r requirements.txt
WORKDIR /django-code
ENTRYPOINT ["bash","-c","gunicorn -c config/config.py django_code.wsgi"]
# 