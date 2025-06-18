create database if not exists feedbackdb;

use feedbackdb;

create table if not exists feedback(
    id int auto_increment primary key,
    student_name varchar(100),
    email varchar(100),
    comments text,
    submitted_at timestamp default current_timestamp
);