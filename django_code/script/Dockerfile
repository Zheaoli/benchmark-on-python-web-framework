FROM python:3.9
COPY . /django-code
RUN cd /django-code && pip install -r requirements.txt
WORKDIR /django-code
ENTRYPOINT ["bash","-c","gunicorn -c config/config.py django_code.wsgi"]
# 