FROM python:3.9
COPY . /flask-code
RUN cd /flask-code && pip install -r requirements.txt
WORKDIR /flask-code
ENTRYPOINT ["bash","-c","gunicorn -c config/config.py app:app"]
# 