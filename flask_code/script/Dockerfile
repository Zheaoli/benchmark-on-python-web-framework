FROM python:3.12
RUN apt update && apt install -y libmariadb-dev
COPY . /flask-code
RUN cd /flask-code && pip install -r requirements.txt
WORKDIR /flask-code
ENTRYPOINT ["bash","-c","gunicorn -c config/config.py app:app"]
# 