default:
	cat makefile

test:
	pytest -vvx tests

clean:
	find . -name "*.pyc" | xargs rm || true
	find . -name "__pycache__" | xargs rm -rr || true
