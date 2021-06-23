import sqlite3 as sl
import time

class SisPres:
    def __init__(self, connectionString):
        self.conn = sl.connect(connectionString)
        self.conn.execute("""
            CREATE TABLE PresFunc
            (
                codFunc INTEGER PRIMARY KEY AUTOINCREMENT,
                nome VARCHAR(200) NOT NULL,
                PIS VARCHAR(30) NOT NULL,
                presencasPosiveis INTEGER NOT NULL,
                presencas INTEGER,
                faltas INTEGER
            )
        """)
    def regisPres(self, nome, PIS, codFunc):
        self.conn.execute("""
            UPDATE PresFunc
               SET presencas = presencas+1
             WHERE codFunc = %s
        """%(codFunc))
        print("LOG: Funcionário: %s, PIS: %s, com presença"%(nome, PIS))
    def regisUsua(self, nome, PIS, codFunc):
        self.conn.execute("""
            INSERT INTO PresFunc
                 VALUES(%s, %s, %s, 0, 0, 0)
        """%(codFunc, nome, PIS))

class interSensorBio():
    def __init__(self, connectionString):
        self.sisPres = SisPres(connectionString)
    def chamarRegisPress(self, nome, PIS, codFunc):
        self.sisPres.regisPres(nome, PIS, codFunc)

class interPlatOnline():
    def __init__(self, connectionString):
        self.sisPres = SisPres(connectionString)
        self.minDecorridos = 0
    def contarTempo(self, nome, PIS, codFunc):
        tempoInicial = time.clock()
        tempo = time.clock()
        while(tempo < 60):
            tempo = time.clock() - tempoInicial
        self.chamarRegisPress(nome, PIS, codFunc)
    def chamarRegisPress(self, nome, PIS, codFunc):
        self.sisPres.regisPres(nome, PIS, codFunc)

sisPres = SisPres("BancoTeste.db")
sisPres.regisUsua("Fernando", "192012910", 1)

interBio = interSensorBio("BancoTeste.db")
interBio.chamarRegisPress("Fernando", "192012910", 1)

interPlat = interPlatOnline("BancoTeste.db")
interPlat.contarTempo("Fernando", "192012910", 1)

