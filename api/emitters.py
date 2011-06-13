from piston.emitters import Emitter

from icalendar import Event as calEvent
from icalendar import Calendar


class iCalEmitter(Emitter):
	
	def render(self, request):
		data = self.construct()
		cal = Calendar()
		
		cal.add('prodid', 'iCalendar Feed')
		cal.add('version', '1.0')
		for newevent in data:
			ical_event = calEvent()
			ical_event.add('summary', newevent['description'])
			for occurrence in newevent['event_time']:
				ical_event.add('dtstart', occurrence['start_date'])
				ical_event.add('dtend', occurrence['end_date'])
			ical_event['uid'] = newevent['id']
			cal.add_component(ical_event)

			return cal.as_string()

Emitter.register('ical', iCalEmitter, 'charset=utf-8')