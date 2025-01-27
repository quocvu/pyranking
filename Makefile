init:
	pip install -r requirements.txt

test:
	python -m unittest discover -v

coverage:
	coverage run -m unittest discover

publish:
	python3 -m twine upload dist/* --verbose

.PHONY: init test
