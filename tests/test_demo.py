
def test_version():
    from wechart_apitest import __version__
    assert isinstance(__version__,str)