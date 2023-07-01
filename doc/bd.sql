CREATE DATABASE zeus
DEFAULT CHARACTER SET utf8mb4
DEFAULT COLLATE utf8mb4_general_ci;

USE zeus;

CREATE TABLE funcionarios (
	id_funcionarios INT NOT NULL auto_increment,
	nome VARCHAR(100) NOT NULL,
	cpf VARCHAR(14) NOT NULL UNIQUE,
	n_contato VARCHAR(20),
	cargo VARCHAR(50),
	data_admissao DATE NOT NULL,
	pix VARCHAR(50),
	PRIMARY KEY (id_funcionarios)
);
	
INSERT INTO funcionarios (nome, cpf, n_contato, cargo, data_admissao, pix) VALUES (%s, %s, %s, %s, %s, %s)
