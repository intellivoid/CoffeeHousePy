from coffeehouse_translation import ChTranslation
from hyper_internal_service import web

__all__ = ['Server']


class Server(object):

    def __init__(self, port=5603):
        """
        Public Constructor
        :param port:
        """
        self.port = port
        self.web_application = web.Application()
        self.web_application.add_routes(
            [
                web.post('/', self.root_page),
                web.post('/google_translate', self.google_translate)
            ]
        )
        self.ch_translation = ChTranslation()

    async def root_page(self, request):
        """
        Handles the "/" page, does nothing special

        :return:
        """
        return web.json_response({"status": True})

    async def google_translate(self, request):
        """
        Handles the predict request "/google_translate", usage:
        POST:: "source": str Source language
        POST:: "output": str Output language
        POST:: "input": str The input data
        :param request:
        :return:
        """
        post_data = await request.post()
        results = self.ch_translation.google_translate(post_data["source"], post_data["output"], post_data["input"])
        response = {
            "status": True,
            "results": results
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
