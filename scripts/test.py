from getpost import getPost

def test_api():
    res = getPost("Cute")
    assert res != None
