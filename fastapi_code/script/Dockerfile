FROM python:3.12
COPY . /fastapi-code
RUN cd /fastapi-code && pip install -r requirements.txt
WORKDIR /fastapi-code
ENTRYPOINT ["bash","-c","uvicorn --host 0.0.0.0 --port 12345 --workers 11 app:app --loop uvloop"]
# 