checker-install:
	cd checker && pip install -r requirements.txt

checker:
	cd checker
	python3 check.py -o ./output/output.csv

viewer-install:
	cd viewer && npm install

viewer-dev:
	cd viewer && npm run dev

viewer-build:
	cd viewer && npm run build
