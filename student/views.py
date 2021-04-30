import stripe
from django.conf import settings
# from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
# from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .models import AdminData, StudentData, Resources, Clubs, Event, Placements

stripe.api_key = settings.STRIPE_SECRET_KEY

# Create your views here.


def login_view(request):
    if request.method == "GET":
        try:
            if request.session['user']:
                return HttpResponseRedirect(reverse("student:index"))
            else:
                return render(request, "student/login.html")
        except:
            return render(request, "student/login.html")

    if request.method == "POST":
        user = request.POST["username"]
        enroll = request.POST["enroll_no"]
        passwd = request.POST["password"]
        role = request.POST["role"]
        dept = request.POST["dept_id"]

        if role == "admin":
            try:
                AdminData.objects.get(
                    username=user, password=passwd, dept_id=dept, enroll_no=enroll)
                request.session['user'] = enroll
                request.session['admin'] = True
                return HttpResponseRedirect(reverse("student:index"))
            except:
                return render(request, "student/login.html", {
                    "message": "Invalid Credentials"
                })
        elif role == "student":
            try:
                StudentData.objects.get(
                    username=user, password=passwd, dept_id=dept, enroll_no=enroll)
                request.session['user'] = enroll
                request.session['admin'] = False
                return HttpResponseRedirect(reverse("student:index"))
            except:
                return render(request, "student/login.html", {
                    "messageAlert": "Invalid Credentials"
                })
    return render(request, "student/login.html")


def index(request):
    if request.method == "GET":
        try:
            if request.session['user']:
                flag = request.session['admin']
                if flag == True:
                    return render(request, "faculty/index.html")
                else:
                    return render(request, "student/index.html")
        except:
            return HttpResponseRedirect(reverse("student:login"))


def logout_view(request):
    try:
        del request.session['user']
        del request.session['admin']
        return HttpResponseRedirect(reverse("student:login"))
    except:
        return HttpResponseRedirect(reverse("student:login"))


def templates(request, search):
    if request.method == "GET":
        try:
            if request.session['user']:
                user = request.session['user']
                flag = request.session['admin']
                resources = Resources.objects.all()
                clubs = Clubs.objects.all()
                placements = Placements.objects.all()
                event = Event.objects.all()
                if flag == True:
                    data = AdminData.objects.get(enroll_no=user)
                    return render(request, f"faculty/{search}.html", {
                        "data": data,
                        "resources": resources,
                        'clubs': clubs,
                        'placements': placements,
                        "event": event
                    })
                else:
                    data = StudentData.objects.get(enroll_no=user)
                    return render(request, f"student/{search}.html", {
                        "data": data,
                        "resources": resources,
                        'clubs': clubs,
                        'placements': placements,
                        "event": event
                    })
        except:
            return HttpResponseRedirect(reverse("student:login"))
    if request.method == "POST":
        try:
            if request.session['user']:
                user = request.POST["username"]
                enroll = request.POST["enroll_no"]
                passwd = request.POST["password"]
                dept = request.POST["dept_id"]
                role = request.POST["role"]
                if role == "admin":
                    try:
                        form = AdminData(
                            username=user, password=passwd, dept_id=dept, enroll_no=enroll)
                        form.save()
                        return render(request, "faculty/register.html", {
                            "messageSuccess": "Admin Created"
                        })
                    except:
                        return render(request, "faculty/register.html", {
                            "messageAlert": "User Already Exist"
                        })
                elif role == "student":

                    try:
                        form = StudentData(
                            username=user, password=passwd, dept_id=dept, enroll_no=enroll)
                        form.save()
                        return render(request, "faculty/register.html", {
                            "messageSuccess": "User Created"
                        })
                    except:
                        return render(request, "faculty/register.html", {
                            "messageAlert": "User Already Exist"
                        })
        except:
            HttpResponse(500)
            return render(request, "student/login.html", {
                "message": "Please Login Again"
            })


