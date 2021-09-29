## Execução

Utilize os comando as seguir para executar o programa do seu terminal:

**obs: ** comandos de exemplos, mas deve sempre importar a a classe para instanciar um objeto

from paciente import Paciente <br>
from medico import Medico <br>
from medicamento import Medicamento<br>
from prontuario import Prontuario <br>
paciente1 = Paciente('Paciente1')<br>
prontuario1 = Prontuario()<br>
paciente2 = Paciente('Paciente2')<br>
prontuario2 = Prontuario()<br>
medicamento1 = Medicamento('Omeprazol')<br>
medicamento2 = Medicamento('Tylenol')<br>
medicamento3 = Medicamento('Dipirona')<br>
medico1 = Medico('Medico1')<br>
medico2 = Medico('Medico2')<br>
paciente1.definir_prontuario(prontuario1)<br>
paciente2.definir_prontuario(prontuario2)<br>
paciente1.prontuario.insere_procedimento(medicamento1, '68mcg', medico1, "15-06-2020", "10:10")<br>
paciente1.prontuario.insere_procedimento(medicamento2, '100mg', medico1, "15-06-2020", "11:40")<br>
paciente2.prontuario.insere_procedimento(medicamento2, '18mcg', medico2, "14-06-2020", "12:00")<br>
paciente2.prontuario.insere_procedimento(medicamento3, '20mg', medico2, "15-06-2020", "12:05")<br>

paciente2.prontuario.exibe_prontuario()   //exibe prontuarios do paciente2(objeto)