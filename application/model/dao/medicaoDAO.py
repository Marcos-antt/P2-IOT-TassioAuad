from datetime import datetime
from application.model.entity.medicao import Medicao
from datetime import datetime


class MedicaoDAO():
    def __init__(self, medicao):
        self.__medicao = medicao
    
    def listarMedicoes(self):
        return self.__medicao

    def adicionarMedicoes(self, medicao):
        self.__medicao.append(medicao)



medicao1 = Medicao(1, 1, 1, 1, 1,"11/06/2021")
medicao2 = Medicao(1, 2, 2, 2, 2, "15/06/2021")
medicao3 = Medicao(2, 4, 5, 3, 2,"12/06/2021")


medicao_list = MedicaoDAO([medicao1, medicao2, medicao3]) 




