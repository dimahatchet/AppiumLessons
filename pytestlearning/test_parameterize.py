import pytest


#log = logging.Logger(__name__, logging.INFO)


def get_data():
    return [
        ("trainer@way2automation.com", "password1"),
        ("java@way2automation.com", "password2"),
        ("info@way2automation.com", "password3")
    ]


@pytest.mark.parametrize("username,password", get_data())
def test_do_login(username, password):
    print(username, "---", password)
    #logger = log()
    #logger.info("This is a v new log")
    #logger.error("This is an v error message")
