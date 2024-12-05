from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns=[path("",views.index,name="index"),
             path("Visualization/",views.Visualization,name="Visualization"),
             path("banking/",views.banking,name="banking"),
             path("Budget/",views.Budget,name="Budget"),
             path("sample/",views.sample,name="sample"),
             path('Register/', views.Register, name='Register'),
             path("login/",views.Login,name="login"),
             path('logout/', views.Logout, name='logout'),
             path('house/', views.house, name='house'),
             path('foodmodel/', views.foodmodel, name='foodmodel'),
             path('shoppingmod/', views.shoppingmod, name='shoppingmod'),
             path('travelmodel/', views.travelmodel, name='travelmodel'),
             path('healthmod/', views.healthmod, name='healthmod'),
             path('schooling/', views.schooling, name='schooling'),
             path('businesmod/', views.businesmod, name='businesmod'),
             path('social/', views.social, name='social'),
             path('enter/', views.enter, name='enter'),
             path('expense_tracking/', views.expense_tracking, name='expense_tracking'),
             path('api/expenses/', views.get_expenses, name='get_expenses'),
             path('budget_planning/', views.budget_planning, name='budget_planning'),
             path('logout/', auth_views.LogoutView.as_view(), name='logout'),]  # This handles the logout functionality
