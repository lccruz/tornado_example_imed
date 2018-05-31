import uuid
import tornado.web
import tornado.websocket
import tornado.httpserver
import tornado.ioloop

PORT = 8888


class WebSocketHandler(tornado.websocket.WebSocketHandler):
    waiters = {}

    def check_origin(self, origin):
        return True

    def open(self, message):
        user_id = len(WebSocketHandler.waiters)
        WebSocketHandler.waiters[user_id] = self

    def on_message(self, message):
        for key, value in self.waiters.items():
            value.write_message(message)


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/websocket/(.*)', WebSocketHandler)
        ]
        settings = dict(
            # cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
            debug=False,
            autoreload=False,
            xsrf_cookies=False,
        )
        tornado.web.Application.__init__(self, handlers)


if __name__ == '__main__':
    ws_app = Application()
    server = tornado.httpserver.HTTPServer(ws_app)
    server.listen(PORT)
    tornado.ioloop.IOLoop.instance().start()
