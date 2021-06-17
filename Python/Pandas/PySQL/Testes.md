```py
{
	"tab": '1c', 
	"bg": 'SystemWindow', 
	"fg": 'black',
	"selectbackground": '#dddddd', 
	"selectforeground": 'black', 
	"insertbackground": 'black'
}
#insert into TINF_INFTAB(TABI_NOM, TABI_DESPRI, TABI_DESSEC, TABI_OBS) values ('teste','teste','teste','teste')
#insert into TINF_INFTAB(TABI_NOM, TABI_DESPRI, TABI_DESSEC, TABI_OBS) values (['teste','teste','teste','teste'], ['teste','teste','teste','teste'])
#INSERT INTO Baozi (Nome, Tamaho, Fisico, Porte) values ('Baozi', 'Grande', 'Obeso', 'Gigante'), ('Curry', 'Pequeno', 'Magro', 'Baixo')

{
        "Matematica":   ["Ω", "π", "√", "≠"],
        "Matematica2": ["⁰", "¹", "²", "³"],
        "Fracoes":      ["⅟", "¼", "½", "¾"],
        "Setas":        ["←", "→", "↑", "↓"],
        "Quadrados":    ["▢", "▥", "■", "▣"],
        "Triangulos":   ["▲", "◀", "▶", "▼"],
        "Circulos":     ["◌", "●", "○", "◍"],
        "Porcoes":      ["◖", "◗", "◓", "◐"]
}

{
        "Matematica":   {"Ω", "π", "√", "≠"},
        "Matematica2": {"⁰", "¹", "²", "³"},
        "Fracoes":      {"⅟", "¼", "½", "¾"},
        "Setas":        {"←", "→", "↑", "↓"},
        "Quadrados":    {"▢", "▥", "■", "▣"},
        "Triangulos":   {"▲", "◀", "▶", "▼"},
        "Circulos":     {"◌", "●", "○", "◍"},
        "Porcoes":      {"◖", "◗", "◓", "◐"}
}

{
        "Matematica":   {0: "Ω", 1: "π", 2: "√", 3: "≠"},
        "Matematica2":  {0: "⁰", 1: "¹", 2: "²", 3: "³"},
        "Fracoes":      {0: "⅟", 1: "¼", 2: "½", 3: "¾"},
        "Setas":        {0: "←", 1: "→", 2: "↑", 3: "↓"},
        "Quadrados":    {0: "▢", 1: "▥", 2: "■", 3: "▣"},
        "Triangulos":   {0: "▲", 1: "◀", 2: "▶", 3: "▼"},
        "Circulos":     {0: "◌", 1: "●", 2: "○", 3: "◍"},
        "Porcoes":      {0: "◖", 1: "◗", 2: "◓", 3: "◐"}
}
CREATE TABLE "NomeDaTabela" (
  "index" INTEGER PRIMARY KEY IDENTITY(1,1),
  "Matematica" VARCHAR(2) collate utf8_general_ci,
  "Matematica2" VARCHAR(2) collate utf8_general_ci,
  "Fracoes" VARCHAR(2) collate utf8_general_ci,
  "Setas" VARCHAR(2) collate utf8_general_ci,
  "Quadrados" VARCHAR(2) collate utf8_general_ci,
  "Triangulos" VARCHAR(2) collate utf8_general_ci,
  "Circulos" VARCHAR(2) collate utf8_general_ci,
  "Porcoes" VARCHAR(2) collate utf8_general_ci
)
{
        "Matematica":   ["Ω", "π", "√", "≠"],
        "Matematica2":  {"⁰", "¹", "²", "³"},
        "Fracoes":      {0: "⅟", 1: "¼", 2: "½", 3: "¾"},
        "Setas":        ["←", "→", "↑", "↓"],
        "Quadrados":    {0: "▢", 1: "▥", 2: "■", 3: "▣"},
        "Triangulos":   {0: "▲", 1: "◀", 2: "▶", 3: "▼"},
        "Circulos":     {"◌", "●", "○", "◍"},
        "Porcoes":      ["◖", "◗", "◓", "◐"]
}

```
```sql
select *
from TINF_INFTAB as t1
join TINF_INFSIG as t2
on t1.TABI_COD = t2.SIGI_COD
order by t1.TABI_COD;

create table Baozi(
	id INTEGER PRIMARY KEY IDENTITY(1,1),
	Nome VARCHAR(50),
	Tamanho VARCHAR(50),
	Fisico VARCHAR(50),
	Porte VARCHAR(50)
);
INSERT INTO Baozi (Nome, Tamanho, Fisico, Porte) values ('Baozi', 'Grande', 'Obeso', 'Gigante'), ('Curry', 'Pequeno', 'Magro', 'Baixo');
select * from Baozi;
```
```py
{'TABI_COD': {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8, 8: 9, 9: 10, 10: 11, 11: 12, 12: 13, 13: 14, 14: 15, 15: 16, 16: 17, 17: 18, 18: 19, 19: 20, 20: 21, 21: 22, 22: 23, 
23: 24, 24: 25, 25: 26, 26: 27, 27: 28, 28: 29, 29: 30, 30: 31, 31: 32, 32: 33, 33: 34, 34: 35, 35: 36, 36: 37, 37: 38, 38: 39, 39: 40, 40: 41, 41: 42, 42: 43, 43: 44, 44: 45, 45: 46, 46: 47, 47: 48, 48: 49, 49: 50, 50: 51, 51: 52, 52: 53, 53: 54, 54: 55, 55: 56, 56: 57, 57: 58, 58: 59, 59: 60, 60: 61, 61: 62, 62: 63, 63: 64, 64: 65, 65: 66, 66: 67, 67: 68, 68: 69, 69: 70, 70: 71, 71: 72, 72: 73, 73: 74, 74: 75, 75: 76, 76: 77, 77: 78, 78: 79, 79: 80, 80: 81, 81: 82, 82: 83, 83: 84, 84: 85}, 'TABI_NOM': {0: 'TINF_INFTAB', 1: 'TINF_INFSIG', 2: 'TACE_GRPUSU', 3: 'TACE_USUSIS', 4: 'TCOM_ANACOM', 5: 'TCOM_CATFIS', 6: 'TCOM_CFCEMP', 7: 'TCOM_CFCGER', 8: 'TCOM_CFOFIS', 9: 'TCOM_CFOGRU', 10: 'TCOM_CFOTIP', 11: 'TCOM_CLACLI', 12: 'TCOM_CLAPRO', 13: 'TCOM_CLAREP', 14: 'TCOM_COMERC', 15: 'TCOM_COMEST', 16: 'TCOM_COMGRU', 17: 'TCOM_COMUNI', 18: 'TCOM_CONPAG', 19: 'TCOM_CPGUNI', 20: 'TCOM_CPLPDS', 21: 'TCOM_EQUVEN', 22: 'TCOM_FAMPRO', 23: 'TCOM_FATCOM', 24: 'TCOM_FISCOM', 25: 'TCOM_FORPAG', 26: 'TCOM_FPGUNI', 27: 'TCOM_GRUCLI', 28: 'TCOM_GRUPRO', 29: 'TCOM_IMGPRO', 30: 
'TCOM_LISPRE', 31: 'TCOM_LISUNI', 32: 'TCOM_LOCENT', 33: 'TCOM_LOGPDS', 34: 'TCOM_LOJGRU', 35: 'TCOM_LOTPDS', 36: 'TCOM_MARPRO', 37: 'TCOM_PEDSAI', 38: 'TCOM_PRAPAG', 39: 'TCOM_PROSER', 40: 'TCOM_PROUNI', 41: 'TCOM_RAMATI', 42: 'TCOM_REGVEN', 43: 'TCOM_REPUNI', 44: 'TCOM_REPVEN', 45: 'TCOM_SERENT', 46: 'TCOM_SETVEN', 47: 'TCOM_STAPDS', 48: 'TCOM_SUBPRO', 49: 'TCOM_SUBREG', 50: 'TCOM_TIPANA', 51: 'TCOM_TIPPAG', 52: 'TCOM_UNIPRO', 53: 'TEST_ALMOXA', 54: 'TEST_MOVPRO', 55: 'TEST_SALMES', 56: 'TEST_SALPRO', 57: 'TEST_TIPMOV', 58: 'TFIN_ANODOC', 59: 'TFIN_BANCOS', 60: 'TFIN_DOCPAR', 61: 'TFIN_FORPGR', 62: 'TFIN_LOTPAG', 63: 'TFIN_RECPAG', 64: 'TFIN_PLACTA', 65: 'TFIN_PLAGRU', 66: 'TFIN_PLALAN', 67: 'TFIN_PORTIT', 68: 'TFIN_TIPDOC', 69: 'TGEN_ANOCLA', 70: 'TGEN_COTMON', 71: 'TGEN_EMPRES', 72: 'TGEN_ENTANO', 73: 'TGEN_ENTBAS', 74: 'TGEN_ENTCON', 75: 'TGEN_ENTEND', 76: 'TGEN_ENTFIS', 77: 'TGEN_ENTIMG', 78: 'TGEN_ESTEMP', 79: 'TGEN_ESTFED', 80: 'TGEN_FERIAD', 81: 'TGEN_GRUEMP', 82: 'TGEN_IMPNOT', 83: 'TGEN_IMPRES', 84: 'TGEN_ITENOT'}, 'TABI_DESPRI': {0: 'Tabela Informação', 1: 'Tabela Informação', 2: 'Tabela Acesso', 3: 'Tabela Acesso', 4: 'Tabela Comercial', 5: 'Tabela Comercial', 6: 'Tabela Comercial', 7: 'Tabela Comercial', 8: 'Tabela Comercial', 9: 'Tabela Comercial', 10: 'Tabela Comercial ', 11: 'Tabela Comercial', 12: 'Tabela Comercial', 13: 'Tabela Comercial', 14: 'Tabela Comercial', 15: 'Tabela Comercial', 16: 'Tabela Comercial', 17: 'Tabela Comercial', 18: 'Tabela Comercial', 19: 'Tabela Comercial', 20: 'Tabela Comercial', 21: 'Tabela Comercial', 22: 'Tabela Comercial', 23: 'Tabela Comercial', 24: 'Tabela Comercial', 25: 'Tabela Comercial', 26: 'Tabela Comercial', 27: 'Tabela Comercial', 28: 'Tabela Comercial', 29: 'Tabela Comercial', 30: 'Tabela Comercial', 31: 'Tabela Comercial', 32: 'Tabela Comercial', 33: 'Tabela Comercial', 34: 'Tabela Comercial', 35: 'Tabela Comercial', 36: 'Tabela Comercial', 37: 'Tabela Comercial', 38: 'Tabela Comercial', 39: 'Tabela Comercial', 40: 'Tabela Comercial', 41: 'Tabela Comercial', 42: 'Tabela Comercial', 43: 'Tabela Comercial', 44: 'Tabela Comercial', 45: 'Tabela Comercial', 46: 'Tabela Comercial', 47: 'Tabela Comercial', 48: 'Tabela Comercial', 49: 'Tabela Comercial', 50: 'Tabela Comercial', 51: 'Tabela Comercial', 52: 'Tabela Comercial', 53: 'Tabela Estoque', 54: 'Tabela Estoque', 55: 'Tabela Estoque', 56: 'Tabela Estoque', 57: 'Tabela Estoque', 58: 'Tabela Finanças', 59: 'Tabela Finanças', 60: 'Tabela Finanças', 61: 'Tabela Finanças', 62: 'Tabela Finanças', 63: 'Tabela Finanças', 64: 'Tabela Finanças', 65: 'Tabela Finanças', 66: 'Tabela Finanças', 67: 'Tabela Finanças', 68: 'Tabela Finanças', 69: 'Tabela Gerencial', 70: 'Tabela Gerencial', 71: 'Tabela Gerencial', 72: 'Tabela Gerencial', 73: 'Tabela Gerencial', 74: 'Tabela Gerencial', 75: 'Tabela Gerencial', 76: 'Tabela Gerencial', 77: 'Tabela Gerencial', 78: 'Tabela Gerencial', 79: 'Tabela Gerencial', 80: 'Tabela Gerencial', 81: 'Tabela Gerencial', 82: 'Tabela Gerencial', 83: 'Tabela Gerencial', 84: 'Tabela Gerencial'}, 'TABI_DESSEC': {0: 'Informação Tabelas', 1: 'Informação Siglas', 2: 'Grupo Usuários', 3: 'Usuários Sistema', 4: '(ANA) Compras', 5: 'Categoria Fiscal', 6: '(CFC) Empresa', 7: '(CFC) Gerencia', 8: 'CFOP Fiscal', 9: 'CFOP Grupo', 10: 'CFOP Tipo', 11: 'Classificação Cliente', 12: 'Classificação Produto', 13: 'Classificação (REP)', 14: 'Comercialização', 15: 'Compras (EST)', 16: 'Compras Grupo', 17: 'Compras Unidade', 18: '(CONPAG)', 19: '(CPG) Unidade', 20: 'Complemento Pedido', 21: 'Equipe Vendas', 22: 'Família Produto', 23: 'Faturamento Compra', 24: '(FIS) Compras', 25: 'Forma Pagamento', 26: '(FPG) Unidade', 27: 'Grupo Cliente?', 28: 'Grupo Produto', 29: 'Imagem Produto', 30: 'Lista Preco', 31: 'Lista Unidade', 32: '(LOC) Entrega', 33: 'Log Pedidos', 34: '(LOJ) Grupo', 35: 'Lote Pedido', 36: 'Marca Produto', 37: 'Pedido Saída', 38: '(PRA) Pagamento', 39: 'Produto (SER)', 40: 'Produto Unidade', 41: 'Ramo Atividade', 42: 'Região Venda', 43: 'Representante Unidade', 44: 'Representante Venda', 45: 'Serviço Entrega', 46: 'Setor Venda', 47: 'Status Pedido', 48: 'Produto Subgrupo', 49: 'Sub Região', 50: 'Tipo (ANA)', 51: 'Tipo Pagamento', 52: 'Unidade Produto', 53: 'Almoxarifado', 54: 'Movimentação Produto', 55: 'Saldo Mês', 56: 'Saldo Produto', 57: 'Tipo Movimentação', 58: '(ANO) Documento', 59: 'Bancos', 60: 'Documento (PAR)', 61: 'Forma Pagamento', 62: 'Lote Pagamento', 63: '(REC) Pagamento', 64: '(PLACTA)', 65: '(PLAGRU)', 66: '(PLALAN)', 67: '(PORTIT)', 68: 'Tipo Documento', 69: '(ANO) Classificacao', 70: '(COTMON)', 71: '(EMPRES)', 72: 'Entrega (ANO)', 73: 'Entrega Basico', 74: 'Entrega (CON)', 75: 'Entrega Endereco', 76: 'Entrega (Fiscal)?', 77: 'Entrega (Imagem)?', 78: '(EST) Empresa', 79: 'Estado Federal', 80: '(FERIAD)', 81: 'Grupo Empresa', 82: 'Imposto Nota', 83: 'Imposto (RES)', 84: 'Item Nota'}, 'TABI_OBS': {0: None, 1: None, 2: None, 3: None, 4: 'ANA - Provavelmente - Análise', 5: None, 6: 'CFC - Desconhecida', 7: 'CFC - Desconhecida', 8: 'CFOP - Código Fiscal de Operações e Prestações', 9: 'CFOP - Código Fiscal de Operações e Prestações', 10: 'CFOP - Código Fiscal de Operações e Prestações', 11: None, 12: None, 13: 'REP - Provavelmente - Repositório / Representante', 14: None, 15: 'EST - Provavelmente - Estado', 16: None, 17: None, 18: 'CONPAG - Desconhecido', 19: 'CPG - Desconhecido', 20: None, 21: None, 22: None, 23: None, 24: 'FIS - Provavelmente - Fiscal', 25: None, 26: 'FPG - Chave Estrangeira que referencia - TCOM_FORPAG', 27: 'Talvez, não é certeza', 28: None, 29: None, 30: None, 31: None, 32: 'LOC - Desconhecido', 33: None, 34: 'LOJ - Provavelmente - Loja', 35: None, 36: None, 37: None, 38: 'PRA - Talvez - Pra', 39: 'SER - Provavelmente - Serviço / Serie', 40: None, 41: None, 42: None, 43: None, 44: None, 45: None, 46: None, 47: None, 48: None, 49: None, 50: 'ANA - Provavelmente - Análise', 51: None, 52: 'Unidade - Peça, Kilo, Cartela, Centimetro...', 53: None, 54: None, 55: 'Saldo - No sentido de Estoque', 56: None, 57: None, 58: 'ANO - Desconhecido', 59: None, 60: 'PAR - Desconhecido', 61: None, 62: None, 63: 'REC - Provavelmente - Recebimento / Recibo', 64: 'PLACTA - Desconhecido', 65: 'PLAGRU - Desconhecido', 66: 'PLALAN - Desconhecido', 67: 'PORTIT - Desconhecido', 68: None, 69: 'ANO - Desconhecido', 70: 'COTMON - Desconhecido', 71: 'EMPRES - Provavelmente - Empresa', 72: 'ANO - Desconhecido', 73: None, 74: 'CON - Desconhecido', 75: None, 76: 'Talvez, não é certeza', 77: 'Talvez, não é certeza', 78: 'EST - Provavelmente - Estado / Estoque', 79: None, 80: 'FERIAD - Desconhecido', 81: None, 82: None, 83: 'RES - Desconhecido', 84: None}, 'SIGI_COD': {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8, 8: 9, 9: 10, 10: 11, 11: 12, 12: 13, 13: 14, 14: 15, 
15: 16, 16: 17, 17: 18, 18: 19, 19: 20, 20: 21, 21: 22, 22: 23, 23: 24, 24: 25, 25: 26, 26: 27, 27: 28, 28: 29, 29: 30, 30: 31, 31: 32, 32: 33, 33: 34, 34: 35, 35: 36, 36: 37, 37: 38, 38: 39, 39: 40, 40: 41, 41: 42, 42: 43, 43: 44, 44: 45, 45: 46, 46: 47, 47: 48, 48: 49, 49: 50, 50: 51, 51: 52, 52: 53, 53: 54, 54: 55, 55: 56, 56: 57, 57: 58, 58: 59, 59: 60, 60: 61, 61: 62, 62: 63, 63: 64, 64: 65, 65: 66, 66: 67, 67: 68, 68: 69, 69: 70, 70: 71, 71: 72, 72: 73, 73: 74, 74: 75, 75: 76, 76: 77, 77: 78, 78: 79, 79: 80, 80: 81, 81: 82, 82: 83, 83: 84, 84: 85}, 'SIGI_NOM': {0: 'INF', 1: 'SIG', 2: 'T / TAB', 3: 'ACE', 4: 'GRP / GRU', 5: 'USU', 6: 'SIS', 7: 'ANA', 8: 'COM', 9: 'CAT', 10: 'FIS', 11: 'EMP', 12: 'CFO', 13: 'GER', 14: 'TIP', 15: 'CLA', 16: 'CLI', 17: 'PRO', 18: 'REP', 19: 'COMERC', 20: 'EST', 21: 'UNI', 22: 'PAG', 23: 'CPL', 24: 'PDS / PED', 25: 'EQU', 26: 'VEN', 27: 'FAM', 28: 
'FAT', 29: 'FOR', 30: 'FPG', 31: 'IMG', 32: 'LIS', 33: 'PRE', 34: 'ENT', 35: 'LOG', 36: 'LOJ', 37: 'LOT', 38: 'MAR', 39: 'SAI', 40: 'RAM', 41: 'ATI', 42: 'REG', 43: 'SER', 44: 'SET', 45: 'STA', 46: 'SUB', 47: 'ALMOXA', 48: 'MOV', 49: 'SAL', 50: 'MES', 51: 'FIN', 52: 'ANO', 53: 'DOC', 54: 'BANCOS', 55: 'PAR', 56: 'REC', 57: 'PLA', 58: 'CTA', 59: 'LAN', 60: 
'POR', 61: 'TIT', 62: 'COT', 63: 'MON', 64: 'EMRPES', 65: 'BAS', 66: 'CON', 67: 'END', 68: 'FED', 69: 'FERIAD', 70: 'IMP', 71: 'NOT', 72: 'RES', 73: 'ITE', 74: 'LAY', 75: 'COL', 76: 'DAD', 77: 'LIN', 78: 'LAYOUT', 79: 'LYD', 80: 'MUN', 81: 'CID', 82: 'PAIS', 83: 'TRANSP', 84: 'NEG'}, 'SIGI_DES': {0: 'Informação', 1: 'Sigla', 2: 'Tabela', 3: 'Acesso', 4: 'Grupo', 5: 'Usuário', 6: 'Sistema', 7: 'Desconhecido', 8: 'Compras / Comercial', 9: 'Categoria', 10: 'Fiscal', 11: 'Empresa', 12: 'CFOP', 13: 'Gerência', 14: 'Tipo', 15: 'Classificação', 16: 'Cliente', 17: 'Produto', 18: 'Desconhecido', 19: 'Comercialização', 20: 'Estoque / Estado', 21: 'Unidade', 22: 'Pagamento', 23: 'Complemento', 24: 'Pedido', 25: 'Equipe', 26: 'Vendas', 27: 'Família', 28: 'Faturamento', 29: 'Forma', 30: 'Chave Estrangeira', 31: 'Imagem', 32: 'Lista', 33: 'Preço', 34: 'Entrega', 35: 'Log / Logradouro', 36: 'Desconhecido', 37: 'Lote', 38: 'Marca', 39: 'Saída', 40: 'Ramo', 41: 'Atividade', 42: 'Região', 43: 'Serviço / Serie / Serial', 44: 'Setor', 45: 'Status', 46: 'Sub / Subgrupo', 47: 'Almoxarifado', 48: 'Movimentação', 49: 'Saldo', 50: 'Mês / Mensal', 51: 'Desconhecido', 52: 'Desconhecido', 53: 'Documento', 54: 'Bancos', 55: 'Desconhecido', 56: 'Recebimento / Recibo', 57: 'Desconhecido', 58: 'Desconhecido', 59: 'Desconhecido', 60: 'Desconhecido', 61: 'Desconhecido', 62: 'Desconhecido', 63: 'Desconhecido', 64: 'Desconhecido', 65: 'Básico', 66: 'Desconhecido', 67: 'Endereço', 68: 'Federal', 69: 'Desconhecido', 70: 'Imposto', 71: 'Nota', 72: 'Desconhecido', 73: 'Item', 74: 'Desconhecido', 75: 'Desconhecido', 76: 'Desconhecido', 77: 'Desconhecido', 78: 'Layout', 79: 'Desconhecido', 80: 'Município', 81: 'Cidade', 82: 'País', 83: 'Transportadora', 84: 'Desconhecido'}, 'SIGI_OBS': {0: 'Se aplica as tabelas TINF', 1: 'Se aplica as tabelas TINF', 2: 'Também se aplica a TINF', 3: None, 4: None, 5: None, 6: None, 7: 'ANA - Provavelmente - Análise', 8: None, 9: None, 10: None, 11: None, 12: 'CFOP = Código Fiscal de Operações e Prestações', 13: None, 14: None, 15: None, 16: None, 17: None, 18: 'REP - Provavelmente - Repositório / Representante', 19: None, 20: None, 21: None, 22: None, 23: None, 24: None, 25: None, 26: None, 27: None, 28: None, 29: None, 30: 'Referencia TCOM_FORPAG', 31: None, 32: None, 33: None, 34: None, 35: None, 36: 'LOJ - Provavelmente - Loja', 37: None, 38: None, 39: None, 40: None, 41: None, 42: None, 43: None, 44: None, 45: None, 46: None, 47: None, 48: None, 49: None, 50: None, 51: 'FIN - Provavelmente - Finanças', 52: 'ANO - Desconhecido', 53: None, 54: None, 55: None, 56: None, 57: 'PLA - Desconhecido', 58: 'CTA - Desconhecido', 59: 'LAN - Desconhecido', 60: 'POR - Desconhecido', 61: 'TIT - Desconhecido', 62: 'COT - Desconhecido', 63: 'MON - Desconhecido', 64: 'EMPRES - Provavelmente - Empresa', 65: None, 66: 'CON - Desconhecido', 67: None, 68: None, 69: 'FERIAD - Desconhecido', 70: None, 71: None, 72: 'RES - Desconhecido', 73: None, 74: 'LAY - Desconhecido', 75: 'COL - Provavelmente - Coluna', 76: 'DAD - Provavelmente - Dados', 77: 'LIN - Provavelmente - Linha', 78: None, 79: 'LYD - Desconhecido', 80: None, 81: None, 82: None, 83: None, 84: 'NEG - Desconhecido'}}
```




    