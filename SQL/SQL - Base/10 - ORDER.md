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