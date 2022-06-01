#!/usr/bin/env python3

import requests
import logging
import os

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s: [ %(levelname)s ] %(message)s'
)
log = logging.getLogger(os.path.basename(__file__))

class LeshanRESTAPIWrapper():
    def __init__(self):
        self.host = "http://localhost:8080/api"
        self.session = requests.Session()
        self.device_id    = None
        self.device_id_bs = None

    def set_device_id(self, imei):
        self.device_id    = f"urn:imei:{imei}"
        self.device_id_bs = f"urn:imei:{imei}-bs"

    def _delete(self, path):
        url = f"{self.host}{path}"
        return self.session.delete(url)

    def _get(self, path):
        url = f"{self.host}{path}"
        return self.session.get(url)

    def _post(self, path, payload):
        url = f"{self.host}{path}"
        return self.session.post(url, headers={ "Content-Type": "application/json" }, json=payload)

    def _put(self, path, payload):
        url = f"{self.host}{path}"
        return self.session.put(url, headers={ "Content-Type": "application/json" }, json=payload)

    @staticmethod
    def check_response(response):
        status_code = response.status_code
        if status_code < 200 or status_code >= 300:
            caller = inspect.stack()[1]
            raise SystemExit(
                f"{caller.filename}, {caller.lineno}: "
                f"{caller.function} received a response object with status code {status_code}"
            )

    def get_clients(self):
        r = self._get("/clients")
        self.check_response(r)
        return r

    def read_resources(self, path):
        if not path:
            r = self._get(f"/clients/{self.device_id}")
        else:
            r = self._get(f"/clients/{self.device_id}{path}")
        self.check_response(r)
        return r

    def write_single_resource(self, path, payload):
        """
        Path format:

            /<object id>/<instance id>/<resource id>

        Payload example:

            {
                "id": 1,
                "value": 60
            }
        """
        return self._put(f"/clients/{self.device_id}{path}", payload)

    def write_resources(self, path, payload):
        """
        Path format:

            /<object id>/<instance id>

        Payload example:

            {
                "id":"0",
                "resources":[
                    { "id": 1, "value": 30 },
                    { "id": 2, "value": 10 },
                    { "id": 3, "value": 10 },
                    { "id": 5, "value": 0 },
                    { "id": 6, "value": True },
                    { "id": 7, "value": "U" }
                ]
            }
        """
        return self._put(f"/clients/{self.device_id}{path}", payload)

# TODO: Continue to add methods for this.

if __name__ == "__main__":
    leshan = LeshanRESTAPIWrapper()
    r = leshan.get_clients()
