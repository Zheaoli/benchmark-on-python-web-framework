# benchmark-on-python-web-framework

## Something before

I have already make a benchmark on three Python web frameworks(Django/Flask/FastAPI). The test result just for personal review & comment. It does not represent the real performance on the real production environment

## Pre-Requirements

I have already prepared some environments for this benchmark. All of those environments are supported by Azure(Thanks Microsoft). Here's the detail

### Hardware

1. a Kubernetes cluster with three nodes(each node gets four cores CPU and 16G RAM). Each server is deployed with three pods and each pod has been scheduled to a different node. There is no resource limit on server deployment.

2. The Kubernetes Ingress Controller made by Nginx 1.7.10 is used to be the load balancer. Every pod for the server gets the same weight.

3. MySQL service is used at the database. The version is 8.0 and the server gets 8 cores CPU and 16G RAM with a single node.

### Test Tools

I choice the JMeter as the test tool, the influxDB as time database, grafana to analysis the result

Here's the Detail

1. 3 x 8C16G VM to run JMeter Server to send the request to server. Here's 1000 threads on each server

2. use 1 x 8C16G to run the influxdb server.

### Test Method

As before, I use MySQL as the test database. I created a SQL table like this

```sql
create table  if not exists  `demo_data`
(
    `id`          bigint(20)   not null auto_increment,
    `name`        varchar(255) not null,
    `create_time` timestamp default CURRENT_TIMESTAMP,
    `update_time` timestamp default CURRENT_TIMESTAMP,
    primary key (`id`),
    index (`name`)
) charset = utf8mb4
  engine = innodb;
```

I have already push a million random data in this table. the `name` data is a random string with a random size between 1-255

The server will query a random string with a random size between 1-255 is  existed in this table or not

### Deploy Config

I have already made some different config for Django/Flask/FastAPI

* Django: Gunicorn as the WSGI server, Gevent as the worker. I also use the [greenify](https://github.com/douban/greenify) to patch the MySQL client which is implemented by C, so it can be scheduled by Gevent after the patch. Each server is run with 7 workers.

* Flask: Gunicorn as the WSGI server, Gevent as the worker. I also use the [greenify](https://github.com/douban/greenify) to patch the mysqlclient which is implemented by C, so it can be scheduled by Gevent after the patch. Each server is run with 7 workers.

* FastAPI: Uvicorn as the ASGI server, the [databases](https://github.com/encode/databases) as async ORM. Each server is run with 7 workers.

## Results

### The Origin Results

#### Django

![image](https://user-images.githubusercontent.com/7054676/117008718-97f4ed00-ad1d-11eb-9ffa-9091a62713d3.png)

#### Flask

![image](https://user-images.githubusercontent.com/7054676/117008814-b2c76180-ad1d-11eb-841f-79e17a277813.png)

#### FastAPI

![image](https://user-images.githubusercontent.com/7054676/117008767-a6430900-ad1d-11eb-9b5d-244f261411ee.png)
