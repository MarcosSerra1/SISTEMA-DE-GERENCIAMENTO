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

CREATE TABLE Obra (
  id_obra INT NOT NULL AUTO_INCREMENT,
  nome VARCHAR(100) NOT NULL,
  endereco VARCHAR(200),
  data_inicio DATE,
  data_conclusao DATE,
  PRIMARY KEY (id_obra)
);

CREATE TABLE FuncionarioObra (
  id_funcionarioObra INT NOT NULL AUTO_INCREMENT,
  funcionario_id INT,
  obra_id INT,
  FOREIGN KEY (funcionario_id) REFERENCES Funcionarios(id_funcionarios),
  FOREIGN KEY (obra_id) REFERENCES Obra(id_obra),
  PRIMARY KEY (id_funcionarioObra)
);
	
	
	
	
INSERT INTO funcionarios (nome, cpf, n_contato, cargo, data_admissao, pix) VALUES (%s, %s, %s, %s, %s, %s)

INSERT INTO obra (nome, endereco, data_inicio, data_conclusao) VALUES (%s, %s, %s, %s)