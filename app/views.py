from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    return render(request, 'home.html')


# Formulário de cadastro 
def create(request):
    return render(request, 'create.html')

# Inserção dos dados dos usuários no banco
def store(request):
    data = {}
    if(request.POST['password']!= request.POST['password-conf']):
        data['msg'] = 'Senha e confirmação de senha diferentes !'
        data['class'] = 'alert-danger'
    else:
        user = User.objects.create_user(request.POST['name'],request.POST['email'],request.POST['password'], )
        user.save()
        data['msg'] = 'Usuário cadastrado com sucesso !'
        data['class'] = 'alert-success'
    return render(request, 'create.html',data)
