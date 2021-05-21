### <span style = "color:#6a9955"> AND / OR </span>
AND e OR funcionam exatamente como em outras linguagems, unico exemplo que é interessante de mostrar é caso tenha que se combinar os dois.
```sql
--age == idade, salary == salario, atributos ficticios pro exemplo
SELECT * 
FROM persons 
WHERE age > 18 AND (salary < 1000 OR salary > 5000);
```
