#insert into TINF_INFTAB(TABI_NOM, TABI_DESPRI, TABI_DESSEC, TABI_OBS) values ('teste','teste','teste','teste') 
#insert into TINF_INFTAB(TABI_NOM, TABI_DESPRI, TABI_DESSEC, TABI_OBS) values (['teste','teste','teste','teste'], ['teste','teste','teste','teste'])
from ast import literal_eval
import re

sql = "INSERT INTO NomeDaTabela (Matematica, Matematica2, Fracoes, Setas, Quadrados, Triangulos, Circulos, Porcoes) VALUES (['Ω', 'π', '√', '≠'], ['⁰', '¹', '²', '³'], ['⅟', '¼', '½', '¾'], ['←', '→', '↑', '↓'], ['▢', '▥', '■', '▣'], ['▲', '◀', '▶', '▼'], ['◌', '●', '○', '◍'], ['◖', '◗', '◓', '◐'])"
'''valuesIndex = re.search('values \(', sql, flags=re.IGNORECASE)
valuesTuples = literal_eval("("+sql[valuesIndex.end()::])
if type(valuesTuples[0]) == list:
    _valuesTuples = ""
    _valuesTuplesSize = len(valuesTuples)-1
    _index = 0
    for _valuesList in valuesTuples:
        _tuple = tuple(_valuesList)
        if(_index != _valuesTuplesSize):
            _valuesTuples += str(_tuple)+", "
        else:
            _valuesTuples += str(_tuple)
        _index += 1;
    _valuesTuples = "values "+_valuesTuples
    sql = sql[0:valuesIndex.start()]+_valuesTuples'''

#Talvez fazer essa parada de:
#if type(valuesTuples[0]) == list:
#Antes de chamar a função
#INSERT INTO NomeDaTabela (Matematica, Matematica2, Fracoes, Setas, Quadrados, Triangulos, Circulos, Porcoes) VALUES (['Ω', 'π', '√', '≠'], ['⁰', '¹', '²', '³'], ['⅟', '¼', '½', '¾'], ['←', '→', '↑', '↓'], ['▢', '▥', '■', '▣'], ['▲', '◀', '▶', '▼'], ['◌', '●', '○', '◍'], ['◖', '◗', '◓', '◐'])
def formInsert(sql):
    valuesIndex = re.search('values \(', sql, flags=re.IGNORECASE)
    valuesTuple = literal_eval("("+sql[valuesIndex.end()::])
    if type(valuesTuple[0]) == list:
        _newValuesTuple = list()
        for i in range(len(valuesTuple[0])):
            _list = list()
            for j in range(len(valuesTuple)):
                _list.append(valuesTuple[j][i])
            _newValuesTuple.append(_list)
        _valuesTuple = ""
        _valuesTupleSize = len(_newValuesTuple)-1
        _index = 0
        for _valuesList in _newValuesTuple:
            _tuple = tuple(_valuesList)
            if(_index != _valuesTupleSize):
                _valuesTuple += str(_tuple)+", "
            else:
                _valuesTuple += str(_tuple)
            _index += 1
        _valuesTuple = "values "+_valuesTuple
        sql = sql[0:valuesIndex.start()]+_valuesTuple
    return sql    

sql = formInsert(sql)
print(sql)