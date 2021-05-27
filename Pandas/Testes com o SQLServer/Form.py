#insert into TINF_INFTAB(TABI_NOM, TABI_DESPRI, TABI_DESSEC, TABI_OBS) values ('teste','teste','teste','teste') 
#insert into TINF_INFTAB(TABI_NOM, TABI_DESPRI, TABI_DESSEC, TABI_OBS) values (['teste','teste','teste','teste'], ['teste','teste','teste','teste'])
from ast import literal_eval
import re

sql = "insert into TINF_INFTAB(TABI_NOM, TABI_DESPRI, TABI_DESSEC, TABI_OBS) values (['teste','teste','teste','teste'], ['teste','teste','teste','teste'])"
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

def formInsert(sql):
    valuesIndex = re.search('values \(', sql, flags=re.IGNORECASE)
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
        sql = sql[0:valuesIndex.start()]+_valuesTuples
    return sql    

sql = formInsert(sql)
print(sql)