clean:
	# APT Mod
	rm -rf mods/apt/build
	rm -rf mods/apt/dist
	rm -rf mods/apt/coffeehouse_dltc.egg-info

	# Stopwords Mod
	rm -rf mods/stopwords/build
	rm -rf mods/stopwords/dist
	rm -rf mods/stopwords/coffeehouse_dltc.egg-info

	# Tokenizer Mod
	rm -rf mods/tokenizer/build
	rm -rf mods/tokenizer/dist
	rm -rf mods/tokenizer/coffeehouse_dltc.egg-info

	# Deep Learning Text Classification
	rm -rf dltc/build
	rm -rf dltc/dist
	rm -rf dltc/coffeehouse_dltc.egg-info

build:
	# APT Mod
	python3 mods/apt/setup.py build
	python3 mods/apt/setup.py sdist

	# Stopwords Mod
	python3 mods/stopwords/setup.py build
	python3 mods/stopwords/setup.py sdist

	# Tokenizer Mod
	python3 mods/tokenizer/setup.py build
	python3 mods/tokenizer/setup.py sdist

	# Deep Learning Text Classification
	python3 dltc/setup.py build
	python3 dltc/setup.py sdist

install:
	python3 mods/apt/setup.py install
	python3 mods/stopwords/setup.py install
	python3 mods/tokenizer/setup.py install
	python3 dltc/setup.py install