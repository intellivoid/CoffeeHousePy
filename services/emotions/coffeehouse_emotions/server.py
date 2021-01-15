from hyper_internal_service import web

from .main import EmotionPrediction

__all__ = ['Server']


class Server(object):

    def __init__(self, port=5605):
        """
        Public Constructor
        :param port:
        """
        self.port = port
        self.web_application = web.Application()
        self.web_application.add_routes(
            [web.post('/', self.predict)]
        )
        self.emotion_prediction = EmotionPrediction()

    async def predict(self, request):
        """
        Handles the predict request "/", usage:
        POST:: "input": str
        :param request:
        :return:
        """
        post_data = await request.post()
        results = self.emotion_prediction.predict(post_data['input'])
        response = {
            "status": True,
            "results": {
                "neutral": str(results['neutral']),
                "happiness": str(results['happiness']),
                "affection": str(results['affection']),
                "sadness": str(results['sadness']),
                "anger": str(results['anger'])
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