FROM python:3.12
COPY . /starlette-code
RUN cd /starlette-code && pip install -r requirements.txt
WORKDIR /starlette-code
ENTRYPOINT ["bash","-c","uvicorn --host 0.0.0.0 --port 12345 --workers 11 app:app --loop uvloop"]
# 