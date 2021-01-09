clean:
	rm -rf build

build:
	# Building JAR
	mkdir build
	ant jar
	mv coffeehouse_corenlp.jar build/

	# Adding Libs
	cp lib/* build/
	cp liblocal/* build/

	# Updating models
	python3 update_model.py
	cp /var/resources/CoffeeHouseData-CoreNLP/* build/

start:
	cd build; java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -port 5604 -timeout 15000