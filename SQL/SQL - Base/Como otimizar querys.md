# Como otimizar querys SQL
---
## Otimizador SQL
Muitas das propostas de melhora de desempenho desse md vão mencionar o Otimizador SQL que é basicamente um "programa" nativo do sql que roda antes da query para criar um plano de execução otimizado (ele não é externo, ele é nativo do sql e sempre esteve ai rodando nas suas querys).
#### Exemplo:
Em uma query como essa abaixo, o otimizador SQL determina um plano de execução em passos (nesse caso do 1 ao 11), para fazer uma execução mais eficiente dessa query sem alterar seu resultado.
```sql
(8) SELECT (9) DISTINCT (11) <TOP quantidade> <lista de campos de retorno>
 (1) FROM <tabela>
 (3) <tipo de junção> JOIN <tabela> ON (2) <condições da junção>
 (4) WHERE <condições where >
 (5) GROUP BY <lista de agrupamento>
 (6) WITH {CUBE | ROLLUP}
 (7) HAVING <condições having>
(10) ORDER BY <lista de campos>
```

## Indices
Uso de indice é recomendado quando a consulta sera feita em tabelas grandes. Isso fara com que todas as tabelas precisem de uma chave-primária.  </br>  
Normalmente são criados em colunas que são acessadas com maior frequência e podem ser criados em uma unica coluna ou um grupo delas.
* #### Indices clusterizados e não clusterizados
    * Clusterizados: Uma tabela pode ter apenas um desses, eles determinam a sequencia de armazenamentos de registros em uma tabela e são usados em campos de busca frequente ou que são acessados de forma ordenada.
    * Não clusterizados: Os dados são armazenados em um local diferente e referenciados por ponteiros, em geral são usados em: critérios de pesquisa; usados para se juntar a outras tabelas; usados como campos de chave estrangeira ou na cláusula order by.
    Eles não permitem o uso de text, ntext, image, porém ele permite o uso de view então...

## Views indexadas
Podem ser usadas de duas maneiras diferentes. Primeira, pode ser chamada a partir de uma consulta (modo convencional), dessa forma ele é capaz de retornar os resultados da view quase que instantaneamente. Segunda, o otimizador SQL e o gerenciador do banco aplicam automaticamente os indices das views quando existem e são possiveis de serem usados.  
O primeiro indice de uma view é sempre um indice clusterizado, os outros podem ser não clusterizados.

## Uso de Union
O union junta dois conjuntos eliminando os repetidos, é a melhor escolha quando se precisa juntar dois conjuntos de select e você sabe que eles tem linhas duplicadas, caso não tenha é melhor o Union All, ja que ele não perdera tempo e recursos executando o comando distinct.
```sql
(1)
SELECT a.nome_columa1
   FROM tabela1 a
   WHERE NOT EXISTS (SELECT b.nome_columa2 FROM tabela2 b WHERE b.nome_columa2   = a.nome_columa1)

(2)
SELECT a.nome_columa1
   FROM tabela1 a
     LEFT JOIN tabela2 b ON b.nome_columa2   = a.nome_columa1
   WHERE b.nome_columa2 IS NULL

(3)
SELECT nome_columa1
   FROM tabela1
   WHERE nome_columa1 NOT IN (SELECT nome_columa2 FROM tabela2)
```
Em cada uma das consultas apresentadas o resultado é o mesmo. Porém, qual delas tem a melhor performance? Assumindo que todo o resto é igual, a versão que tem o melhor desempenho é a primeira (1) e a última (3) é a pior. O comando not exists (ou exists) é o mais eficiente.

## Uso do comando Group By
Deve ser usado apenas se ouver função agregada (quando se trata de performance), nesse caso deve-se considerar as seguintes recomendações ao usar o group by.
* O número de linhas de retorno a partir da consulta deve ser o menor possível;

* Manter o número de agrupamentos o mais limitado possível;

* Não agrupar colunas redundantes;

* Se existe um join na mesma instrução select que tem um group by, tente reescrever uma consulta utilizando uma subconsulta em vez de usar o join. Se for possível fazer isso, o desempenho será melhor. Se for necessário usar um join, utilize as colunas do group by com a mesma coluna da tabela em que a função está sendo usada;

* Considere adicionar um order by para a(s) mesma(s) coluna(s) existente(s) no group by. Isso pode fazer com que ele tenha um melhor desempenho.
###### Fonte
https://www.devmedia.com.br/otimizacao-de-consultas-sql/33485
