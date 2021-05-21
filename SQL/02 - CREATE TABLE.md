### <span style = "color:#6a9955">CREATE TABLE  </span>
Usado para criar todo e qualquer tipo de tabela, as possibilidades são infinitas, elas podem ser de praticamente qualquer tamanho e usadas para praticamente qualquer coisa, são a base de um banco de dados.
Os atributos que colocamos na tabela são suas colunas.
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
