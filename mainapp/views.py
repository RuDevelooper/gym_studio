from django.conf import settings
from django.shortcuts import render
from telegram import ParseMode

from mainapp.models import Membership, PromotionPrice, Testimonial
from scheduleapp.models import Trainer, WorkoutType, Workout
import datetime

# Create your views here.
from django.views.generic import TemplateView
from tga.models import *
from .forms import GetDiscountForm
from tga.management.commands.bot import *

request = Request(
    connect_timeout=0.5,
    read_timeout=1.0,
)
bot = Bot(
    request=request,
    token=settings.TOKEN,
    base_url=getattr(settings, 'PROXY_URL', None),
)


class HomePage(TemplateView):
    template_name = 'mainapp/index.html'

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        if context["form"].is_valid():
            phone = context["form"]['phone'].value()
            bot.send_message(chat_id=542277086, text=f'<strong>ПЕРЕЗВОНИ</strong>\n {phone}', parse_mode=ParseMode.HTML)
            bot.send_message(chat_id=735314493, text=f'<strong>ПЕРЕЗВОНИ</strong>\n {phone}',
                             parse_mode=ParseMode.HTML)

        return super(TemplateView, self).render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # bot.send_message(chat_id=542277086, text='TEST')

        # send_message(chat_id=542277086)

        t = Testimonial.objects.all()
        context['testimonials'] = t

        f = WorkoutType.objects.all()
        context['fitness'] = f

        date = datetime.date.today()
        w = Workout.objects.filter(date__gt=date).order_by('date')
        context['workouts'] = w

        form = GetDiscountForm(self.request.POST or None)  # instance= None
        context["form"] = form

        return context


class Memberships(TemplateView):
    template_name = 'mainapp/membership.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        m = Membership.objects.all()
        p = PromotionPrice.objects.all()
        memberships = {}

        m.only('group').values_list('title')
        for i in m:
            if not memberships.setdefault(i.group.title):
                memberships.update(
                    {
                        i.group.title: {
                            'description': i.group.description,
                            'options': list(map(lambda x: x[0], i.group.options.values_list('title'))),
                            'memberships': []
                        }
                    }
                )
            mem_sh = {
                'price': i.price,
                'title': i.title,
                'payment_period': i.get_payment_period_display(),
                'options': list(map(lambda x: x[0], i.options.values_list('title')))
            }
            memberships[i.group.title]['memberships'].append(mem_sh)

        context['promo'] = [
            {
                'title': pr.title,
                'discount': pr.discount,
                'description': pr.description,
            } for pr in p
        ]
        context['memberships'] = memberships

        return context


class Facilities(TemplateView):
    template_name = 'mainapp/facilities.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        t = Testimonial.objects.all()
        context['testimonials'] = t

        return context


class Team(TemplateView):
    template_name = 'mainapp/team.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        t = Trainer.objects.all()
        context['trainers'] = t

        return context


class Contacts(TemplateView):
    template_name = 'mainapp/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
