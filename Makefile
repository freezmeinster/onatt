run:
	@python manage.py runserver 0.0.0.0:9000
initdev:
	@rm db.sqlite3; python manage.py runscript initdev
