import requests
import unittest

class V2exApiTestCase(unittest.TestCase):

    def test_node_api(self):
    url = "https://www.v2ex.com/api/nodes/show.json"
    querystring = {"name": "python"}
    response = requests.request("GET", url, params-querystring).json
    self.assertEquals(response['name'],querystring['name'])


if __name__ == '__main__':
    unittest.main

