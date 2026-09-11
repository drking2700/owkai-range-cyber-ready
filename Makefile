.PHONY: install test serve scan demo
install:
	python -m pip install -e '.[dev]'
test:
	pytest
serve:
	range serve
scan:
	python scripts/secret_scan.py .
demo:
	range init-db && range seed-demo
