### <span style = "color:#6a9955"> LEFT JOIN </span>
Um tipo de `OUTER JOIN`  
![alt text](img/left-join.png "Left Join")  

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

Esse tipo de join vai retornar todos os elementos da tabela a esquerda (tabela que vem do `FROM`), e retorna eles independente de eles terem par ou não na outra tabela, mas caso tenham, ele retorna seus pares.

```sql
SELECT t1.emp_name, t1.hire_date, t2.dept_name
FROM employers AS t1
LEFT JOIN departments as t2
ON t1.dept_id = t2.dept_id ORDER BY emp_id;
```

### <span style = "color:#6a9955"> Output Esperado: </span>
| emp_id | emp_name     | hire_date  | dept_name       |
|--------|--------------|------------|-----------------|
|      1 | Ethan Hunt   | 2001-05-01 | Human Resources |
|      2 | Tony Montana | 2002-07-15 | Administration  |
|      3 | Sarah Connor | 2005-10-18 | Sales           |
|      4 | Rick Deckard | 2007-01-03 | Finance         |
|      5 | Martin Blank | 2008-06-24 | NULL            |
