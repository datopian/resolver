from flask_jsonpify import jsonpify
import unittest
try:
    from unittest.mock import Mock, patch
except ImportError:
    from mock import Mock, patch

from importlib import import_module
module = import_module('resolver.controllers')


class ResolverTest(unittest.TestCase):

    def test___call___resolver(self):
        out = module.resolve('datahub/data-x')
        self.assertEqual(out['userid'], 'datahub')
        self.assertEqual(out['packageid'], 'data-x')
