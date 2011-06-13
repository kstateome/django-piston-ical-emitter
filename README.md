# Django Piston RSS Emitter

This custom emitter allows you to request django piston api objects in an RSS format.

## Dependencies
* Django
* Django-Piston
* PyRSS2Gen [http://www.dalkescientific.com/Python/PyRSS2Gen.html]

## Usage

You will need to add emitters.py to your api project and then import it into your handlers file.  From there passing ?format=rss should activate the use of the custom emitter.

You'll also need to modify emitters.py to build your RSS file with the data you pass it.  For this example I have used synopsis for the description and title for the title.

I'm open to any and all contributions and improvements.
