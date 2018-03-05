from logging import getLogger

from gevent.wsgi import WSGIServer

from rico.app.core.factory import create_app

log = getLogger(__name__)

if __name__ == '__main__':
    # Create and run Flask app
    app = create_app('miami')
    port = 3310
    http_server = WSGIServer(('', port), app, log=log)
    http_server.serve_forever()
