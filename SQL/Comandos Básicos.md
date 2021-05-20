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

https://www.tutorialrepublic.com/sql-reference/mysql-data-types.php  

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
INSERT INTO <nome_da_tabela> (coluna1, coluna2,...) VALUES (value1, value2,...), (value3, value4,...)
```
### <span style = "color:#6a9955">Exemplo:  </span>
```sql
INSERT INTO persons (name, birth, phone) 
VALUES ('Baozi', '1970-01-01', '(14)99000-0001'), ('Fernando', '2002-09-03', '(14)99000-0002');
```

### <span style = "color:#6a9955">SELECT  </span>
```sql
SELECT <coluna1>, <coluna2>, <colunaN> FROM <nome_da_tabela>
```
### <span style = "color:#6a9955">Selecionar todos  </span>
```sql
SELECT * FROM <nome_da_tabela>
```

### <span style = "color:#6a9955">Exemplo: </span> 
```sql
SELECT name, birth FROM persons;
```

### <span style = "color:#6a9955"> WHERE </span>
Usada com o Select e o Update



