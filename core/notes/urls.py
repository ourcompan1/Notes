from django.urls import path
from .views import *

urlpatterns = [
    path('', reg_page, name='reg_page'),
    path('/', reg_page, name='reg_page'),

    path('login', login_page,name='login'),
    path('login/', login_page,name='login'),

    path('login/notes', note_page, name='note_page'),
    path('login/notes/', note_page, name='note_page'),

    path('login/notes/loguot', logout_page, name='logout'),
    path('login/notes/loguot/', logout_page, name='logout'),

]