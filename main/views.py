from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from django.views.generic.edit import FormView, FormMixin
from . models import Description, Witcher, WitcherSchool, Wizard, Kingdom, Quest, Comment, Contract, Personal, Monster
from . forms import CommentForm
from django.views.generic.base import View
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, login
from django.contrib.auth.models import Group

# Create your views here.

class MainView(TemplateView):  # Главная страница
    template_name = 'main/main.html'


class WitcherView(TemplateView):  # Страница Ведьмака
    template_name = 'main/witcher.html'
    extra_context = {'witchers' : Witcher.objects.all()}


class WizardView(TemplateView):  # Страница Чародеев
    template_name = 'main/wizard.html'
    extra_context = {'wizards' : Wizard.objects.all()}


class WitcherSchoolView(TemplateView):  # Страница Школа Ведьмаков
    template_name = 'main/witcher_school.html'
    extra_context = {'witcher_schools' : WitcherSchool.objects.all()}


class KingdomView(TemplateView):  # Страница Королевства
    template_name = 'main/kingdom.html'
    extra_context = {'kingdoms' : Kingdom.objects.all()}


class MonsterView(TemplateView):  # Страница Монстров
    template_name = 'main/monster.html'
    extra_context = {'monsters' : Monster.objects.all()}


class QuestView(TemplateView):  # Страница Квестов
    template_name = 'main/quest.html'
    extra_context = {'quests' : Quest.objects.all()}


class WitcherDetailView(FormMixin, DetailView): # Для отображения отдельных новостей
    model = Witcher
    form_class = CommentForm
    template_name = 'main/witcher_detail.html'
    context_object_name = 'witcher'  # Имя ключа для словаря при передаче в render

    def get_context_data(self, *args, **kwargs):
        context = super(WitcherDetailView, self).get_context_data(**kwargs)
        return context

    def get_object(self):
        witcher = super(DetailView, self).get_object()
        if self.request.method != 'POST':
            witcher.description.Number += 1 # Увеличиваем счетчик просмотров
            witcher.description.save()
        return witcher

    def get_success_url(self):
        return '/witcher/' + str(self.get_object().id)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.description = self.get_object().description
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


def delete_comment(request, pk):  # Удаление комментария
    comment = Comment.objects.get(id=pk)
    comment.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

class WizardDetailView(FormMixin, DetailView): # Для отображения отдельных новостей
    model = Wizard
    form_class = CommentForm
    template_name = 'main/wizard_detail.html'
    context_object_name = 'wizard'  # Имя ключа для словаря при передаче в render

    def get_context_data(self, *args, **kwargs):
        context = super(WizardDetailView, self).get_context_data(**kwargs)
        return context

    def get_object(self):
        wizard = super(DetailView, self).get_object()
        if self.request.method != 'POST':
            wizard.description.Number += 1 # Увеличиваем счетчик просмотров
            wizard.description.save()
        return wizard

    def get_success_url(self):
        return '/wizard/' + str(self.get_object().id)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.description = self.get_object().description
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class MonsterDetailView(FormMixin, DetailView): # Для отображения отдельных новостей
    model = Monster
    form_class = CommentForm
    template_name = 'main/monster_detail.html'
    context_object_name = 'monster'  # Имя ключа для словаря при передаче в render

    def get_context_data(self, *args, **kwargs):
        context = super(MonsterDetailView, self).get_context_data(**kwargs)
        return context

    def get_object(self):
        monster = super(DetailView, self).get_object()
        if self.request.method != 'POST':
            monster.description.Number += 1 # Увеличиваем счетчик просмотров
            monster.description.save()
        return monster

    def get_success_url(self):
        return '/monster/' + str(self.get_object().id)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.description = self.get_object().description
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class QuestDetailView(FormMixin, DetailView): # Для отображения отдельных новостей
    model = Quest
    form_class = CommentForm
    template_name = 'main/quest_detail.html'
    context_object_name = 'quest'  # Имя ключа для словаря при передаче в render

    def get_context_data(self, *args, **kwargs):
        context = super(QuestDetailView, self).get_context_data(**kwargs)
        return context

    def get_object(self):
        quest = super(DetailView, self).get_object()
        if self.request.method != 'POST':
            quest.description.Number += 1 # Увеличиваем счетчик просмотров
            quest.description.save()
        return quest

    def get_success_url(self):
        return '/quest/' + str(self.get_object().id)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.description = self.get_object().description
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class KingdomDetailView(FormMixin, DetailView): # Для отображения отдельных новостей
    model = Kingdom
    form_class = CommentForm
    template_name = 'main/kingdom_detail.html'
    context_object_name = 'kingdom'  # Имя ключа для словаря при передаче в render

    def get_context_data(self, *args, **kwargs):
        context = super(KingdomDetailView, self).get_context_data(**kwargs)
        return context

    def get_object(self):
        kigdom = super(DetailView, self).get_object()
        if self.request.method != 'POST':
            kigdom.description.Number += 1 # Увеличиваем счетчик просмотров
            kigdom.description.save()
        return kigdom

    def get_success_url(self):
        return '/kingdom/' + str(self.get_object().id)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.description = self.get_object().description
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)



class WitcherSchoolDetailView(FormMixin, DetailView): # Для отображения отдельных новостей
    model = WitcherSchool
    form_class = CommentForm
    template_name = 'main/witcher_school_detail.html'
    context_object_name = 'witcher_school'  # Имя ключа для словаря при передаче в render

    def get_context_data(self, *args, **kwargs):
        context = super(WitcherSchoolDetailView, self).get_context_data(**kwargs)
        return context

    def get_object(self):
        witcher_school = super(DetailView, self).get_object()
        if self.request.method != 'POST':
            witcher_school.description.Number += 1 # Увеличиваем счетчик просмотров
            witcher_school.description.save()
        witchers = Witcher.objects.all()
        res = []
        for w in witchers:
            contracts = w.contract_set.all()
            i = 0
            while i < len(contracts) and contracts[i].monster.name != 'Стрыга':
                i += 1
            if i == len(contracts):
                res.append(w)
        return witcher_school

    def get_success_url(self):
        return '/witcher_school/' + str(self.get_object().id)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.description = self.get_object().description
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class RegisterFormView(FormView): # Форма для регистрации нового пользователя
    form_class = UserCreationForm
    success_url = '../login'

    template_name = 'main/register.html'

    def form_valid(self, form):
        new_user = form.save()
        new_user.groups.add(Group.objects.get(name='visitor'))
        new_user.save()
        return super(RegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegisterFormView, self).form_invalid(form)


class LoginFormView(FormView): # Форма для авторизации нового пользователя
    form_class = AuthenticationForm
    success_url = "../"

    template_name = "main/login.html"

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View): # Форма для выхода из аккаунта
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("../")

import xml.etree.ElementTree as xml
root = xml.Element("witchers")
for witcher in res:
    xml_witcher = xml.Element("witcher")
    description = xml.SubElement(xml_witcher, "description")
    witcher_school = xml.SubElement(xml_witcher, "witcher_school")
    personal = xml.SubElement(xml_witcher, "personal")
    fame = xml.SubElement(xml_witcher, "fame")

    description.text = str(witcher.description)
    witcher_school.text = str(witcher.witcher_school)
    personal.text = str(witcher.personal)
    fame.text = str(witcher.fame)
    root.append(xml_witcher)
with open("xml_witchers", "w") as f:
    f.write(xml.tostring(root, encoding="utf-8", method="xml").decode(encoding="utf-8"))



