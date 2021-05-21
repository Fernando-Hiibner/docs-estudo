### <span style = "color:#6a9955"> FULL JOIN </span>
Um tipo de `OUTER JOIN`  
![alt text](img/full-join.png "Full Join")  

### <span style = "color:#6a9955"> Tabela de Funcionarios (employers) </span>  
|emp_id  | emp_name     | hire_date  | dept_id |
|--------|--------------|------------|---------|
|      1 | Ethan Hunt   | 2001-05-01 |       4 |
|      2 | Tony Montana | 2002-07-15 |       1 |
|      3 | Sarah Connor | 2005-10-18 |       5 |
|      4 | Rick Deckard | 2007-01-03 |       3 |
|      5 | Martin Blank | 2008-06-24 |    NULL |  

### <span style = "color:#6a9955"> Tabela de Departamentos (departments) </span>   
| dept_id | dept_name        |
|---------|------------------|
|       1 | Administration   |
|       2 | Customer Service |
|       3 | Finance          |
|       4 | Human Resources  |
|       5 | Sales            | 

Nesse caso ele vai pegar todas as combinações de `LEFT` e `RIGHT OUTER JOIN` e retornar, mesmo que sejam repetidos ou nulos, é exatamente isso, ele vai retornar uma tabela combinada das duas outras funções.

```sql
SELECT t1.emp_name, t1.hire_date, t2.dept_name
FROM employers AS t1
FULL JOIN departments AS t2;
```

### <span style = "color:#6a9955"> Output Esperado: </span>
| emp_id | emp_name     | hire_date  | dept_name        |
|--------|--------------|------------|------------------|
|   NULL | NULL         | NULL       | Customer Service |
|      1 | Ethan Hunt   | 2001-05-01 | Human Resources  |
|      1 | Ethan Hunt   | 2001-05-01 | Human Resources  |
|      5 | Martin Blank | 2008-06-24 | NULL             |
|      4 | Rick Deckard | 2007-01-03 | Finance          |
|      4 | Rick Deckard | 2007-01-03 | Finance          |
|      3 | Sarah Connor | 2005-10-18 | Sales            |
|      3 | Sarah Connor | 2005-10-18 | Sales            |
|      2 | Tony Montana | 2002-07-15 | Administration   |
|      2 | Tony Montana | 2002-07-15 | Administration   |