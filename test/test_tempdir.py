import os
from backports.temporarydirectory import TemporaryDirectory


def test_smoke():
    with TemporaryDirectory() as td:
        assert os.path.isdir(td)
    assert not os.path.exists(td)
