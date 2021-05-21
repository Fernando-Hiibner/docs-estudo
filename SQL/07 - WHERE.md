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
