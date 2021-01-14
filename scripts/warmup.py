"""
This script is executed on start-up after starting up the services, this is intended to check if all the services
has started correctly and load all the resources that are required are loaded, after this program is done
executing, the bootstrap should start the ping service so that programs know that CoffeeHouse-Utils is ready.
"""

import urllib.parse
import requests
import base64
import time
import sys


def core_nlp():
    print("[CORENLP] Warming up")

    current_tries = 0
    max_tries = 30  # 5 Minutes

    while True:
        if current_tries > max_tries:
            print("[CORENLP] ERROR! Too many attempts")
            sys.exit(1)

        try:
            r = requests.post("http://0.0.0.0:5604/?properties={\"annotators\": \"tokenize,ssplit,pos,ner,regexner,"
                              "sentiment\"}&pipelineLanguage=en",

                              headers={"Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"},
                              data=urllib.parse.quote_plus("The quick brown fox jumped over the lazy dog")
                              )
            if r.status_code == 200:
                print("[CORENLP] OK")
                break
            else:
                print("[CORENLP] Failed, Returned status code {0}, '{1}'".format(str(r.status_code), r.text))
        except:
            print("[CORENLP] Failed, request not completed")
            pass

        print("[CORENLP] Waiting 10 seconds")
        time.sleep(10)
        current_tries += 1

    print("[CORENLP] Started successfully")


def langdetect():
    print("[LANGDETECT] Warming up")

    current_tries = 0
    max_tries = 30  # 5 Minutes
    while True:
        if current_tries > max_tries:
            print("[LANGDETECT] ERROR! Too many attempts")
            sys.exit(1)

        try:
            r = requests.post("http://0.0.0.0:5606/", data={"input": "The quick brown fox jumped over the lazy dog"})
            if r.status_code == 200:
                print("[LANGDETECT] OK")
                break
            else:
                print("[LANGDETECT] Failed, Returned status code {0}, '{1}'".format(str(r.status_code), r.text))
        except:
            print("[LANGDETECT] Failed, request not completed")
            pass

        print("[LANGDETECT] Waiting 10 seconds")
        time.sleep(10)
        current_tries += 1

    print("[LANGDETECT] Started successfully")


def spamdetect():
    print("[SPAMDETECT] Warming up")

    current_tries = 0
    max_tries = 30  # 5 Minutes
    while True:
        if current_tries > max_tries:
            print("[SPAMDETECT] ERROR! Too many attempts")
            sys.exit(1)

        try:
            r = requests.post("http://0.0.0.0:5601/", data={"input": "The quick brown fox jumped over the lazy dog"})
            if r.status_code == 200:
                print("[SPAMDETECT] OK")
                break
            else:
                print("[SPAMDETECT] Failed, Returned status code {0}, '{1}'".format(str(r.status_code), r.text))
        except:
            print("[SPAMDETECT] Failed, request not completed")
            pass

        print("[SPAMDETECT] Waiting 10 seconds")
        time.sleep(10)
        current_tries += 1

    print("[SPAMDETECT] Started successfully")


def nsfw():
    print("[NSFW] Warming up")

    current_tries = 0
    max_tries = 30  # 5 Minutes

    import os
    print()

    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "red.jpg"), "rb") as img_file:
        image_data = base64.b64encode(img_file.read()).decode('utf-8')

    while True:
        if current_tries > max_tries:
            print("[NSFW] ERROR! Too many attempts")
            sys.exit(1)

        try:
            r = requests.post("http://0.0.0.0:5602/", data={
                "input": image_data,
                "type": "jpg"
            })
            if r.status_code == 200:
                print("[NSFW] OK")
                break
            else:
                print("[NSFW] Failed, Returned status code {0}, '{1}'".format(str(r.status_code), r.text))
        except:
            print("[NSFW] Failed, request not completed")
            pass

        print("[NSFW] Waiting 10 seconds")
        time.sleep(10)
        current_tries += 1

    print("[NSFW] Started successfully")


print("    (  )   (   )  )")
print("     ) (   )  (  (")
print("     ( )  (    ) )")
print("     _____________")
print("    <_____________> ___")
print("    |             |/ _ \\")
print("    |               | | |")
print("    |               |_| |")
print(" ___|             |\___/")
print("/    \___________/    \\")
print("\_____________________/")
print()
print("CoffeeHouse-Utils Warmup")

core_nlp()
spamdetect()
langdetect()
nsfw()

print("OK, CoffeeHouse-Utils seems to be running fine.")
print("Exiting with code 0, the ping service should start in the next step.")
sys.exit(0)
