from datetime import datetime

class Medicao():
    def __init__(self, id, matparticulado, ozonio, mono_carbono, oxi_nitroso, data ):
        self.__id = id 
        self.__matparticulado = matparticulado
        self.__ozonio = ozonio
        self.__mono_carbono = mono_carbono
        self.__oxi_nitroso = oxi_nitroso
        self.__data = data
      
    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_matparticulado(self):
        return self.__matparticulado

    def set_matparticulado(self, matparticulado):
        self.__matparticulado = matparticulado
    
    def get_ozonio(self):
        return self.__ozonio

    def set_ozonio(self, ozonio):
        self.__ozonio = ozonio
    
    def get_mono_carbono(self):
        return self.__mono_carbono

    def set_mono_carbono(self, mono_carbono):
        self.__mono_carbono = mono_carbono

    def get_oxi_nitroso(self):
        return self.__oxi_nitroso

    def set_oxi_nitroso(self, oxi_nitroso):
        self.__oxi_nitroso = oxi_nitroso

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    def toDict(self) -> dict:
        return {
            "id": self.__id,
            "ozonio": self.__ozonio,
            "matparticulado": self.__matparticulado,
            "mono_carbono": self.__mono_carbono,
            "oxi_nitroso": self.__oxi_nitroso,
            "data": self.__data
        }