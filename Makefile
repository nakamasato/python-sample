init:
	pip install -r requirements.txt

test:
	pytest --pyargs sample

.PHONY: init test