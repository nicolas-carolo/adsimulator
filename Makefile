.PHONY: default, lint

default:
	python -m adsimulator
lint:
	pylint adsimulator
pep8:
	autopep8 adsimulator --in-place --recursive --aggressive --aggressive
