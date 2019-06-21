from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('excel-upload/', views.excelSheetData, name='excel_sheet_data'),

    path('env/', views.envByUserName, name='by_username'),
    path('env-by-month/', views.envByMonth, name='env_by_month'),

    path('env-by-users/', views.environmentsByUser, name='env_by_users'),

    path('environments-by-month/', views.environmentsByMonth, name='environment_by_month'),
    path('user-by-environments-by-month/', views.userByEnvironmentsByMonth, name='user_by_environments_by_month'),






]