from django.http import HttpRequest,request
from django.shortcuts import render


def home(request):
	return render(request,'home.html')

def add(request):
	number1 = int(request.GET["num1"])
	number2 = int(request.GET["num2"])

	addition = number1 + number2

	return render(request, 'add.html',{'addition': addition})
