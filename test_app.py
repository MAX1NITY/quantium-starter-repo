import pytest
from app import app


def test_check_header_present(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#header", timeout=4)
    header = dash_duo.find_element("#header")
    assert header is not None

def test_check_visual_present(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#sales-graph", timeout=4)
    visual = dash_duo.find_element("#sales-graph")
    assert visual is not None

def test_check_radio_present(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#radio-buttons", timeout=4)
    region = dash_duo.find_element("#radio-buttons")
    assert region is not None

