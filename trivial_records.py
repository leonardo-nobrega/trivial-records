
import io

from typing import Generator

RecordDictionary = dict[str, dict[str, str]]


def stream_to_record_dictionary(stream: io.TextIOBase) -> RecordDictionary:
    result: RecordDictionary = {}
    read_record_name = True
    current_record_name = None
    while line := stream.readline():
        line = line.strip()
        if not line:
            read_record_name = True
            current_record_name = None
        else:
            if read_record_name:
                current_record_name = line
                result[current_record_name] = {}
                read_record_name = False
            else:
                key, value = line.split(maxsplit=1)
                assert current_record_name is not None
                result[current_record_name][key] = value
    return result


def string_to_record_dictionary(string: str) -> RecordDictionary:
    return stream_to_record_dictionary(io.StringIO(string))


def record_dictionary_to_string_generator(
        record_dictionary: RecordDictionary
) -> Generator[str, None, None]:
    separator = False
    for record_name, record in record_dictionary.items():
        if separator:
            yield "\n"
        separator = True
        yield record_name + "\n"
        for key, value in record.items():
            yield key + " " + value + "\n"


def record_dictionary_to_string(record_dictionary: RecordDictionary) -> str:
    generator = record_dictionary_to_string_generator(record_dictionary)
    return "".join(list(generator))
