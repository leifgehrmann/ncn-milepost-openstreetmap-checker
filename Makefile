install:
	pip install -r requirements.txt

check:
	python3 check.py > output.csv
