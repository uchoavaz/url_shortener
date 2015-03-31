from django.shortcuts import render,get_object_or_404
from .forms import *
from .models import Url
from django.core.signing import Signer
from django.shortcuts import redirect


context = {}

def cadastre(request):
	protected_url = False

	if request.method == 'POST':
		signer = Signer()
		value = signer.sign(request.POST['url'])
		enc = value[len(request.POST['url'])+1:len(request.POST['url']) + 7]

		if 'protegido' in request.POST:
			protected_url = True
		
		url = Url.objects.create(original_url=request.POST['url'],short_url=enc,is_protected=protected_url,url_password=request.POST['senha'],email=request.POST['email'],slug=enc)
		url.save()

		context['dados'] = "Voce encurtou a Url: %s para %s \n A protecao dela esta %s e sua senha e : %s \n Seu email e : %s.Entre com /pesquisa/%s" % (request.POST['url'],enc,protected_url,request.POST['senha'],request.POST['email'],enc)
		return render(request,'cadastred.html',context)

	return render(request, 'home.html')


def redirectUrl(request,slug):

	url = get_object_or_404(Url,slug = slug)

	if request.method == 'POST':
		print (request.POST['senha'])
		if request.POST['senha'] == url.url_password:
			return redirect(url.original_url)
		else:
			return render(request,'home.html')

	else:
		if url.is_protected == True:
			return render(request,'url_password.html')
		else:
			return redirect(url.original_url)


def details(request,slug):
	url = get_object_or_404(Url, slug=slug)
	forms = UrlForm(instance = url)
	context['details'] = forms
	return render(request,'details.html',context)