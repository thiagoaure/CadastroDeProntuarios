from pessoa import Pessoa
from prontuario import Prontuario

class Paciente(Pessoa):
    __total_pacientes = 0
    prontuario = Prontuario()

    def __init__(self, __nome):
        Paciente.__total_pacientes += 1
    
    def __del__(self):
        Paciente.__total_pacientes -=1
        print("Paciente apagado")
    
    def definir_id(self, id):
        tam_id = len(id)
        if (tam_id > 5):
            print("ERRO! ID COM MAIS DE 5 CARACTERES")
    
    def pacientes_ativos():
        return Paciente.__total_pacientes;

    def definir_prontuario(self, pront):
        self.prontuario = pront;