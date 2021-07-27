
# Como otimizar consultas SQL

## Otimizador SQL
Muitas das propostas de melhora de desempenho desse .md vão mencionar o Otimizador SQL que é basicamente um "programa" nativo do SQL que roda antes da query para criar um plano de execução otimizado (ele não é externo, ele é nativo do SQL e sempre esteve ai rodando nas suas consultas).
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
Normalmente são criados em colunas que são acessadas com maior frequência e podem ser criados em uma única coluna ou um grupo delas.
* #### Indices clusterizados e não clusterizados
    * **Clusterizados:** Uma tabela pode ter apenas um desses, eles determinam a sequencia de armazenamentos de registros em uma tabela e são usados em campos de busca frequente ou que são acessados de forma ordenada.
    * **Não clusterizados:** Os dados são armazenados em um local diferente e referenciados por ponteiros, em geral são usados em: critérios de pesquisa; usados para se juntar a outras tabelas; usados como campos de chave estrangeira ou na cláusula order by.
    Eles não permitem o uso de text, ntext, image, porém ele permite o uso de view então...

## Views indexadas
Podem ser usadas de duas maneiras diferentes. Primeira, pode ser chamada a partir de uma consulta (modo convencional), dessa forma ele é capaz de retornar os resultados da view quase que instantaneamente. Segunda, o otimizador SQL e o gerenciador do banco aplicam automaticamente os indices das views quando existem e são possíveis de serem usados.  
O primeiro índice de uma view é sempre um índice clusterizado, os outros podem ser não clusterizados.

## Uso de Union
O union junta dois conjuntos eliminando os repetidos, é a melhor escolha quando se precisa juntar dois conjuntos de select e você sabe que eles tem linhas duplicadas, caso não tenha é melhor o Union All, já que ele não perdera tempo e recursos executando o comando distinct.
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
Deve ser usado apenas se houver função agregada (quando se trata de performance), nesse caso deve-se considerar as seguintes recomendações ao usar o group by.
* O número de linhas de retorno a partir da consulta deve ser o menor possível;

* Manter o número de agrupamentos o mais limitado possível;

* Não agrupar colunas redundantes;

* Se existe um join na mesma instrução select que tem um group by, tente reescrever uma consulta utilizando uma subconsulta em vez de usar o join. Se for possível fazer isso, o desempenho será melhor. Se for necessário usar um join, utilize as colunas do group by com a mesma coluna da tabela em que a função está sendo usada;

* Considere adicionar um order by para a(s) mesma(s) coluna(s) existente(s) no group by. Isso pode fazer com que ele tenha um melhor desempenho.

## Or em clausulas Join/Where entre colunas e tabelas
O uso do ```or``` entre colunas ou tabelas pode prejudicar muito a performance de uma consulta.
```sql
SELECT DISTINCT
	PRODUCT.ProductID,
	PRODUCT.Name
FROM Production.Product PRODUCT
INNER JOIN Sales.SalesOrderDetail DETAIL
ON PRODUCT.ProductID = DETAIL.ProductID
OR PRODUCT.rowguid = DETAIL.rowguid;
```
Nessa consulta por exemplo a tabela Product contem 504 linhas, e a tabela SalesOrderDetail contém 121317 linhas, porém para a realização da operação com o Or foi necessário 1.2 milhões de leituras e 2 segundos para executar.
Existem diversas formas de substituir o Or por uma operação mais rápida, mas isso depende muito do cenário que a query se encontra e o que aquele Or está tentando atingir, abaixo segue um exemplo de como essa query acima poderia ser otimizada.
```sql
SELECT
	PRODUCT.ProductID,
	PRODUCT.Name
FROM Production.Product PRODUCT
INNER JOIN Sales.SalesOrderDetail DETAIL
ON PRODUCT.ProductID = DETAIL.ProductID
UNION
SELECT
	PRODUCT.ProductID,
	PRODUCT.Name
FROM Production.Product PRODUCT
INNER JOIN Sales.SalesOrderDetail DETAIL
ON PRODUCT.rowguid = DETAIL.rowguid
```
Nesse exemplo o número de leituras caiu de 1.2 milhões para apenas 750 e o tempo caiu pra baixo de 1 segundo.

## Busca "coringa" com Strings
Para colunas de String frequentemente buscadas vale a pena olhar se:
* Índices estão presentes nas colunas pesquisadas;
* Esses índices podem ser usados;
* Se não, podemos usar índices de String completos?
* Se não, podemos usar hashes, n-gramas, ou outra solução?

