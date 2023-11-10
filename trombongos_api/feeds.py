from django_ical.views import ICalFeed

from api.models import TourCalendar, Event


class EventFeed(ICalFeed):
    """
    A simple event calender
    """
    product_id = '-//trombongos.ch//Tour//DE'
    timezone = 'Europe/Zurich'
    file_name = "saison.ics"

    def items(self):
        # categories = Category.objects.all().filter(event__season__active=True).order_by('-date_start', '-sort')
        tour = TourCalendar.objects.all().filter(season__active=True).order_by('category__sort')
        return tour

    def item_guid(self, item):
        return f'{item.uuid}@trombongos.ch'

    def item_title(self, item):
        return item.name

    def item_description(self, item):
        if item.fetch_events:
            events = Event.objects.all().filter(category=item.category).filter(season__active=True).order_by(
                'category__sort')

            description_string = "Termine heute:\n\n"
            for event in events:

                if event.makeup is not None:
                    description_string = description_string + f'{event.makeup} Uhr - Schminken Magazin\n\n'
                if event.sun is not None:
                    description_string = description_string + f'{event.warehouse} Uhr - Abfahrt Car Magazin\n{event.sun} Uhr Abfahrt Car Sonne\n\n'

                description_string = description_string + f'{event.play} - {event.name}\n'

            return description_string
        else:
            return ""

    def item_start_datetime(self, item):
        '''

        event = Event.objects.all().filter(category=item).order_by('-date', 'sort').first()
        time_start = event.play
        if event.makeup is not None:
            time_start = event.makeup
        date_format = "%Y-%m-%d %H:%M:%S"
        print(f'START: {event.date} {time_start}')
        return datetime.strptime(f'{item.date_start} {time_start}', date_format)
        '''
        return item.from_dt

    def item_end_datetime(self, item):
        '''
        event = Event.objects.all().filter(category=item).order_by('-date', 'sort').last()

        date_format = "%Y-%m-%d %H:%M:%S"
        date_string = f'{event.date} {event.play}'
        time_end = datetime.strptime(date_string, date_format)
        time_end_add_delta = time_end + timedelta(minutes=30)

        print(f'END: {time_end_add_delta}')
        return time_end_add_delta
        '''
        return item.to_dt

    def item_link(self, item):
        return f'https://trbapi.thievent.org/api/v1/{item.id}'
