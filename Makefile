PIP=.venv/bin/pip
NOSETEST=.venv/bin/nosetests
PYTHON=.venv/bin/python

test:clean
	PYTHONPATH=. ${NOSETEST} -v

venv:
	virtualenv .venv

setup:venv
	${PIP} install -U pip
	${PIP} install -r requirements.txt

clean:
	find . -name "*.pyc" -exec rm -rf {} \;
