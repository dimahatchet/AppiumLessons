import pytest


def test_validate_titles():
    expected_title = "Google.com"
    actual_title = "Googdle.com"
    title = "This is Gmail website"

    #if actual_title != expected_title:
    #     print("Test case fail")
    #else:
    #     print("Test case pass")

    print(" Beginning")
    assert expected_title == actual_title, "Titles are not matching"
    assert "Gmail" in title, "Gmail does not exist in the title"
    assert False, "forcefully failing the test"

    print("Ending")

    #pytest test_validate_titles.py -s -v --soft-asserts
