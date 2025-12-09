
import io

import pytest

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


@pytest.fixture()
def record_dictionary() -> tr.RecordDictionary:
    return tr.make_record_dictionary(io.StringIO(BOOKS))


def test_number_of_records(
        record_dictionary: tr.RecordDictionary
) -> None:
    assert len(record_dictionary) == 2


def test_first_record(record_dictionary: tr.RecordDictionary) -> None:
    assert "Peopleware" in record_dictionary
    record = record_dictionary["Peopleware"]
    assert "author1" in record
    assert record["author1"] == "Tom DeMarco"
    assert "author2" in record
    assert record["author2"] == "Timothy Lister"
    assert "publisher" in record
    assert record["publisher"] == "Addison Wesley"


def test_second_record(record_dictionary: tr.RecordDictionary) -> None:
    assert "CCNA 200-301" in record_dictionary
    record = record_dictionary["CCNA 200-301"]
    assert "author" in record
    assert record["author"] == "Wendell Odom"
    assert "publisher" in record
    assert record["publisher"] == "Cisco Press"


def test_empty_string() -> None:
    assert not tr.make_record_dictionary_from_string("")
