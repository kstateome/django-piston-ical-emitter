# Django Piston iCal Emitter

This custom emitter allows you to request django piston api objects in an iCal format.

## Dependencies
* Django
* Django-Piston
* icalendar 

## Usage

You will need to add emitters.py to your api project and then import it into your handlers file.  From there passing ?format=ical should activate the use of the custom emitter.

The event object will need a description, id, start date, end date.  This emitter is setup to handle a collection of events, but can handle a single event as well.

I'm open to any and all contributions and improvements.
