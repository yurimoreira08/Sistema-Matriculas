CREATE TABLE Pessoa (
    idPessoa SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cpf VARCHAR(14) UNIQUE NOT NULL,
    email VARCHAR(100),
    dataNascimento DATE
); 

CREATE TABLE Aluno (
    idAluno SERIAL PRIMARY KEY,
    emailInstitucional VARCHAR(100),
    idPessoa INT UNIQUE NOT NULL,
    FOREIGN KEY (idPessoa) REFERENCES Pessoa(idPessoa) ON DELETE CASCADE
); 

CREATE TABLE Professor (
    idProfessor SERIAL PRIMARY KEY,
    areaEspecializacao VARCHAR(100),
    emailInstitucional VARCHAR(100),
    idPessoa INT UNIQUE NOT NULL,
    FOREIGN KEY (idPessoa) REFERENCES Pessoa(idPessoa) ON DELETE CASCADE
); 

CREATE TABLE Funcionario (
    idFuncionario SERIAL PRIMARY KEY,
    cargo VARCHAR(50),
    emailInstitucional VARCHAR(100),
    idPessoa INT UNIQUE NOT NULL,
    FOREIGN KEY (idPessoa) REFERENCES Pessoa(idPessoa) ON DELETE CASCADE
); 

CREATE TABLE Curso (
    idCurso SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cargaHoraria INT
); 

CREATE TABLE Disciplina (
    idDisciplina SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cargaHoraria INT,
    codigoDisciplina VARCHAR(20),
    idCurso INT,
    FOREIGN KEY (idCurso) REFERENCES Curso(idCurso) ON DELETE CASCADE
); 

CREATE TABLE Turma (
    idTurma SERIAL PRIMARY KEY,
    periodo VARCHAR(20),
    ano INT,
    horario VARCHAR(50),
    idCurso INT,
    FOREIGN KEY (idCurso) REFERENCES Curso(idCurso) ON DELETE CASCADE
); 

CREATE TABLE Matricula (
    idMatricula SERIAL PRIMARY KEY,
    dataMatricula DATE DEFAULT CURRENT_DATE,
    situacao VARCHAR(20) DEFAULT 'Ativo',
    nota1 NUMERIC(4,2) CHECK (nota1 >= 0 AND nota1 <= 10),
    nota2 NUMERIC(4,2) CHECK (nota2 >= 0 AND nota2 <= 10),
    idAluno INT NOT NULL,
    idTurma INT NOT NULL,
    FOREIGN KEY (idAluno) REFERENCES Aluno(idAluno) ON DELETE CASCADE,
    FOREIGN KEY (idTurma) REFERENCES Turma(idTurma) ON DELETE CASCADE,
    UNIQUE (idAluno, idTurma) 
); 

CREATE TABLE Professor_Turma (
    idProfessor INT NOT NULL,
    idTurma INT NOT NULL,
    PRIMARY KEY (idProfessor, idTurma),
    FOREIGN KEY (idProfessor) REFERENCES Professor(idProfessor) ON DELETE CASCADE,
    FOREIGN KEY (idTurma) REFERENCES Turma(idTurma) ON DELETE CASCADE
); 