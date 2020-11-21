from django.shortcuts import render,redirect
from django.contrib import messages

# Create your views here.

def home(request):
    result = 0
    if request.method == 'POST':

        num1 = int(request.POST['num1'])
        operator = request.POST['operator']
        num2 = int(request.POST['num2'])

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '/':
            result = num1/num2
        elif operator == '*':
            result = num1 * num2
        else:
            messages.error(request,'invalid operator')

    context = {'result':result}

    return render(request,'calculator/home.html',context)

def results(request):
    pass
    # result = num1 = num2
    # context = {'result':result}
    return render(request,'calculator/results.html')