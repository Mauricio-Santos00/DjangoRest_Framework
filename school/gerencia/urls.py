from django.conf.urls import url
from gerencia.Views import professorView,alunoView,atividadeAlunoView,atividadeView,disciplinaAlunoView,disciplinaView,planoAulaView,frequenciaAlunoView,frequenciaView, querysView

urlpatterns = [
    url(r'^professor$',professorView.ProfessorApi),
    url(r'^professor/([0-9]+)$',professorView.ProfessorApi),
    
    url(r'^aluno$',alunoView.AlunoApi),
    url(r'^aluno/([0-9]+)$',alunoView.AlunoApi),
    
    url(r'^disciplina$',disciplinaView.DisciplinaApi),
    url(r'^disciplina/([0-9]+)$',disciplinaView.DisciplinaApi),
    
    url(r'^disciplinaAluno$',disciplinaAlunoView.DisciplinaAlunoApi),
    url(r'^disciplinaAluno/([0-9]+)$',disciplinaAlunoView.DisciplinaAlunoApi),
    
    url(r'^atividade$',atividadeView.AtividadeApi),
    url(r'^atividade/([0-9]+)$',atividadeView.AtividadeApi),
    
    url(r'^atividadeAluno$',atividadeAlunoView.AtividadeAlunoApi),
    url(r'^atividadeAluno/([0-9]+)$',atividadeAlunoView.AtividadeAlunoApi),
    
    url(r'^planoAula$',planoAulaView.PlanoAulaApi),
    url(r'^planoAula/([0-9]+)$',planoAulaView.PlanoAulaApi),
    
    url(r'^frequencia$',frequenciaView.FrequenciaApi),
    url(r'^frequencia/([0-9]+)$',frequenciaView.FrequenciaApi),
    
    url(r'^frequenciaAluno$',frequenciaAlunoView.FrequenciaAlunoApi),
    url(r'^frequenciaAluno/([0-9]+)$',frequenciaAlunoView.FrequenciaAlunoApi),
    
    url(r'^professor/([0-9]+)/disciplinas$',querysView.ProfessorDisciplinaApi),
    
     url(r'^disciplinas/([0-9]+)/alunos$',querysView.AlunoDisciplinaApi),
]
