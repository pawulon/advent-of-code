from pathlib import Path
import re


def read_santas_list(input_path: Path) -> list[str]:
    return input_path.read_text().split('\n')


def get_sum_of_string_characters(santas_list: list[str]) -> int:
    return sum([len(record) for record in santas_list])

def parse_record(record: str) -> str:
    record = record[1:-1]
    record = record.replace(r"\\", r"@")
    record = record.replace(r"\"", r"@")
    record = re.sub(r"\\x..", "@", record)
    return record

def get_sum_of_in_memory_characters(santas_list: list[str]) -> int:
    return sum([len(parse_record(record)) for record in santas_list])

if __name__ == '__main__':
    santas_list = read_santas_list(Path('input.txt'))
    print(get_sum_of_string_characters(santas_list) - get_sum_of_in_memory_characters(santas_list))

