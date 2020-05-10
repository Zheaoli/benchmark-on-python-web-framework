# benchmark-on-python-web-framework

## Something before

I have already make a benchmark on three Python web frameworks(Django/Flask/FastAPI). The test result just for personal review & comment. It does not represent the real performance on the real production environment

## Pre-Requirements

I have already prepared some environments for this benchmark. All off those environments are supported by Azure(Thanks Microsoft). Here's the detail

### Hardware

1. a Kubernetes cluster with three nodes(each node gets four cores CPU and 16G RAM). Each server is deployed with three pods and each pod has been scheduled to a different node. There is no resource limit on server deployment.

2. The Kubernetes Ingress Controller made by Nginx is used to be the load balancer. Every pod for the server gets the same weight.

3. MySQL service is used at the database. The version is 8.0 and the server gets 2 cores CPU and 8G RAM with a single node.

### Test Tools

I choice the JMeter as the test tool. 

1. a Master Pod to schedule the test task

2. two slave Pod to run the test task

3. use Inluxdb as the data collector

4. use the Grafana as the dashboard

Here's the architecture

![image](https://user-images.githubusercontent.com/7054676/81506493-4479da00-9329-11ea-9a94-fafaeda26698.png)

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

![image](https://user-images.githubusercontent.com/7054676/81506736-14333b00-932b-11ea-8a18-67ef92857593.png)

#### Flask

![image](https://user-images.githubusercontent.com/7054676/81506749-2319ed80-932b-11ea-87cc-9a2a9fd3ea1b.png)

#### FastAPI

![image](https://user-images.githubusercontent.com/7054676/81506763-3cbb3500-932b-11ea-83c6-239faae6f1fa.png)

