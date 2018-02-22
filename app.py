
import falcon
import json


LEDS = {"red": "RED COLOR",
        "green": "GREEN COLOR"}


class LedsResource(object):
    def on_get(self, req, resp):
        """
        Return main menu
        """
        resp.status = falcon.HTTP_200  # This is the default status

        resp.set_header('Powered-By', 'Falcon')
        resp.body = (json.dumps({"led_url": req.url + "led/{green | red}/"
                                    ,"led_url_POST": {"state": "{1 | 0}"}}))

class LedsResourceTwo(object):
    def on_get(self, req, resp, color):
        """
        Return current state for LED indicated by the color parameter
        """
        resp.status = falcon.HTTP_200
        resp.set_header('Powered-By', 'Falcon')

        if color in LEDS:
            resp.body = (json.dumps({color: "simulated_state"}))
        else:
            resp.body = (json.dumps({"error": "color_not_found"}))

    def on_post(self, req, resp, color):
        """
        Change state of LED indicated by the color parameter
        """
        if color in LEDS:
            print("Received:", color, req.get_params("state"))
        resp.body = (json.dumps({"response": "all_ok"}))


app = falcon.API()

app.add_route('/', LedsResource())
app.add_route('/led/{color}', LedsResourceTwo())


if __name__ == "__main__":
    pass