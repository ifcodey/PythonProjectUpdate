from django.urls import path
from  . import views

urlpatterns = [
    # for registration to driver
    path('', views.login),
    path('reg',views.reg),
    path('driver',views.driver),

    # for registration to police
    path('regp',views.police),
    path('police',views.regpolice),

    # for login to User
    path('login',views.login),
    path('logout', views.logout),
    path('signin',views.signin),
    path('policeinfo',views.policeinfo),
    path('addviolation',views.addviolation),
    path('add', views.add_vio),
    path('showviolation', views.showviolation),
    path('rule', views.rule),
    path('home',views.home),
]
