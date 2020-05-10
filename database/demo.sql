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