all:
	python setup.py build
	python setup.py install

register:
	python setup.py register -r pypi

upload:
	python setup.py sdist upload -r pypi

publish: register upload