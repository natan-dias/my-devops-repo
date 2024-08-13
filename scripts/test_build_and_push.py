import pytest 

from build_and_push import build_image

def test_build_image():
    build_image('images/webserver-example')