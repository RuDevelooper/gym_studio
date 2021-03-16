from django.shortcuts import render
from django.views.generic import TemplateView
from scheduleapp.models import *
import datetime


class Schedule(TemplateView):
    template_name = 'mainapp/schedule.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        date = datetime.date.today()
        start_week = date - datetime.timedelta(date.weekday())
        end_week = start_week + datetime.timedelta(7)
        s = Workout.objects.filter(date__range=[start_week, end_week])

        # w_d = list(map(lambda x: x[0].weekday(), s.values_list('date')))
        ws = {}

        for i in range(7):
            if not ws.setdefault(i):
                ws.update(
                    {
                        i: [],
                        # 'today': date == w.date,
                    }
                )
            for w in s.filter(date__iso_week_day=i+1):
                ws[i].append(
                    {
                        'type': w.type,
                        'trainer': w.trainer,
                        'intensity': int(w.intensity),
                        'start_workout': w.start_workout,
                        'end_workout': (datetime.datetime.combine(date.today(), w.start_workout) + datetime.timedelta(minutes=w.workout_time)).time(),
                        'workout_time': w.workout_time,
                        'date': w.date,
                        'photo': w.type.photo.url,
                    }
                )

        # context['workouts'] = [
        #     {
        #         i: [
        #             {
        #                 'type': w.type,
        #                 'trainer': w.trainer,
        #                 'intensity': w.intensity,
        #                 'start_workout': w.start_workout,
        #                 'workout_time': w.workout_time,
        #             } for w in s.filter(date__week_day=i)
        #         ]
        #     } for i in range(1, 7)
        # ]
        context['workouts'] = ws
        context['start_week'] = start_week
        context['end_week'] = end_week
        context['today_weekday'] = date.weekday()
        return context
