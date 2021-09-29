from pessoa import Pessoa

class Medico(Pessoa):

    def __init__(self, nome):
        self.__nome = nome

    def definir_id(self, id):
        tam_id = str(id);
        if (len(tam_id)>3):
            print("ERRRO! ID MAIOR QUE 3 CARACTERES")

    def nome_medico(self):
        return self.__nome