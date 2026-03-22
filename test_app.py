import pytest
from dash.testing.application_runners import import_app


@pytest.fixture
def app():
    return import_app("app")


def test_header(dash_duo, app):
    dash_duo.start_server(app)
    header = dash_duo.find_element("h1")
    assert header is not None
    assert header.text != ""



def test_graph_present(dash_duo, app):
    dash_duo.start_server(app)
    graph = dash_duo.find_element("#graph")  # ensure your graph has id="graph"
    assert graph is not None



def test_region_picker(dash_duo, app):
    dash_duo.start_server(app)
    dropdown = dash_duo.find_element("#region-picker")  # ensure id matches your dropdown
    assert dropdown is not None