def setting(request):
    if request.method == "POST":
        try:
            if request.session['user']:
                role = request.session['admin']
                enroll = request.session['user']
                passwd = request.POST['currPassword']
                newPasswd = request.POST['newPassword']

                if role:
                    try:
                        form = AdminData.objects.get(
                            enroll_no=enroll, password=passwd)
                        form.password = newPasswd
                        form.save()
                        HttpResponseRedirect("/admin/settings")
                        return render(request, "faculty/settings.html", {
                            "messageSuccess": "Password Updated"
                        })
                    except:
                        HttpResponseRedirect("/admin/settings")
                        return render(request, "faculty/settings.html", {
                            "messageAlert": "Wrong Password"
                        })
                else:
                    try:
                        form = StudentData.objects.get(
                            enroll_no=enroll, password=passwd)
                        form.password = newPasswd
                        form.save()

                        HttpResponseRedirect("/app/settings")
                        return render(request, "student/settings.html", {
                            "messageSuccess": "Password Updated"
                        })
                    except:
                        HttpResponseRedirect("/app/settings")
                        return render(request, "student/settings.html", {
                            "messageAlert": "Wrong Password"
                        })
        except:
            HttpResponse(500)
            return render(request, "student/login.html", {
                "message": "Please Login Again"
            })


def handleFileUpload(request, fileName):
    if request.method == "POST":
        title = request.POST["title"]
        details = request.POST["details"]
        try:
            resource = request.FILES["resource"]
            fs = FileSystemStorage()
            filename = fs.save(resource.name, resource)
            url = fs.url(filename)
        except:
            resource = None
            url = None

        if fileName == "resources":
            dept = request.POST["dept_id"]
            type = request.POST["type"]
            form = Resources(title=title, details=details, type=type,
                             dept_id=dept, file_name=resource, file_link=url)
            form.save()

        # Placements
        if fileName == 'placement':
            link = request.POST['applyForm']
            form = Placements(company=title, details=details,
                              document=resource, documentUrl=url, form_link=link)
            form.save()

        # Clubs
        if fileName == "clubs":
            form = Clubs(title=title, details=details,
                         file_name=resource.name, file_link=url)
            form.save()

        # Events
        if fileName == "event":
            form = Event(title=title, details=details,
                         file_name=resource.name, file_link=url)
            form.save()

        return HttpResponseRedirect(f"/admin/{fileName}")
    else:
        return HttpResponse(400)


# Stripe Integration
class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'inr',
                        'unit_amount': 7700000,
                        # 'unit_amount': 7700,
                        'product_data': {
                            'name': 'Tuition',
                            'images': ['https://images.unsplash.com/20/cambridge.JPG?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1030&q=80'],
                        },
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url='http://127.0.0.1:8000/app/success',
            cancel_url='http://127.0.0.1:8000/app/cancel',
        )

        return JsonResponse({'id': checkout_session.id})

# @csrf_exempt
# def stripe_webhook(request):
#     payload = request.body
#     sig_header = request.META['HTTP_STRIPE_SIGNATURE']
#     event = None
#     try:
#         event = stripe.Webhook.construct_event(
#             payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
#         )
#     except ValueError as e:
#         # Invalid payload
#         return HttpResponse(status=400)
#     except stripe.error.SignatureVerificationError as e:
#         # Invalid signature
#         return HttpResponse(status=400)

#      # Handle the checkout.session.completed event
#     if event['type'] == 'checkout.session.completed':
#         session = event['data']['object']
#         customer_email = session['customer_details']['email']
#         send_mail(
#             subject="Receipt of transaction",
#             message="Thank you, your tuition fees has been received successfully. It will be updated in your account soon",
#             recipient_list=[customer_email],
#             from_email="jashmerchant@gmail.com"
#         )
#     return HttpResponse(status=200)


def checkout(request):
    return render(request, "student/checkout.html")


def success(request):
    return render(request, "student/success.html")


def cancel(request):
    return render(request, "student/cancel.html")
