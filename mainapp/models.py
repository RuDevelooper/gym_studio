from django.db import models
from multiselectfield import MultiSelectField


class Membership(models.Model):
    class Meta:
        verbose_name = 'Абонемент'
        verbose_name_plural = 'Абонементы'

    title = models.CharField(max_length=20, verbose_name='Название')
    group = models.ForeignKey(to='MembershipGroup', on_delete=models.PROTECT, verbose_name='Группа', related_name='group')
    unique_together = ['title', 'group']

    payment_period_choice = [
        ('once', 'Разовый'),
        ('week', 'Неделя'),
        ('month', 'Месяц'),
        ('3_month', '3 месяца'),
        ('6_month', '6 месяцев'),
        ('9_month', '9 месяцев'),
        ('year', 'Год')
    ]

    payment_period = models.CharField(max_length=30,
                                      choices=payment_period_choice,
                                      default='month',
                                      verbose_name='Период оплаты')
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')
    options = models.ManyToManyField(to='MembershipOptions', verbose_name='Опции')

    def __str__(self):
        return f'{self.title} - {self.group}'

class PromotionPrice(models.Model):
    class Meta:
        verbose_name = 'Акция и скидка'
        verbose_name_plural = 'Акции и скидки'

    title = models.CharField(max_length=20, verbose_name='Название')
    description = models.TextField(verbose_name='Описание скидки', null=True, blank=True)
    discount = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Скидка')

    def __str__(self):
        return f'{self.title}'

class MembershipGroup(models.Model):
    class Meta:
        verbose_name = 'Группа абонементов'
        verbose_name_plural = 'Группы абонементов'

    title = models.CharField(max_length=100, verbose_name='Название группы')
    description = models.TextField(verbose_name='Описание группы', null=True, blank=True)

    options = models.ManyToManyField(to='MembershipGroupOptions', verbose_name='Примечания', blank=True)

    def __str__(self):
        return f'{self.title}'

class MembershipOptions(models.Model):
    class Meta:
        verbose_name = 'Опция абонемента'
        verbose_name_plural = 'Опции абонементов'

    title = models.TextField(max_length=200, verbose_name='Опция')
    important = models.BooleanField(verbose_name='Выделить в группе?', default=False)

    def __str__(self):
        return f'{self.title}'

class MembershipGroupOptions(models.Model):
    class Meta:
        verbose_name = 'Опция группы'
        verbose_name_plural = 'Опции группы'

    title = models.TextField(max_length=200, verbose_name='Опция')

    def __str__(self):
        return f'{self.title}'
