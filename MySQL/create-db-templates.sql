CREATE DATABASE db_matriculas
    DEFAULT CHARACTER SET = 'utf8mb4';

show DATABASES;

use db_matriculas;

show tables;

-- SENTENCIAS DDL
--CREAR UNA TABLA

CREATE TABLE alumno (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nro_documento VARCHAR(20) NOT NULL,
    nombre VARCHAR(255) NOT NULL,
    email VARCHAR(100)
);

ALTER TABLE alumno
    ADD COLUMN nota INT DEFAULT 0;

DROP TABLE estudiantes;

insert into alumno(nro_documento,nombre) values('100','cesar');

INSERT INTO alumno(nro_documento,nombre,nota)
VALUES
('200','ana',15),
('300','luis',20),
('400','jose',11),
('500','raul',10),
('600','carmen',13),
('700','jorge',16),
('800','daniel',20),
('900','luisa',17),
('1000','pedro',5);

SELECT * FROM alumno;

SELECT nombre,nota FROM alumno;

-- select con where
SELECT * FROM alumno
WHERE nota >= 10;

SELECT nombre,nota FROM alumno
WHERE nombre like '%l%';

--actualizar y eliminar datos

UPDATE alumno
SET email = 'codigo@gmail.com'