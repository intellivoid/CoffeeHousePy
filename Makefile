clean:
	rm -rf dltc/build
	rm -rf dltc/dist
	rm -rf dltc/coffeehouse_dltc.egg-info

build:
	python3 dltc/setup.py build
	python3 dltc/setup.py sdist

install:
	python3 dltc/setup.py install