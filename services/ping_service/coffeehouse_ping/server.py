from hyper_internal_service import web

__all__ = ['Server']


class Server(object):

    def __init__(self, port=5600):
        """
        Public Constructor
        :param port:
        """
        self.port = port
        self.web_application = web.Application()
        self.web_application.add_routes(
            [web.post('/', self.ping)]
        )

    async def ping(self, request):
        """
        Handles the predict request "/", usage:
        POST:: "input": str
        :param request:
        :return:
        """
        post_data = await request.post()
        return web.json_response({"status": True})

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