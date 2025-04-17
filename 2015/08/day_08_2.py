from pathlib import Path
from day_08_1 import read_santas_list, get_sum_of_string_characters

def encode_record(record: str) -> str:
    record = record.replace('\\', r'\\')
    record = record.replace(r'"', r'\"')
    record = f'"{record}"'
    return record

def get_sum_of_encoded_characters(santas_list: list[str]) -> int:
    return sum([len(encode_record(record)) for record in santas_list])

if __name__ == '__main__':
    santas_list = read_santas_list(Path('input.txt'))
    print(get_sum_of_encoded_characters(santas_list) - get_sum_of_string_characters(santas_list))

