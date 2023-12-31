from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView

from core.models import Event
from web.forms import EventForm, GiftForm


class EventList(ListView):
    model = Event
    template_name = 'web/event_list.html'
    context_object_name = 'events'


class EventDetail(DetailView):
    model = Event
    template_name = 'web/event_detail.html'
    context_object_name = 'event'


class EventCreate(CreateView):
    template_name = 'web/event_create.html'
    form_class = EventForm
    extra_context = {'title': 'Создание события'}

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
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
