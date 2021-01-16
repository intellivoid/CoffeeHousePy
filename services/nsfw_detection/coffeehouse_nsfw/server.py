import os
import base64
import random
import string

from hyper_internal_service import web

from .classifier import Classifier

__all__ = ['Server']


class Server(object):

    def __init__(self, port=5602):
        """
        Public Constructor
        :param port:
        """
        self.port = port
        self.web_application = web.Application()
        self.web_application.add_routes(
            [web.post('/', self.predict)]
        )
        self.letters = string.ascii_lowercase
        self.classifier = Classifier()

    def get_tmp(self, ext):
        file_name = ''.join(random.choice(self.letters) for i in range(24)) + "." + ext
        return os.path.join("/tmp", file_name)

    async def predict(self, request):
        """
        Handles the predict request "/", usage:
        POST:: "input": str
        :param request:
        :return:
        """
        post_data = await request.post()

        tmp_image = self.get_tmp(post_data["type"])
        with open(tmp_image, 'wb') as f:
            f.write(base64.b64decode(post_data["input"]))

        results = self.classifier.classify(tmp_image)[tmp_image]
        os.remove(tmp_image)

        response = {
            "status": True,
            "results": {
                "unsafe": str(results['unsafe']),
                "safe": str(results['safe'])
            }
        }
        return web.json_response(response)

    def start(self):
        """
        Starts the web application
        :return:
        """
        web.run_app(app=self.web_application, port=self.port)
        return True

    def stop(self):
        """
        Stops the web application
        :return:
        """
        self.web_application.shutdown()
        self.web_application.cleanup()
        return True