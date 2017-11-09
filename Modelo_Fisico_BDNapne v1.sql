-- Geração de Modelo físico
-- Sql ANSI 2003 - brModelo.



CREATE TABLE Atendimento (
numero int PRIMARY KEY,
Profissional varchar(11),
Aluno varchar(11),
data date,
hora varchar(5),
Relato varchar(500)
)

CREATE TABLE Pessoa (
CPF varchar(11) PRIMARY KEY,
Nome varchar(100),
RG varchar(50),
Endereco varchar(100),
Telefone varchar(15),
Profissao varchar(50),
Senha varchar(8),
Turma varchar(10),
Turno varchar(10),
Periodo varchar(10),
Curso varchar(50),
Dificuldade varchar(150)
)

ALTER TABLE Atendimento ADD FOREIGN KEY(Profissional) REFERENCES Pessoa (CPF)
ALTER TABLE Atendimento ADD FOREIGN KEY(Aluno) REFERENCES Pessoa (CPF)
