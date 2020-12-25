clean:
	# APT Mod
	rm -rf mods/apt/build mods/apt/dist mods/apt/coffeehousemod_apt.egg-info

	# Stopwords Mod
	rm -rf mods/stopwords/build mods/stopwords/dist mods/stopwords/coffeehousemod_stopwords.egg-info

	# Tokenizer Mod
	rm -rf mods/tokenizer/build mods/tokenizer/dist mods/tokenizer/coffeehousemod_tokenizer.egg-info

	# Deep Learning Text Classification
	rm -rf dltc/build dltc/dist dltc/coffeehouse_dltc dltc/coffeehouse_dltc.egg-info

build:
	# APT Mod
	cd mods/apt; python3 setup.py build; python3 setup.py sdist

	# Stopwords Mod
	cd mods/stopwords; python3 setup.py build; python3 setup.py sdist

	# Tokenizer Mod
	cd mods/tokenizer; python3 setup.py build; python3 setup.py sdist

	# Deep Learning Text Classification
	cd dltc; python3 setup.py build; python3 setup.py sdist

install:
	cd mods/apt; python3 setup.py install
	cd mods/stopwords; python3 setup.py install
	cd mods/tokenizer; python3 setup.py install
	cd dltc; python3 setup.py install