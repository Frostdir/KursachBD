from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainView.as_view(), name='main'),
    path('witcher', views.WitcherView.as_view(), name='witcher'),
    path('wizard', views.WizardView.as_view(), name='wizard'),
    path('witcher_school', views.WitcherSchoolView.as_view(), name='witcher_school'),
    path('monster', views.MonsterView.as_view(), name='monster'),
    path('kingdom', views.KingdomView.as_view(), name='kingdom'),
    path('quest', views.QuestView.as_view(), name='quest'),
    path('witcher/<int:pk>', views.WitcherDetailView.as_view(), name='witcher_detail'),
    path('delete_comment/<int:pk>', views.delete_comment, name='delete_comment'),
    path('wizard/<int:pk>', views.WizardDetailView.as_view(), name='wizard_detail'),
    path('witcher_school/<int:pk>', views.WitcherSchoolDetailView.as_view(), name='witcher_school_detail'),
    path('monster/<int:pk>', views.MonsterDetailView.as_view(), name='monster_detail'),
    path('kingdom/<int:pk>', views.KingdomDetailView.as_view(), name='kingdom_detail'),
    path('quest/<int:pk>', views.QuestDetailView.as_view(), name='quest_detail'),
    path('register', views.RegisterFormView.as_view(), name='register'),
    path('login', views.LoginFormView.as_view(), name='login'),
    path('logout', views.LogoutView.as_view(), name='logout'),
]
