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
