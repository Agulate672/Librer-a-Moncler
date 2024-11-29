from django.http import HttpResponse
from django.shortcuts import render, get_list_or_404

def index(request):
        return render (request, 'index.html')
