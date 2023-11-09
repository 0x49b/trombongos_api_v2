from datetime import datetime, timedelta

from django_ical.views import ICalFeed

from api.models import Event, Category


class EventFeed(ICalFeed):
    """
    A simple event calender
    """
    product_id = '-//trombongos.ch//Tour//DE'
    timezone = 'Europe/Zurich'
    file_name = "saison.ics"

    def items(self):
        categories = Category.objects.all().filter(event__season__active=True).order_by('-date_start', '-sort')
        return categories

    def item_title(self, item):
        return item.name

    def item_description(self, item):
        events = Event.objects.all().filter(category=item).order_by('-date', 'sort')

        description_string = ""
        for event in events:

            if event.makeup is not None:
                description_string = description_string + f'Schminken {event.makeup} Uhr\n\n'

            print(event.transport)

            if event.transport == 'Car':
                description_string = description_string + f'Abfahrt Car Magazin {event.warehouse} Uhr\nAbfahrt Car Sonne {event.sun} Uhr'

            description_string = description_string + f'{event.play} - {event.name}\n'

        return description_string

    def item_start_datetime(self, item):

        event = Event.objects.all().filter(category=item).order_by('-date', 'sort').first()
        time_start = event.play
        if event.makeup is not None:
            time_start = event.makeup
        print(f'{item.date_start} {time_start}')

        date_format = "%Y-%m-%d %H:%M:%S"
        return datetime.strptime(f'{item.date_start} {time_start}', date_format)

    def item_end_datetime(self, item):
        event = Event.objects.all().filter(category=item).order_by('-date', 'sort').last()

        date_format = "%Y-%m-%d %H:%M:%S"
        date_string = f'{event.date} {event.play}'

        print(date_string)

        time_end = datetime.strptime(date_string, date_format)

        time_end_add_delta = time_end + timedelta(minutes=30)

        print(f'{time_end_add_delta}')

        return time_end_add_delta

    def item_link(self, item):
        return f'https://trbapi.thievent.org/api/v1/categories/{item.id}/'
