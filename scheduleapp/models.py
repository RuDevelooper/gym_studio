from django.db import models


class Trainer(models.Model):
    class Meta:
        verbose_name = 'Тренер'
        verbose_name_plural = 'Тренеры'

    name = models.CharField(max_length=100, verbose_name='Фамилия Имя')
    photo = models.ImageField(verbose_name='Изображение', upload_to='trainer_photos/', default='static/img/team-01.jpg')
    position = models.CharField(verbose_name='Должность', max_length=100)
    description = models.TextField(verbose_name='Описание тренера', null=True, blank=True)
    instagram = models.CharField(max_length=200, verbose_name='Ссылка на Instagramm', null=True, blank=True)
    telegram = models.CharField(max_length=200, verbose_name='Профиль в Telegram', null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

    # user = ForeignKey.User


class WorkoutType(models.Model):
    class Meta:
        verbose_name = 'Вид занятий'
        verbose_name_plural = 'Виды занятий'

    title = models.CharField(verbose_name='Название', max_length=100)
    photo = models.ImageField(verbose_name='Изображение', upload_to='workout_photos/', default='workout_photos/default.png')
    description = models.TextField(verbose_name='Описание')

    # equipment = models.TextField(verbose_name='Краткое описание')

    def __str__(self):
        return f'{self.title}'


class Workout(models.Model):
    class Meta:
        verbose_name = 'Занятие'
        verbose_name_plural = 'Расписание занятий'

    type = models.ForeignKey(WorkoutType, on_delete=models.CASCADE, related_name='workout',
                             verbose_name='Вид тренировки', blank=False)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, related_name='workout', verbose_name='Тренер',
                                blank=False)

    INTENSITY_CHOICE = (
        ('1', 'Слабая'),
        ('2', 'Средняя'),
        ('3', 'Высокая')
    )
    intensity = models.CharField(max_length=1, choices=INTENSITY_CHOICE, default='1', verbose_name='Интенсивность')
    date = models.DateField(verbose_name='Дата')
    start_workout = models.TimeField(verbose_name='Начало тренировки')
    workout_time = models.PositiveSmallIntegerField(verbose_name='Продолжительность (минут)')

    def __str__(self):
        return f'{self.type} {self.date} в {self.start_workout}'
