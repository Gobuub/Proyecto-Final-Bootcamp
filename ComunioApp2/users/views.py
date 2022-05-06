from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.base import View
# Create your views here.


class LoginView(View):
    def get(self,request):
        return render(request, 'login.html')

    def post(self, request):
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return HttpResponse(content=b'Success')
        return self.get(request)


class LogoutView(View):

    def get(self, request):
        if request.user.is_authenticated:
            logout(request)

            return redirect('login')


class IndexView(View):

    def get(self, request):

        if request.user.is_authenticated:

            return render(request, 'index.html')

        return redirect('login')
