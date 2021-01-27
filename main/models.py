from django.db import models
from django.contrib.auth.models import User


class Personal(models.Model):
    FIO = models.CharField('ФИО', max_length=100)
    race = models.CharField('Раса', max_length=100)
    sex = models.CharField('Пол', max_length=100)
    Date = models.DateField('Дата рождения')

    def __str__(self):
        return self.FIO

    class Meta:
        verbose_name = 'Личная информация '
        verbose_name_plural = 'Личная информация'


class Description(models.Model):
    Text = models.TextField('Текст')
    Number = models.IntegerField('Количество просмотров', default=0)

    def __str__(self):
        return self.Text

    class Meta:
        verbose_name = 'Описание'
        verbose_name_plural = ' Описания'


class WitcherSchool(models.Model):
    description = models.ForeignKey(Description, on_delete=models.CASCADE)
    location = models.CharField('Расположение', max_length=100)
    specialization = models.CharField('Специализация', max_length=100)
    name = models.CharField('Название', max_length=50)

    def __str__(self):
        return self.specialization

    class Meta:
        verbose_name = 'Школа Ведьмаков'
        verbose_name_plural = 'Школы Ведьмаков'


class Kingdom(models.Model):
    description = models.ForeignKey(Description, on_delete=models.CASCADE)
    square = models.CharField('Площадь', max_length=100)
    name = models.CharField('Название', max_length=50)

    def __str__(self):
        return self.square

    class Meta:
        verbose_name = 'Королевство'
        verbose_name_plural = 'Королевства'


class Monster(models.Model):
    description = models.ForeignKey(Description, on_delete=models.CASCADE)
    ability = models.CharField('Способность', max_length=100)
    name = models.CharField('Название', max_length=50)

    def __str__(self):
        return self.ability

    class Meta:
        verbose_name = 'Чудовище'
        verbose_name_plural = 'Чудовища'


class Witcher(models.Model):
    description = models.ForeignKey(Description, on_delete=models.CASCADE)
    witcher_school = models.ForeignKey(WitcherSchool, on_delete=models.CASCADE)
    personal = models.ForeignKey(Personal, on_delete=models.CASCADE)
    fame = models.CharField('Известность', max_length=100)

    def __str__(self):
        return self.fame

    class Meta:
        verbose_name = 'Ведьмак'
        verbose_name_plural = 'Ведьмаки'


class Wizard(models.Model):
    description = models.ForeignKey(Description, on_delete=models.CASCADE)
    kingdom = models.ForeignKey(Kingdom, on_delete=models.CASCADE)
    personal = models.ForeignKey(Personal, on_delete=models.CASCADE)
    fame = models.CharField('Известность', max_length=100)
    magic = models.CharField('Магия', max_length=100)

    def __str__(self):
        return self.magic

    class Meta:
        verbose_name = 'Чародей'
        verbose_name_plural = 'Чародеи'


class Quest(models.Model):
    description = models.ForeignKey(Description, on_delete=models.CASCADE)
    zone = models.CharField('Зона', max_length=100)
    name = models.CharField('Название', max_length=50)

    def __str__(self):
        return self.zone

    class Meta:
        verbose_name = 'Квест'
        verbose_name_plural = 'Квесты'


class Contract(models.Model):
    description = models.ForeignKey(Description, on_delete=models.CASCADE)
    witcher = models.ForeignKey(Witcher, on_delete=models.CASCADE)
    place = models.CharField('Место контракта', max_length=100)
    monster = models.ForeignKey(Monster, on_delete=models.CASCADE)

    def __str__(self):
        return self.place

    class Meta:
        verbose_name = 'Контракт'
        verbose_name_plural = 'Контракты'



class Comment(models.Model):
    comment = models.TextField('Комментарий')
    description = models.ForeignKey(Description, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime = models.DateTimeField('Дата и время', auto_now_add=True)

    def __str__(self):
        return self.comment

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