Sem o uso de uma técnica de otimização de busca por String, o SQL pode demorar demais pra fazer a consulta, exemplo:
```sql
SELECT
	Person.BusinessEntityID,
	Person.FirstName,
	Person.LastName,
	Person.MiddleName
FROM Person.Person
WHERE Person.LastName LIKE '%For%';
```
Ao usar % no começo da String, o uso de índices crescentes se torna impossível, e de forma semelhante, ao usar % no fim de uma String, o uso de índices decrescentes se torna impossível.
Existem diversas formas de otimizar isso:
* Repensar a aplicação. É realmente necessário o uso de uma busca coringa? Se não se livre dela e o problema estará resolvido.
* É possível adicionar mais filtros capazes de reduzir a quantidade de dados que deverão ser lidos? Como por exemplo, data, tempo, status e etc.
* É possível retirar a % de algum dos lados?
* Índice de texto completo (uma String sem %) possível de ser usada? Se sim implemente.
* É possível de implementar uma consulta hash ou uma solução n-grama.

Os 3 primeiros pontos são mais escolhas de design do que métodos de otimização.  
O ultimo método a ser abordado nesse tópico é o n-grama.
O que é um n-grama?  
Nos campos de linguística computacional e probabilidade, um n-grama é uma sequência contígua de n itens de uma determinada amostra de texto ou fala.  
Para se usar um n-grama é necessário entender profundamente as regras de pesquisa usadas pela aplicação.
* Existe um número mínimo ou máximo de caracteres permitidos na busca?
* Buscas vazias são permitidas?
* Múltiplas palavras/frases são permitidas?
* Precisamos armazenar uma Substring no começo da String? Se sim, isso pode ser feito com uma busca por índice.

Após avaliar essas considerações, podemos pegar uma coluna de String e quebra-la em segmentos. Por exemplo, considere um sistema de pesquisa onde o tamanho mínimo da String de pesquisa é de 3 caracteres, e a palavra armazenada é "Dinossauro", as Substrings de dinossauro que possuem 3 caracteres ou mais (Excluindo Din já que é facilmente encontrável com índices) são: ino, inos, inoss, inossa, inossau, inossaur, inossauro, nos, noss, nossa, nossau, nossaur, nossauro, oss, ossa, ossau, ossaur, ossauro, ssa, ssau, ssaur, ssauro, sau, saur, sauro, aur, auro, uro.
Com isso nós podemos criar uma tabela com esses valores (n-grama), e fazer uma busca por igualdade, usando essa tabela e a nossa. Exemplo:
```sql
SELECT
n_gram_table.my_big_table_id_column
FROM  dbo.n_gram_table
WHERE  n_gram_table.n_gram_data  =  'Dino';
```
Assumindo que n_gram.data seja indexado, ele retornara rapidamente os IDs da tabela grande que possui a palavra Dino. A tabela n-grama só precisa de duas colunas, e seu tamanho pode ser limitado usando as regras que definimos acima, mesmo que ela fique grande, ainda sim será muito mais rápida que o método normal.
O problema dessa solução é manutenção, será necessário atualizar a tabela de n-grama toda vez que uma nova linha for inserida na tabela principal, tendo isso em vista, recomenda-se essa aproximação apenas para pequenas Strings, como nome, códigos ZIP, ou números de telefone.
Resumindo, não há soluções simples para resolver o problema de performance de buscas coringas, o que podemos fazer é rever nossas regras de design e arquitetura para tentar retirar o "%", ou limitar a forma que buscamos de forma que permita a implementação de outros filtros.

## Grandes operações de escrita
Esse tópico tratara de um cenário onde a iteração ajuda na performance da consulta e falará sobre contenção de dados.
Ao mexer com grandes operações de escrita, o SQL coloca as tabelas envolvidas na transação em contenção, bloqueando o uso delas por outras tabelas durante o tempo que a transação ta em execução, isso é bom porque garante a segurança e integridade dos dados e confiabilidade dos resultados obtidos, por outro lado, tem a desvantagem de bloquear o uso das tabelas envolvidas na transação até que ela acabe, e isso pode demorar muito.
Além da contenção outro problema é que grandes operações geram muitos logs, o que pode ser perigoso, então é sempre bom ficar de olho para garantir que o log da transação não fique cheio, e principalmente que o disco rígido do servidor não fique também.
Uma boa forma de otimizar isso e evitar grandes períodos de contenção, seria dividir a operações em pequenas operações que afetam poucas linhas por vez, caso isso não seja possível, executar essas operações em momentos do dia que o servidor principal não esta sendo extensivamente usado.
Operações que podem gerar grandes operações de escrita.
* Adicionar uma nova coluna a uma tabela e ir preenchendo a ela inteira.
* Atualizar uma coluna inteira da tabela
* Mudar o tipo de dado de uma coluna
* Importar um grande volume de novos dados
* Arquivar ou deletar um grande número de dados antigos.

