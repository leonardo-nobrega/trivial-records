
import trivial_records as tr

BOOKS = """
Peopleware
author1 Tom DeMarco
author2 Timothy Lister
publisher Addison Wesley

Fluent Python
author Luciano Ramalho
publisher O'Reilly
"""


def test_number_of_records_in_books_fixture() -> None:
    record_dictionary = tr.string_to_record_dictionary(BOOKS)
    assert len(record_dictionary) == 2


def test_first_record() -> None:
    record_dictionary = tr.string_to_record_dictionary(BOOKS)
    assert "Peopleware" in record_dictionary
    record = record_dictionary["Peopleware"]
    assert "author1" in record
    assert record["author1"] == "Tom DeMarco"
    assert "author2" in record
    assert record["author2"] == "Timothy Lister"
    assert "publisher" in record
    assert record["publisher"] == "Addison Wesley"


def test_second_record() -> None:
    record_dictionary = tr.string_to_record_dictionary(BOOKS)
    assert "CCNA 200-301" in record_dictionary
    record = record_dictionary["CCNA 200-301"]
    assert "author" in record
    assert record["author"] == "Wendell Odom"
    assert "publisher" in record
    assert record["publisher"] == "Cisco Press"


def test_empty_string() -> None:
    assert not tr.string_to_record_dictionary("")


def test_encode_decode() -> None:
    expected = {"one": {"a": "1", "b": "2"}, "two": {"c": "3"}}
    actual = tr.string_to_record_dictionary(
        tr.record_dictionary_to_string(expected)
    )
    assert expected == actual
