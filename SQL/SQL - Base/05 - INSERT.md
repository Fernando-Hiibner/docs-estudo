### <span style = "color:#6a9955">INSERT INTO  </span>
Usado para inserir valores nas linhas das tabelas, correspondentes as suas colunas, cada nova inserção é uma nova linha.
Multiplos conjuntos de values indicam inserção em novas linhas.
```sql
INSERT INTO <nome_da_tabela> (coluna1, coluna2,...) 
VALUES (value1, value2,...), (value3, value4,...);
```
### <span style = "color:#6a9955">Exemplo:  </span>
```sql
INSERT INTO persons (name, birth, phone) 
VALUES ('Baozi', '1970-01-01', '(14)99000-0001'), ('Fernando', '2002-09-03', '(14)99000-0002');
```
