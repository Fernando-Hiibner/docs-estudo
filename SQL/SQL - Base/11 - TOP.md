### <span style = "color:#6a9955"> TOP </span>
`TOP` é o comando usado no SQL Server e MS Acess para determinar quantas linhas serão retornadas por uma query.
Esse comando é o mesmo que `LIMIT` no MySQL e `ROWNUM` no Oracle.

```sql
SELECT TOP 3 *
FROM persons
ORDER BY salary DESC;
```

Tambem é possivel usar o `PERCENT` após um número do `TOP` para retornar uma porcentagem das linhas.
Valores `float` são arredondados para o `int` acima mais próximo. Ex.: 1.5 -> 2

```sql
SELECT TOP 30 PERCENT *
FROM persons
ORDER BY salary DESC;
```