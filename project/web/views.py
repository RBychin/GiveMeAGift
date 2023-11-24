from datetime import datetime
from django.shortcuts import redirect, get_object_or_404
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView

from core.models import Event, Gift, WebConfig
from web.forms import EventForm, GiftForm


class EventList(ListView):
    model = Event
    template_name = 'web/event_list.html'
    context_object_name = 'events'


class EventDetail(DetailView):
    model = Event
    template_name = 'web/event_detail.html'
    context_object_name = 'event'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['config'] = WebConfig.objects.get(pk=1)
        return context


class HolidayCreate(CreateView):
    template_name = 'web/event_create.html'
    form_class = EventForm
    extra_context = {'title': 'Создание события'}

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return redirect('event:main', pk=obj.id)


class GiftCreate(CreateView):
    template_name = 'web/event_create.html'
    form_class = GiftForm
    extra_context = {'title': 'Добавление подарка'}

    def form_valid(self, form):
        event = get_object_or_404(Event, pk=self.kwargs.get('pk'))
        gift = form.save(commit=False)
        gift.event = event
        gift.save()
        return redirect('event:main', pk=event.pk)
