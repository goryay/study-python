from chap_11.name_function import get_formatted_name

def test_first_last_name():
    formatted_name = get_formatted_name("john", "doe")
    assert formatted_name == "John Doe"

def test_first_last_middle_name():
    formatted_name = get_formatted_name("wolfgang", "mozart", "amadeus")
    assert formatted_name == "Wolfgang Amadeus Mozart"