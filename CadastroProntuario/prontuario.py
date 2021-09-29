from medico import Medico
from medicamento import Medicamento
from datetime import datetime

class Prontuario:
    
    def __init__(self):
        self.__lista_procedimentos = []
    
    def insere_procedimento(self, medicamento , posologia, medico, data, hora):
       
        data_obj = datetime.strptime(data, '%d-%m-%Y').date()
        hora_obj = datetime.strptime(hora, '%H:%M').time()
        self.__paciente  = (medicamento.nome_medicamento(), posologia, medico.nome_medico(), str(data_obj), str(hora_obj))
        print(medico.nome_medico(), '  ', medicamento.nome_medicamento(), '   ', posologia, '   ',  data_obj,'   ', hora_obj )
        self.__lista_procedimentos.append(self.__paciente)

    def exibe_prontuario(self):
        for i in self.__lista_procedimentos:
            print(i)