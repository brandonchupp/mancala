clean-pyc:
	find . -name '*.pyc' -exec rm -f \;

init:
	pip install -r requirements.txt

test: clean-pyc
	py.test --verbose --color=yes

run:
	python3 MancalaRunner.py
