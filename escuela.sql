CREATE DATABASE IF NOT EXISTS escuela;

use escuela;

CREATE TABLE IF NOT EXISTS usuarios(
	id			int(25) auto_increment not null,
    nombre 		varchar(45),
    apellidos	varchar(45),
    email		varchar(50) not null,
    password	varchar(255) not null,
    fecha		date not null,
    constraint pk_usuario primary key(id),
    constraint uq_email unique(email)
)ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS notas(
	id			int(25) auto_increment not null,
    usuario_id	int(25) not null,
    titulo		varchar(255) not null,
    descripcion mediumtext,
    fecha		date not null,
    constraint	pk_notas primary key(id),
    constraint fk_notas_usuarios foreign key(usuario_id) references usuarios(id)
)ENGINE=InnoDB;

show full tables  from escuela;