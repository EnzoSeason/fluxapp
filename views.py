from django.shortcuts import render, redirect, reverse
from fluxapp.forms import Ex1Form, fileForm
from fluxapp.mathFunctions import ex1_calculPai, hospital_calculRho
import numpy as np
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request, 'fluxapp/index.html')



def ex1(request):
    pai = 0.0
    rho1 = 0.0
    rho2 = 0.0
    rho3 = 0.0
    if request.method == 'POST':
        form = Ex1Form(request.POST)
        if form.is_valid():
            lbd = form.cleaned_data['lbd']
            p01 = form.cleaned_data['p01']
            p02 = 1 - p01
            mu1 = form.cleaned_data['mu1']
            mu2 = form.cleaned_data['mu2']
            mu3 = form.cleaned_data['mu3']
            pai, rho = ex1_calculPai(lbd, p01, p02, mu1, mu2, mu3)
            pai = np.around(pai, decimals=5)
            rho1 = np.around(rho.item(0), decimals=3)
            rho2 = np.around(rho.item(1), decimals=3)
            rho3 = np.around(rho.item(2), decimals=3)
        else:
            form = Ex1Form()
    else:
        form = Ex1Form()
    if rho1<0 or rho1>1 or rho2<0 or rho2>1 or rho3<0 or rho3>1:
        return render(request, 'fluxapp/ex1.html', {'form': Ex1Form(), 'pai': 0, 'rho1': 0, 'rho2': 0, 'rho3': 0, 'err': 1})
    else:
        return render(request, 'fluxapp/ex1.html', {'form': form, 'pai': pai, 'rho1': rho1, 'rho2': rho2, 'rho3': rho3, 'err': 0})

def createFiles1(request):
    if request.method == 'POST':
        form = fileForm(request.POST)
        if form.is_valid():
            lbd = form.cleaned_data['lbd']
            nbFiles = form.cleaned_data['nbFiles']
            return redirect(reverse('createFiles2', kwargs={'lbd': lbd, 'nbFiles': nbFiles}))
        else:
            form = fileForm()
    else:
        form = fileForm()

    return render(request, 'fluxapp/createFiles1.html', {'form': form})

def createFiles2(request, lbd=1, nbFiles=1):
    return render(request, 'fluxapp/createFiles2.html', {'lbd': lbd, 'nbFiles': range(int(nbFiles))})

def systemResult(request):
    print(request.POST)

    lbd = float(request.POST['lbd'])
    print(lbd)

    mu_raw = np.array(request.POST.getlist('mu[]'))
    mu = mu_raw[1:len(mu_raw)].astype(float)
    print(mu)

    nbFiles = int(request.POST['nbFiles'])

    P = np.array(request.POST.getlist('P[0][]'))
    for i in range(1, nbFiles+1):
        line = 'P['+str(i)+'][]'
        q = np.array(request.POST.getlist(line))
        P = np.vstack((P, q))
    print(P)

    p0 = P[0, 1:nbFiles+1].astype(float)
    print(p0)
    P = P[1:nbFiles+1, 1:nbFiles+1].astype(float)
    print(P)
    I = np.eye(nbFiles, nbFiles)
    det = np.linalg.det(I - P)
    if det < 0:
        return JsonResponse({'err': 'det < 0'})
    else:
        rho = hospital_calculRho(nbFiles, lbd, mu, p0, P)

        rho_str = '_'.join(str(e) for e in rho)
        data = {}
        data['rho_str'] = rho_str
        data['err'] = 'non'
        print(data)
        return JsonResponse(data)