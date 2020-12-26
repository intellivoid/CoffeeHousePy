clean_apt:
	rm -rf mods/apt/build mods/apt/dist mods/apt/coffeehousemod_apt.egg-info

clean_stopwords:
	rm -rf mods/stopwords/build mods/stopwords/dist mods/stopwords/coffeehousemod_stopwords.egg-info

clean_tokenizer:
	rm -rf mods/tokenizer/build mods/tokenizer/dist mods/tokenizer/coffeehousemod_tokenizer.egg-info

clean_dltc:
	rm -rf dltc/build dltc/dist dltc/coffeehouse_dltc.egg-info

clean_nlpfr:
	rm -rf nlpfr/build nlpfr/dist nlpfr/nltk.egg-info

clean_alg:
	rm -rf alg/build alg/dist alg/coffeehouse_alg.egg-info

clean_his:
	rm -rf hyper_internal_service/build hyper_internal_service/dist hyper_internal_service/hyper_internal_service.egg-info

clean:
	make clean_apt clean_stopwords clean_tokenizer clean_nlpfr
	make clean_dltc
	make clean_his
	make clean_alg

# ======================================================================================================================

build_apt:
	cd mods/apt; python3 setup.py build; python3 setup.py sdist

build_stopwords:
	cd mods/stopwords; python3 setup.py build; python3 setup.py sdist

build_tokenizer:
	cd mods/tokenizer; python3 setup.py build; python3 setup.py sdist

build_mods:
	make build_apt build_stopwords build_tokenizer

build_nlpfr:
	make build_mods
	cd nlpfr; python3 setup.py build; python3 setup.py sdist

build_dltc:
	cd dltc; python3 setup.py build; python3 setup.py sdist

build_alg:
	cd alg; python3 setup.py build; python3 setup.py sdist

build_his:
	cd hyper_internal_service; python3 setup.py build; python3 setup.py sdist

build:
	make build_nlpfr
	make build_his
	make build_dltc
	make build_alg

# ======================================================================================================================

install_apt:
	cd mods/apt; python3 setup.py install

install_stopwords:
	cd mods/stopwords; python3 setup.py install

install_tokenizer:
	cd mods/tokenizer; python3 setup.py install

install_mods:
	make install_apt install_stopwords install_tokenizer

install_nlpfr:
	make install_mods
	cd nlpfr; python3 setup.py install

install_dltc:
	cd dltc; python3 setup.py install

install_alg:
	cd alg; python3 setup.py install

install_his:
	cd hyper_internal_service; python3 -m pip install -Ur dev_requirements.txt; python3 setup.py install

install:
	make install_nlpfr
	make install_his
	make install_dltc
	make install_alg

# ======================================================================================================================

system_prep_python:
	apt install python3

system_prep_pip:
	apt -y install python3 python3-distutils wget curl
	wget https://bootstrap.pypa.io/get-pip.py
	python3 get-pip.py
	rm get-pip.py

system_prep_gcc:
	apt -y install gcc
