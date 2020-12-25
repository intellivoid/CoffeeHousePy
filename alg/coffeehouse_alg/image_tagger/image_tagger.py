import json
import requests

from coffeehouse_alg.exceptions import CoffeeHouseAlgException
from coffeehouse_alg.utilities import Utilities


class ImageTagger:

    def __init__(self, access_key=None,
                 illustration_endpoint="https://api.algorithmia.com/v1/web/algo/demo/IllustrationTaggerDemo/0.1.0",
                 inception_endpoint="https://api.algorithmia.com/v1/web/algo/demo/InceptionNetDemo/0.1.0",
                 js_source="https://demos.algorithmia.com/image-tagger/public/js/main.js"):
        """
        Public constructor

        :param endpoint: The main endpoint for Illustration Tagger
        :param js_source: The javascript source code containing the API Key
        """
        self.access_key = access_key
        self.illustration_endpoint = illustration_endpoint
        self.inception_endpoint = inception_endpoint
        self.js_source = js_source

        if access_key is None:
            self.access_key = Utilities.get_access_key(self.js_source)

    def predict_tags(self, image_content, results=12):
        """
        Processes the bare-bone request and returns the JSON results

        :param image_content:
        :param results:
        :return:
        """
        headers = {
            "Accept": "application/json, text/javascript",
            "Authorization": self.access_key,
            "Content-Type": "application/json",
            "Origin": "https://demos.algorithmia.com",
            "Referer": "https://demos.algorithmia.com/image-tagger",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
        }
        payload = {
            "image": image_content,
            "numResults": results
        }
        headers = Utilities.add_client_headers(headers)

        response = requests.post(self.illustration_endpoint, data=json.dumps(payload), headers=headers)
        j_response = json.loads(response.text)

        if 'error' in j_response:
            raise CoffeeHouseAlgException('SERVER', j_response['error']['message'], response)

        return j_response

    def predict_inception(self, image_content):
        """
        Processes the bare-bone request and returns the JSON results

        :param image_content:
        :return:
        """
        headers = {
            "Accept": "application/json, text/javascript",
            "Authorization": self.access_key,
            "Content-Type": "application/json",
            "Origin": "https://demos.algorithmia.com",
            "Referer": "https://demos.algorithmia.com/image-tagger",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
        }
        headers = Utilities.add_client_headers(headers)

        response = requests.post(self.inception_endpoint, data=json.dumps(image_content), headers=headers)
        j_response = json.loads(response.text)

        if 'error' in j_response:
            raise CoffeeHouseAlgException('SERVER', j_response['error']['message'], response)

        return j_response