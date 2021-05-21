### <span style = "color:#6a9955"> JOIN </span>
Tipo       | Descrição
---        | ---
INNER JOIN | No `INNER JOIN` o resultado será apenas as linhas que tem um par na outra tabela, por exemplo, existe uma tabela de funcionario que tem as informações de todos os funcionarios e uma chave estrangeira que se chama `dept_id` que liga ela a outra tabela que contem as informações sobre os departamentos, o inner join só retornará os funcionarios que tem um departamento, ou os departamentos que tem algum funcionario.
OUTER JOIN | Funciona como uma extensão do `INNER JOIN`, nesse caso ele retornará as colunas mesmo que não tenham pares. Existem três tipos de `OUTER JOIN`, o `LEFT OUTER JOIN`, `RIGHT OUTER JOIN` e `FULL OUTER JOIN`.
CROSS JOIN | Nesse tipo de `JOIN`, cada linha de uma tabela será combinada com todas as outras linhas da outra tabela, até que todas as linhas tenham sido combinadas com todas as outras linhas da outra tabela.