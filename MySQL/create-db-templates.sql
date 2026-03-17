CREATE DATABASE db_matriculas
    DEFAULT CHARACTER SET = 'utf8mb4';

show DATABASES;

use db_matriculas;

show tables;

-- SENTENCIAS DDL
--CREAR UNA TABLA

CREATE TABLE estudiantes (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nro_documento VARCHAR(20) NOT NULL,
    nombre VARCHAR(255) NOT NULL,
    email VARCHAR(100)
);