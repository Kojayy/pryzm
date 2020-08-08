default:
	cat makefile

test:
	pytest -vvx tests

clean:
	find . -name "*.pyc" | xargs rm || true
	find . -name "__pycache__" | xargs rm -rr || true

publish:
	rm dist/*
	python setup.py sdist bdist_wheel
	python -m twine upload dist/*

