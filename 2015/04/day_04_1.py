import hashlib

def search_for_hash_that_starts_with(input: str, should_start_with: str) -> int:
    i = 0
    while not hashlib.md5(f'{input}{i}'.encode()).hexdigest().startswith(should_start_with):
        i += 1
    return i

def main():
    print(search_for_hash_that_starts_with('iwrupvqb', should_start_with="00000"))

if __name__ == '__main__':
    main()