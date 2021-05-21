### <span style = "color:#6a9955"> TRUNCATE </span>
Esse comando limpa a tabela mais rápido que o `DELETE`, mas não exclui a tabela (`DELETE` tambem não)

```sql
TRUNCATE TABLE persons;
```

### <span style = "color:#6a9955"> Diferenças entre o DELETE e o TRUNCATE </span>
* `TRUNCATE` deleta e recria a tabela inteira a forma que ela era, com isso o valor de auto-increment reseta para 1.
* `DELETE` permite que você use o `WHERE` para filtrar as linhas a ser excluida, enquanto o `TRUNCATE` não.
* `TRUNCATE` é mais rapido e usa menos recursos do sistema do que o `DELETE`, porque o `DELETE` scaneia a tabela para gerar uma conta de quantas linhas serão excluidas, depois deleta uma por uma e gera um registro no `LOG`, enquanto que o `TRUNCATE` só deleta tudo e recria sem prover nenhuma informação extra.


