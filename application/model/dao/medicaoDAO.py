from datetime import datetime
from application.model.entity.medicao import medicao
from datetime import datetime


class medicaoDAO():
    def __init__(self, medicao):
        self.__medicao = medicao
    
    def listarMedicaoes(self):
        return self.medicoes


medicao1 = medicao(1, 1, 1, 1, 1, datetime.now)
medicao2 = medicao(1, 2, 2, 2, 2, "15/06/2021 12:00")
medicao3 = medicao(2, 4, 5, 3, 2, datetime.now())


medicao_list = medicaoDAO(medicao1, medicao1, medicao1)




