# -*- coding: utf-8 -*-
import pytest

from main.app import create_app
from main.config import TestConfig
from tests.utils import TestClient


@pytest.fixture(scope='function')
def test_app():
    """Create test app instance."""

    return create_app(TestConfig)


@pytest.fixture(scope='function')
def testclient(test_app):
    """Create a test client to call APIs without serving a HTTP web server.

    Examples::

        def test_do_something(testclient):
            # POST
            testclient.post(
                '/catalogs',
                headers={},
                data={},
                content_type='application/json'
            )

            # GET
            testclient.get(
                '/catalogs',
                headers={},
                content_type='application/json'
            )
    """

    return TestClient(test_app.test_client())
