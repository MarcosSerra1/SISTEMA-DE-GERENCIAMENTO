# Script para criar a estrutura da tabela de funcionários.

# Banco de Dados
CREATE DATABASE zeus
DEFAULT CHARACTER SET utf8mb4
DEFAULT COLLATE utf8mb4_general_ci;

USE zeus;

# Tabela de funcionarios
CREATE TABLE funcionarios (
	id_funcionarios INT NOT NULL auto_increment,
	nome VARCHAR(100) NOT NULL,
	cpf VARCHAR(14) NOT NULL UNIQUE,
	n_contato VARCHAR(20),
	cargo VARCHAR(50),
	data_admissao DATE NOT NULL,
	pix VARCHAR(50),
	camisa VARCHAR(3),
	calca VARCHAR(3),
	bota VARCHAR(3),
	PRIMARY KEY (id_funcionarios)
);