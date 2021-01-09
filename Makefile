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

clean_rf:
	rm -rf resource_fetch/build resource_fetch/dist resource_fetch/resource_fetch.egg-info

clean_his:
	rm -rf hyper_internal_service/build hyper_internal_service/dist hyper_internal_service/hyper_internal_service.egg-info

clean_langdetect:
	rm -rf services/language_detection/build services/language_detection/dist services/language_detection/coffeehouse_languagedetection.egg-info

clean_spamdetect:
	rm -rf services/spam_detection/build services/spam_detection/dist services/spam_detection/coffeehouse_spamdetection.egg-info

clean_translation:
	rm -rf services/translation/build services/translation/dist services/translation/coffeehouse_translation.egg-info

clean_corenlp:
	cd services/corenlp; make clean

clean:
	make clean_apt clean_stopwords clean_tokenizer clean_nlpfr
	make clean_dltc
	make clean_his
	make clean_alg
	make clean_rf
	make clean_translation
	make clean_langdetect
	make clean_spamdetect
	make clean_corenlp

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

build_rf:
	cd resource_fetch; python3 setup.py build; python3 setup.py sdist

build_langdetect:
	cd services/language_detection; python3 setup.py build; python3 setup.py sdist

build_spamdetect:
	cd services/spam_detection; python3 setup.py build; python3 setup.py sdist

build_translation:
	cd services/translation; python3 setup.py build; python3 setup.py sdist

build_corenlp:
	cd services/corenlp; make build

build:
	make build_nlpfr
	make build_his
	make build_dltc
	make build_alg
	make build_rf
	make buid_translation
	make build_langdetect
	make build_spamdetect
	make build_corenlp

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

install_rf:
	cd resource_fetch; python3 setup.py install
	python3 -m resource_fetch

install_langdetect:
	cd services/language_detection; python3 setup.py install

install_spamdetect:
	cd services/spam_detection; python3 setup.py install

install_translation:
	cd services/translation; python3 setup.py install

install:
	make install_rf
	make install_nlpfr
	make install_his
	make install_dltc
	make install_alg
	make install_translation
	make install_langdetect
	make install_spamdetect

# ======================================================================================================================

system_prep_python:
	apt -y install python3 python3-distutils python3-dev python3-setuptools

system_prep_pip:
	apt -y install wget curl
	wget https://bootstrap.pypa.io/get-pip.py
	python3 get-pip.py
	rm get-pip.py

system_prep_gcc:
	apt -y install gcc build-essential

system_prep_java:
	apt -y install openjdk-8-jre openjdk-8-jdk ant

# ======================================================================================================================

start_langdetect:
	python3 -m coffeehouse_languagedetection --start-server

start_spamdetect:
	python3 -m coffeehouse_spamdetection --start-server

start_translation:
	python3 -m coffeehouse_translation --start-server

start_corenlp:
	cd services/cornlp; make start

# ======================================================================================================================

docker_build:
	docker build -t="coffeehouse_utils" -f Dockerfile .

docker_run:
	docker run -it --name coffeehouse_utils -h coffeehouse_utils --restart always -p 5601:5601 -p 5606:5606 -p 5603:5603 -p 5604:5604 coffeehouse_utils

docker_rm:
	docker rm -f coffeehouse_utils