from django.shortcuts import render, reverse
from django.views import View
from website import models
from website import forms
from django.core.mail import send_mail, EmailMessage
from django.http import JsonResponse
from django.template.loader import render_to_string

# Create your views here.
class Landing(View):
    def get(self, request):

        return render(request, 'website/index.html',
			{'request': request,})

    def post(self, request):
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        business_name = request.POST.get('business_name', '')
        size = request.POST.get('size', '')
        service = request.POST.get('service', '')
        message = request.POST.get('message', '')
        print(name, email, business_name)

        form = models.Business(name=name,
            email=email, company=business_name, size=size, service=service, message=message)
        form.save()
        '''
        html = 'Dear Braintree,<br><br>Please see the following contact form submission:<br>Name: {}<br>Email: {}<br>Company: {}<br>Size: {}<br>Service: {} <br>Message: {}<br><br>Regards,<br>The Verde Team'.format(name, 
            email, business_name, size, service, message)

        send_mail('[Website] Request Callback Form Submission - {}'.format(name), '', 'noreply@verde.work', 
            ['dimitrik@braintree.co.za',], fail_silently=False, html_message=html)
        '''

        return JsonResponse({'name':name})

class Error(View):
    def get(self, request):
        return render(request, 'website/error.html',
            {'request': request, })

class Case(View):
    def get(self, request):
        return render(request, 'website/case.html',
            {'request': request, })

class Read(View):
    def get(self, request):
        return render(request, 'website/read.html',
            {'request': request, })

class B2b(View):
    def get(self, request):
        return render(request, 'website/b2b.html',
            {'request': request, })

class Reseller(View):
    def get(self, request):
        return render(request, 'website/reseller.html',
            {'request': request, })

class Gaming(View):
    def get(self, request):
        return render(request, 'website/gaming.html',
            {'request': request, })

class Industry(View):
    def get(self, request):
        return render(request, 'website/industry.html',
            {'request': request, })

class Azure(View):
    def get(self, request):
        return render(request, 'website/azure.html',
            {'request': request, })

class Ms(View):
    def get(self, request):
        return render(request, 'website/ms.html',
            {'request': request, })

class Product(View):
    def get(self, request):
        return render(request, 'website/product.html',
            {'request': request, })

class Signup(View):
    def get(self, request):
        return render(request, 'website/signup.html',
            {'request': request, })

class Contact(View):
    def get(self, request):
        return render(request, 'website/contact.html',
            {'request': request, })

class Shop(View):
    def get(self, request):
        return render(request, 'website/shop.html',
            {'request': request, })

class Home(View):
    def get(self, request):

        return render(request, 'website/itco.html',
			{'request': request,})

    def post(self, request):
        name = request.POST.get('callback_name', '')
        email = request.POST.get('callback_email', '')
        phone = request.POST.get('callback_phone', '')

        contact = models.Callback(name=name,
            email=email, phone=phone)
        contact.save()

        html = 'Dear Braintree Consulting,<br><br>Please see the following contact form submission:<br>Name: {}<br>Email: {}<br>Phone: {}<br><br>Regards,<br>The Braintree Team'.format(name, 
            email, phone)

        send_mail('[Website] Request Callback Form Submission - {}'.format(name), '', 'no-reply@braintree.co.za', 
            ['dimitrik@braintree.co.za',], fail_silently=False, html_message=html)

        html = render_to_string('website/email/callback.html', {'name': name})

        send_mail('{}, Welcome to Braintree'.format(name), '', 'dimitrik@braintree.co.za',
            [email], html_message=html)

        return JsonResponse({'name':name})

class Error(View):
    def get(self, request):
        return render(request, 'website/error.html',
            {'request': request, })

class Gaming(View):
    def get(self, request):
        return render(request, 'website/gaming.html',
            {'request': request, })

class Tournaments(View):
    def get(self, request):
        return render(request, 'website/tournaments.html',
            {'request': request, })

class BlogG(View):
    def get(self, request):
        return render(request, 'website/blogG.html',
            {'request': request, })

class ShopG(View):
    def get(self, request):
        return render(request, 'website/shopG.html',
            {'request': request, })

class ProductG(View):
    def get(self, request):
        return render(request, 'website/productG.html',
            {'request': request, })

class Account(View):
    def get(self, request):
        return render(request, 'website/account.html',
            {'request': request, })

class SignupG(View):
    def get(self, request):
        return render(request, 'website/signupG.html',
            {'request': request, })

def ajax_individual(request):
    form = forms.IndividualForm(request.POST, request.FILES)
    
    if form.is_valid():
        form = form.save(commit=False)
        form.save()

        html = 'Dear Braintree,<br><br>Please see the following INDIVIDUAL form submission:<br>Name: {}<br>Email: {}<br>Phone: {}<br><br>Regards,<br>The Braintree Team'.format(form.name, 
            form.email, form.phone)

        email = EmailMessage('[Website] INDIVIDUAL Form Submission - {}'.format(form.name), html, 'webmaster@braintree.co.za', ['hello@braintree.co.za'])
        email.content_subtype = 'html'
        email.send()

        html = render_to_string('website/email/individual.html', {'name': form.name})

        send_mail('{}, Welcome to Braintree'.format(form.name), '', 'no-reply@braintree.co.za',
            [form.email], html_message=html)


        return JsonResponse({'name': form.name})

def ajax_business(request):
    name = request.POST.get('name', '')
    email = request.POST.get('email', '')
    phone = request.POST.get('phone', '')
    company = request.POST.get('company', '')

    contact = models.Business(name=name,
        email=email, phone=phone, company=company)
    contact.save()

    html = 'Dear Braintree,<br><br>Please see the following BUSINESS form submission:<br>Name: {}<br>Email: {}<br>Phone: {}<br>Company: {}<br>Regards,<br>The Braintree Team'.format(name, 
        email, phone, company)

    send_mail('[Website] BUSINESS Form Submission - {}'.format(name), '', 'no-reply@braintree.co.za', 
        ['dimitrik@braintree.co.za',], fail_silently=False, html_message=html)

    html = render_to_string('website/email/business.html', {'name': name})

    send_mail('{}, Welcome to Braintree'.format(name), '', 'no-reply@braintree.co.za',
        [email], html_message=html)


    return JsonResponse({'name':name})