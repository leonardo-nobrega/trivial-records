
import io

RecordDictionary = dict[str, dict[str, str]]


def stream_to_record_dictionary(
        stream: io.TextIOBase
) -> RecordDictionary:
    result: RecordDictionary = {}
    current_record_name = None
    read_record_name = False
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
