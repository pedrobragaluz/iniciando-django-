from django.http import HttpResponse

def teste_view(request):
    return HttpResponse("Está é a rota de teste!")


def index_view(request):
    return HttpResponse("<h1>JEFFERSON CPF POR FAVOR!!!</h1>")