from django.shortcuts import render
from django.http import HttpResponse 
from app.models import Create
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate

# Create your views here.

def home(request):

    if request.method == 'POST':
        user_name = request.POST.get('name')
        password = request.POST.get('password')
        print("Nome:", user_name)
        print("Senha:", password)
        
        # Buscar usuário pelo nome fornecido
        try:
            user = Create.objects.get(user_name=user_name)
            print(user.password)
        except Create.DoesNotExist:
            # Se não houver usuário com esse nome
            print("Usuário não encontrado.")
            return render(request, 'app/home.html')

        # Verificar se a senha fornecida corresponde à senha armazenada
        if password == user.password:
            # Se a senha está correta
            print("Senha correta. Usuário autenticado com sucesso.")
        else:
            # Se a senha está incorreta
            print("Senha incorreta. Falha na autenticação.")
        
        return render(request, 'app/home.html')
    else:
        return render(request, 'app/home.html')