## Indices em falta
O SQL Server por meio da ferramenta "plano de execução XML" ou "Índice em falta DMV", mostra índices em falta que provavelmente melhorariam o desempenho de uma query.
![Exemplo das ferramentas mencionadas](https://www.sqlshack.com/wp-content/uploads/2018/06/c-users-epollack-appdata-local-microsoft-windows-1-6.jpeg)
O aviso é util mas é importante levar em consideração algumas coisas antes de usar o que o SQL Server propõe.
* Já existe algum índice semelhante a esse que pode ser modificado pra cumprir esse propósito?
* Precisamos de todas as colunas? Ou um índice apenas nas colunas que vamos filtrar já é o suficiente?
* Quão grande é o impacto do índice? Vai melhorar a query em 98% ou apenas 5%.
* Esse índice já existe e por algum motivo o otimizador de query não ta usando ele?

As vezes os índices sugeridos são excessivos, por exemplo, abaixo está a criação de parte do plano mostrado acima:
```sql
CREATE  NONCLUSTERED  INDEX  <Name  of  Missing  Index,  sysname,>
ON  Sales.SalesOrderHeader (Status,SalesPersonID)
INCLUDE (SalesOrderID,SubTotal)
```
Nesse caso já existe um ID em SalesPersonId. Status é uma coluna que na maioria das vezes tem apenas um valor, o que significa que como uma coluna de ordenação ela não possui muito valor. O impacto de 19% de performance não é tão impressionante, porém se for uma consulta que ocorre muitas vezes durante o dia vale a pena o esforço de adcionar um índice pra isso.
Considere outra sugestão de índice:
![enter image description here](https://www.sqlshack.com/wp-content/uploads/2018/06/c-users-epollack-appdata-local-microsoft-windows-1-7.jpeg)    
Nesse exemplo o índice em falta sugerido é:

```sql
CREATE  NONCLUSTERED  INDEX [<Name of Missing Index, sysname,>]
ON [Person].[Person] ([FirstName])
INCLUDE ([BusinessEntityID],[Title])
```
Dessa vez o índice sugerido aumentaria a performance em 93% e lidaria com a coluna não indexada (FirstName), precisamos colocar BussinesEntityID and Title como colunas de INCLUDE? Pra responder essa questão precisamos pensar "Como sabemos se a performance de uma query está boa?", se apenas ao adicionar o índice resolver o problema, então parar nele é a decisão correta, caso a performance continue ruim, o próximo passo seria adiciona-las.
Em quanto tivermos em mente que índices precisam de manutenção e que eles diminuem a performance de operações de escrita, nós podemos abordar índice de uma perspectiva pragmática.

### Sobrecarregando uma tabela de índices
Quando uma tabela tem muitos índices, as operações de escrita nela se tornam muito lentas (Como UPDATE, DELETE e INSERT), porque sempre que elas mudam algo, elas tem que mudar os índices, além disso índices consomem espaço de armazenamento.
### Deixando uma tabela com poucos índices
Uma query com poucos índices não processa muito bem operações de leitura
### Sem índice clusterizado/Primary key
Todas as tabelas devem ter um índice clusterizado e uma Primary Key. Índices clusterizados quase sempre são mais performáticos que índices de heap, e provem a infraestrutura necessária para a adição de índices não clusterizados. A Primary Key provem informações valiosas para o otimizador de querys. Se encontrar uma tabela sem algum desses dois, considere a adição deles como prioridade máxima e resolva isso antes de continuar pesquisando outras causas.

## Muitas tabelas
Para ajudar o otimizador SQL a encontrar o melhor plano de execução devemos diminuir o número de tabelas em uma query, visto que, cada tabela nova na query aumenta sua complexidade de forma fatorial, e o otimizador tem pouco tempo para encontrar entre todos os planos possíveis o melhor.
Baseado na forma que as tabelas forem ligadas, elas se encaixarão em uma das duas formas abaixo:
* **Left-Deep Tree**: A join B, B join C, C join D, D join E, etc… Essa é uma query onde a maioria das tabelas se juntam de forma sequencial uma depois da outra.
* **Bushy Tree**: A join B, A join C, B join D, C join E, etc…Essa é uma query onde as tabelas se dividem em múltiplas unidades lógicas em cada raiz da árvore.

Bush Tree:
![enter image description here](https://www.sqlshack.com/wp-content/uploads/2018/06/word-image-43.png)  
Left Deep Tree
![enter image description here](https://www.sqlshack.com/wp-content/uploads/2018/06/word-image-44.png)  
Considerando que a Left-Deep Tree é ordenada de forma mais parecida com a que as tabelas são ligadas, o número de candidatos de plano de execução diminuem (As formulas matemáticas incluídas nas imagens são usadas para encontrar a quantidade de planos de execução possíveis para aquela árvore).
Para enfatizar isso, considere essa query envolvendo 12 tabelas:
```sql
SELECT  TOP  25
Product.ProductID,
Product.Name  AS  ProductName,
Product.ProductNumber,
CostMeasure.UnitMeasureCode,
CostMeasure.Name  AS  CostMeasureName,
ProductVendor.AverageLeadTime,
ProductVendor.StandardPrice,
ProductReview.ReviewerName,
ProductReview.Rating,
ProductCategory.Name  AS  CategoryName,
ProductSubCategory.Name  AS  SubCategoryName
FROM  Production.Product
INNER  JOIN  Production.ProductSubCategory
ON  ProductSubCategory.ProductSubcategoryID  =  Product.ProductSubcategoryID
INNER  JOIN  Production.ProductCategory
ON  ProductCategory.ProductCategoryID  =  ProductSubCategory.ProductCategoryID
INNER  JOIN  Production.UnitMeasure  SizeUnitMeasureCode
ON  Product.SizeUnitMeasureCode  =  SizeUnitMeasureCode.UnitMeasureCode
INNER  JOIN  Production.UnitMeasure  WeightUnitMeasureCode
ON  Product.WeightUnitMeasureCode  =  WeightUnitMeasureCode.UnitMeasureCode
INNER  JOIN  Production.ProductModel
ON  ProductModel.ProductModelID  =  Product.ProductModelID
LEFT  JOIN  Production.ProductModelIllustration
ON  ProductModel.ProductModelID  =  ProductModelIllustration.ProductModelID
LEFT  JOIN  Production.ProductModelProductDescriptionCulture
ON  ProductModelProductDescriptionCulture.ProductModelID  =  ProductModel.ProductModelID
LEFT  JOIN  Production.ProductDescription
ON  ProductDescription.ProductDescriptionID  =  ProductModelProductDescriptionCulture.ProductDescriptionID
LEFT  JOIN  Production.ProductReview
ON  ProductReview.ProductID  =  Product.ProductID
LEFT  JOIN  Purchasing.ProductVendor
ON  ProductVendor.ProductID  =  Product.ProductID
LEFT  JOIN  Production.UnitMeasure  CostMeasure
ON  ProductVendor.UnitMeasureCode  =  CostMeasure.UnitMeasureCode
ORDER  BY  Product.ProductID  DESC;
```
Se essa query fosse uma bush tree teria:
(2n-2)! / (n-1)! = (2*12-1)! / (12-1)! = 28,158,588,057,600 possíveis planos de execução.
Se fosse uma left-deep tree teria:
n! = 12! = 479,001,600 possíveis planos de execução.

Métodos para otimizar uma query com muitas tabelas:
* Mover a metadata ou colocar essas tabelas em uma outra query que põe esses dados em uma tabela temporária que pode ser usada em um JOIN depois. 
*  JOINs usados em uma única constante podem ser convertidos para parâmetro ou variável.
* Quebrar uma query grande em menores querys que podem ser ligadas depois
* Para querys muito usadas, considere o uso de views indexadas
* Remova tabelas desnecessárias, subquerys e joins
Para separar uma query grande em pequenas querys é preciso ter certeza que não vai ter mudanças de dados entre essas operações que podem alterar nossos resultados finais, para isso podemos usar um mix de níveis de isolação, transações, e bloqueios para garantir a integridade dos dados.

Exemplo de otimizações feitas na query la de cima:
```sql
SELECT  TOP  25
Product.ProductID,
Product.Name  AS  ProductName,
Product.ProductNumber,
ProductCategory.Name  AS  ProductCategory,
ProductSubCategory.Name  AS  ProductSubCategory,
Product.ProductModelID
INTO  #Product
FROM  Production.Product
INNER  JOIN  Production.ProductSubCategory
ON  ProductSubCategory.ProductSubcategoryID  =  Product.ProductSubcategoryID
INNER  JOIN  Production.ProductCategory
ON  ProductCategory.ProductCategoryID  =  ProductSubCategory.ProductCategoryID
ORDER  BY  Product.ModifiedDate  DESC;
SELECT
Product.ProductID,
Product.ProductName,
Product.ProductNumber,
CostMeasure.UnitMeasureCode,
CostMeasure.Name  AS  CostMeasureName,
ProductVendor.AverageLeadTime,
ProductVendor.StandardPrice,
ProductReview.ReviewerName,
ProductReview.Rating,
Product.ProductCategory,
Product.ProductSubCategory
FROM  #Product  Product
INNER  JOIN  Production.ProductModel
ON  ProductModel.ProductModelID  =  Product.ProductModelID
LEFT  JOIN  Production.ProductReview
ON  ProductReview.ProductID  =  Product.ProductID
LEFT  JOIN  Purchasing.ProductVendor
ON  ProductVendor.ProductID  =  Product.ProductID
LEFT  JOIN  Production.UnitMeasure  CostMeasure
ON  ProductVendor.UnitMeasureCode  =  CostMeasure.UnitMeasureCode;
DROP  TABLE  #Product;
```
Esse é apenas um exemplo de otimização, além disso podemos ver tabelas, colunas, variáveis ou qualquer outra coisa que não estão sendo usadas e retira-las da query.

## Query Hints
Uma query hint é um comando direto pro otimizador SQL.
Existem diversos tipos de hints no SQL Server, que afetam níveis de isolação, tipos de join, bloqueio de tabela, e outros. 
Perigos ao usar as hints:
*  Futuras mudanças ao schema podem fazer com que uma hint se torne inútil ou até mesmo perigosa, sendo necessário altera-la.
* Hints podem obscurecer problemas maiores, como índices em falta, requisições de dados excessivamente largas ou regras de negócio quebradas. Nesse caso é preferível resolver a raiz do problema.
* Hints podem resultar em comportamentos estranhos como por exemplo dados sujos do NOLOCK.
* Usar uma hint pra lidar com um problema na ponta de um processo pode até otimiza-lo, mas quanto ao resto do processo, não há como garantir

Alguns exemplos de query hint:
* **NOLOCK:** Com essa hint, no caso do SQL achar um dado que está bloqueado, o SQL usará dados antigos, também conhecido como dado sujo.
* **RECOMPILE:** Adicionar isso ao fim da query, vai fazer com que um novo plano de execução seja gerado toda vez que a query for executada.
* **MERGE/HASH/LOOP:** Isso vai especificar um tipo específico de operação para o Join, isso é super arriscado visto que o tipo de join ideal muda a medida que as tabelas mudam.
* **OPTIMIZE FOR:** Pode especificar um valor pra otimizar a query.


# Comandos para ver estatísticas
* **SET STATISTICS TIME ON**  
  Mostra o tempo em milissegundos necessário para analisar, compilar e executar cada instrução.
* **SET STATISTICS OI ON**  
  1. **Tabela:** nome da tabela envolvida na consulta;
  2. **Número de verificações:** número de buscas iniciadas para recuperar todos os valores para saída final;
  3. **Leituras lógicas:** número de páginas lidas do cache de dados do SQL Server;
  4. **Leituras físicas:** número de páginas lidas no disco do servidor;
  5. **Leituras read-ahead:** número de páginas colocadas no cache para a consulta;
  6. **Leituras lógicas lob:** número de colunas com valor grande: VARCHAR(MAX), VARCHAR(MAX) e VARBINARY(MAX) lidas do cache;
  7. **Leituras físicas lob:** número de colunas com valor grande: VARCHAR(MAX), VARCHAR(MAX) e VARBINARY(MAX) lidas do disco do servidor;
  8. **Leituras read-ahead lob:** número de colunas com valor grande: VARCHAR(MAX), VARCHAR(MAX) e VARBINARY(MAX) adicionadas no cache de dados.

###### Fonte
https://www.devmedia.com.br/otimizacao-de-consultas-sql/33485  
https://www.devmedia.com.br/10-tecnicas-de-otimizacao-de-consultas-sql/39499 -> Só os comandos pra ver estatísticas, o resto do conteúdo desse site é pago.  
https://www.sqlshack.com/query-optimization-techniques-in-sql-server-tips-and-tricks/  

