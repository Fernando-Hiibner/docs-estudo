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