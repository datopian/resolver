from flask_jsonpify import jsonpify
import unittest
import requests_mock
try:
    from unittest.mock import Mock, patch
except ImportError:
    from mock import Mock, patch

from importlib import import_module
module = import_module('resolver.controllers')


class ResolverTest(unittest.TestCase):

    def setUp(self):
        module.config['AUTH_SERVER'] = 'https://example.com'
        self.mocked_resp ={'userid': 'id_for_datahub'}


    def test___call___resolver(self):
        with requests_mock.Mocker() as mock:
            mock.get('https://example.com/auth/resolve?username=datahub',
                    json=self.mocked_resp)
            out = module.resolve('datahub/data-x')
            self.assertEqual(out['userid'], 'id_for_datahub')
            self.assertEqual(out['packageid'], 'data-x')
