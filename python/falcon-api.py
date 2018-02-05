import json
import falcon
import shlex
import subprocess
from wsgiref import simple_server


class TemperatureResource(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        with open('/home/pi/pifan/data/curr_temp.json', 'r') as tempfile:
                response = tempfile.read()
        resp.body = (response)


class ThresholdResource(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        with open('/home/pi/pifan/data/curr_threshold.json', 'r') as tempfile:
                response = tempfile.read()
        resp.body = (response)

    def on_post(self, req, resp, th_temp):

        data = {'temperature': "{0:0.1f}".format(float(th_temp))}
        with open('/home/pi/pifan/data/curr_threshold.json', 'w') as outfile:
                json.dump(data, outfile)

        resp.status = falcon.HTTP_201


class ShutdownResource(object):
    def on_get(self, req, resp):
        shutdown_command = shlex.split("sudo shutdown -h now")
        subprocess.call(shutdown_command)
        resp.status = falcon.HTTP_200
        resp.body = (response)


# falcon.API instances are callable WSGI apps
app = falcon.API()

temperature = TemperatureResource()
threshold = ThresholdResource()
shutdown = ShutdownResource()

app.add_route('/api/curr_temp', temperature)
app.add_route('/api/curr_threshold', threshold)
app.add_route('/api/threshold/{th_temp}', threshold)
app.add_route('/api/shutdown_this_pihole', shutdown)

if __name__ == '__main__':
    httpd = simple_server.make_server('0.0.0.0', 8000, app)
    httpd.serve_forever()
