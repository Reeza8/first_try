from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from accounts.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordResetForm
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

def login_view(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            username=request.POST['username']
            password=request.POST['password']
            if '@' in username:
                user2 = User.objects.get(email=username)
                user = authenticate(username=user2.username, password=password)
            else:    
                user = authenticate(username=username, password=password)    
            if user is not None:
                login(request,user)
                return redirect('/')
            else:
                messages.error(request, 'user not found') 
        return render(request,'accounts/login.html')
    else:
        return redirect('/')
@login_required
def logout_view(request):
    logout(request)
    return redirect('/')
    
def signup_view(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            form=UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'You signup succefully') 
                return redirect('/')
            else:
                messages.error(request, 'not valid inputs Your password can’t be too similar to your other personal information.Your password must contain at least 8 characters.Your password can’t be a commonly used password.Your password can’t be entirely numeric.') 

        form=UserCreationForm()
        return render(request,'accounts/signin.html',{'form':form})
    


def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "main/password/password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ("/password_reset/done/")
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="accounts/password_reset.html", context={"password_reset_form":password_reset_form})