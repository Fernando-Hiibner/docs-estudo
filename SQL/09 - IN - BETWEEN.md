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