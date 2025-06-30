from app import app

def tesst_home():       # name has to start with test for function too
    response = app.test_client().get("/")
    assert response.status_code==200
    assert response.data == b"hello world"