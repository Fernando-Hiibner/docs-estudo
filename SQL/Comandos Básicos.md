### <span style = "color:#6a9955"> CREATE DATABASE </span>  
```sql
CREATE DATABASE IF NO EXISTS <nome_do_banco>;
CREATE DATABASE <nome_do_banco>;
USE <nome_do_banco>;
```

### <span style = "color:#6a9955">CREATE TABLE  </span>
```sql
CREATE TABLE IF NOT EXISTS persons (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    birth_date DATE,
    phone VARCHAR(15) NOT NULL UNIQUE
);
```
```sql
CREATE TABLE persons(
	id INT NOT NULL PRIMARY KEY IDENTITY(1,1),
	name VARCHAR(50) NOT NULL,
	birth DATE,
	phone VARCHAR(15) NOT NULL UNIQUE
);
```

### <span style = "color:#6a9955">Tipos de dados </span> 
Tipo      | Descrição
---       | ---
INT       | Guarda valores numericos entre -2147483648 até 2147483647  
DECIMAL   | Guarda valores decimais com precisão exata  
CHAR      | Gaurda strings de tamanho fixo com um tamanho máximo de 255 caracteres  
VARCHAR   | Guarda strings de tamanho variavel com um tamanho máximo de 65,535 caracteres  
TEXT      | Guarda strings com um valor máximo de 65,535 caracteres  
DATE      | Gaurda datas no formato YYYY-MM-DD  
DATETIME  | Guarda datas com horas no formato YYYY-MM-DD HH:MM:SS  
TIMESTAMP | Guard valores do tipo TIMESTAMP que é basicamente o numero de segundos desde o Unix Epoch   ('1970-01-01 00:00:01' UTC)  
---
Ref: https://www.tutorialrepublic.com/sql-reference/mysql-data-types.php  

### <span style = "color:#6a9955">MODIFIERS / CONSTRAINTS  </span>
Constante | Descrição
--- | ---
PRIMARY KEY | Marca aquele atributo como chave principal da table  
FOREIGN KEY | Relaciona uma table com a outra importanto como chave estrangeira a chave primaria da tabela que quer relacionar  
NOT NULL    | Não aceitará valor NULL  
UNIQUE      | Garante que cada linha daquela coluna tera um valor unico  
DEFAULT     | Determina um valor padrão para determinada coluna  
CHECK       | Só permite valores que estão de acordo com sua condição, um "if" basicamente  
---

### <span style = "color:#6a9955">Exemplos:  </span>
Constante | Descrição
--- | ---
PRIMARY KEY | id INT NOT NULL PRIMARY KEY 
FOREIGN KEY | dept_id INT</br>FOREIGN KEY (dept_id) REFERENCES departments(dept_id)  
NOT NULL    | name VARCHAR(30) NOT NULL  
UNIQUE      | phone VARCHAR(15) NOT NULL UNIQUE  
DEFAULT     | country VARCHAR(30) NOT NULL DEFAULT 'Australia'  
CHECK       | salary INT NOT NULL CHECK (salary >= 3000 AND salary <= 10000)  
---

### <span style = "color:#6a9955">INSERT INTO  </span>
### <span style = "color:#6a9955">Multiplos conjuntos de values indicam inserção em novas linhas  </span>
```sql
INSERT INTO <nome_da_tabela> (coluna1, coluna2,...) 
VALUES (value1, value2,...), (value3, value4,...);
```
### <span style = "color:#6a9955">Exemplo:  </span>
```sql
INSERT INTO persons (name, birth, phone) 
VALUES ('Baozi', '1970-01-01', '(14)99000-0001'), ('Fernando', '2002-09-03', '(14)99000-0002');
```

### <span style = "color:#6a9955">SELECT  </span>
```sql
SELECT <coluna1>, <coluna2>, <colunaN> 
FROM <nome_da_tabela>;
```
### <span style = "color:#6a9955">Selecionar todos  </span>
```sql
SELECT * 
FROM <nome_da_tabela>;
```

### <span style = "color:#6a9955">Exemplo: </span> 
```sql
SELECT name, birth 
FROM persons;
```

### <span style = "color:#6a9955"> WHERE </span>
Usada com o Select, Update e Delete

### <span style = "color:#6a9955"> Exemplo: </span>
```sql
SELECT * FROM <nome_da_tabela> 
WHERE <condição1>, condição2...;
```

### <span style = "color:#6a9955"> Operadores Where </span>
Operador | Descrição | Exemplo
--- | --- | ---
= | Igual | WHERE id = 2
\> | Maior que | WHERE id > 2
< | Menor que | WHERE id < 2
\>= | Maior ou igual a | WHERE id >= 2
<= | Menor ou igual a | WHERE id <= 2
LIKE | Se o padrão for igual | WHERE nome LIKE "Fer"
IN | Checa se o valor corresponde a algum valor de uma lista de subvalores | WHERE pais IN ('Brazil', 'Alemanha')
BETWEEN | Checa se o valor esta entre x e y | WHERE idade BETWEEN 12 AND 18
---

### <span style = "color:#6a9955"> AND / OR </span>
AND e OR funcionam exatamente como em outras linguagems, unico exemplo que é interessante de mostrar é caso tenha que se combinar os dois.
```sql
--age == idade, salary == salario, atributos ficticios pro exemplo
SELECT * 
FROM persons 
WHERE age > 18 AND (salary < 1000 OR salary > 5000);
```

### <span style = "color:#6a9955"> IN / BETWEEN </span>
IN funciona exatamente como o explicado la em cima nos operadores, o grande gás dele aqui é que ele pode ser NOT
```sql
--dept_id == department id, atributo ficticio pro exemplo, seria departamento de trabalho
SELECT * 
FROM persons 
WHERE dept_id NOT IN (1, 3);
```

O BETWEEN tem usos interessantes nesse tópico, ele pode ser usado pra encontrar coisas em um range de INT, mas não é só isso, com o auxilio de outras funções e em outros casos esse operador pode fazer muitas coisas.
```sql
--CAST converte um tipo para outro se possivel, é tipo fazer (float)2 em C / C++ / C#
--GETDATE retorna a data atual do sistema no formato 'YYYY-MM-DD HH:MM:SS'

SELECT * 
FROM persons 
WHERE birth BETWEEN CAST('2000-01-01 00:00:01' AS DATE) AND CAST(GETDATE() AS DATE);

--Pode ser assim tambem
SELECT * 
FROM persons
WHERE birth BETWEEN CAST('2000-01-01' AS DATE) AND CAST(GETDATE() AS DATE);

--Tambem pode ser usado para encontrar strings que começam entre ranges de letras
SELECT * 
FROM persons 
WHERE name BETWEEN 'A' AND 'E' 
OR name BETWEEN 'G' AND 'Z';
```

### <span style = "color:#6a9955"> ORDER </span>
Usado para ordenar os resultados de select a partir de um critério
```sql
--ASC = Ascending (Crescente)
--DESC = Decresent (Decresente)
SELECT *
FROM persons
ORDER BY name ASC;

--Isso é o mesmo que fazer isso:
SELECT *
FROM persons
ORDER BY name;

--Pq o sorting padrão é crescente(ASC)
SELECT *
FROM persons
ORDER BY name DESC;

--Sorting com multiplas colunas
SELECT *
FROM persons
ORDER BY name, last_name DESC;

SELECT *
FROM persons
ORDER BY name, last_name ASC;

SELECT *
FROM persons
ORDER BY name, last_name DESC;
```





