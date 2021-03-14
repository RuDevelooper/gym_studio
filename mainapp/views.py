from django.shortcuts import render
from mainapp.models import Membership, PromotionPrice

# Create your views here.
from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = 'mainapp/index.html'

    def get_context_data(self, **kwargs):
        return


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

