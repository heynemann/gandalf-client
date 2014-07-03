import client
import tornado.gen as gen


class AsyncTornadoGandalfClient(client.GandalfClient):

    @gen.coroutine
    def _request(self, *args, **kwargs):
        url = kwargs.pop('url')
        data = kwargs.pop('data', None)
        if data:
            kwargs['body'] = data

        response = yield self.client(url, *args, **kwargs)
        raise gen.Return(response)