
def test_import():
    import lorrel_py
    assert hasattr(lorrel_py, "__version__")
    assert lorrel_py.__version__ != ""
