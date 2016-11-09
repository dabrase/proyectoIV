install:
	pip install -r requirements.txt

test:
	cd ElMeteo_bot && python test.py

execute:
	cd ElMeteo_bot && python bot.py
