# CoffeeHouse SpamDetection

Library for detecting spam by classifying input as spam/ham


## Installation

Install the following packages using the corresponding setup and makefile
operations provided by the repo, or use CoffeeHouse-Server's install script
to install all the required components

 - Hyper-Internal-Service
 - CoffeeHouse-NLPFR
 - CoffeeHouse-DLTC 
 - CoffeeHouseMod-Tokenizer
 - CoffeeHouseMod-StopWords
 - CoffeeHouseMod-APT
 
Finally, install CoffeeHouse-SpamDetection by running `python3 setup.py install`


# Build Model

You can update the model build by adding new data to .dat files located in 
`model/spam_ham/` then proceed to build the model by running `./build_model`.
This process will product a directory called `spam_ham_build` which you should
copy over to `coffeehouse_spamdetection/` and replace the already existing
files. This process is resource intensive so make sure you are running
this operation on supported chipsets that were manufactured after 2014.


## Example Usage
```py
from coffeehouse_spamdetection.main import SpamDetection

spam_detection = SpamDetection()
spam_detection.predict("Test")
# {'ham': 0.998092, 'spam': 0.0017609089}
```


## Start as server
```shell script
python3 -m coffeehouse_spamdetection --start-server
```

This process will run using port `5601` and only accepts POST requests
with the parameter `input` as plain text. You should recieve a JSON 
response that looks like this

```json
{
  "status": true,
  "results": {
    "ham": "0.998092",
    "spam": "0.0017609089"
  }
}
```