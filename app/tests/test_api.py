import os
import pytest
from flask.testing import FlaskClient
from flask_migrate import upgrade  # , downgrade
from werkzeug.test import TestResponse

from .. import create_app


class Context:
    def __init__(self, app, client: FlaskClient, api_token: str):
        self.app = app
        self.client = client
        self.api_token = api_token


def expect_status_code(r: TestResponse, code: int):
    assert (
        r.status_code == code
    ), f"Expected status code {code}, got {r.status_code}, response: {r.data.decode('utf-8')}"


g_ctx = None


@pytest.fixture()
def ctx():
    global g_ctx
    if g_ctx is not None:
        yield g_ctx
        return

    app = create_app("testing")

    # make sure that testing DB does not exist
    db_path = app.config.get("SQLALCHEMY_DATABASE_URI").replace("sqlite:///", "")
    if os.path.exists(db_path):
        os.remove(db_path)

    with app.app_context():
        upgrade()

    # recreate app to initialize activity table
    app = create_app("testing")

    # get API token
    with app.test_client() as client:
        # log in via HTTP
        r = client.post("/auth/login", data={"username": "admin", "password": "admin"})
        assert r.status_code == 302

        r = client.get("/").data.decode("utf-8")
        i = r.index('R.init("') + 8
        j = r.index('",', i)
        api_token = r[i:j]

        g_ctx = Context(app, client, api_token)
        yield g_ctx
        return

    g_ctx = None
    raise Exception("Could not create app context")


def test_create_sample(ctx: Context):
    """Test that samples can be created using the API."""
    r = ctx.client.put(
        "/api/sample",
        headers={"Authorization": "Bearer " + ctx.api_token},
        data={"name": "Sample_1", "description": "Test sample"},
    )
    expect_status_code(r, 201)


def test_create_action(ctx: Context):
    """Test that actions can be created using the API."""
    sample_id = 1
    r = ctx.client.put(
        f"/api/action/{sample_id}",
        headers={"Authorization": "Bearer " + ctx.api_token},
        data={"description": "Test action"},
    )
    expect_status_code(r, 201)