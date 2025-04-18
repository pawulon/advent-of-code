def look_and_say(text: str) -> str:
    current_letter = text[0]
    current_letter_count = 1
    output = ''
    for letter in text[1:]:
        if letter == current_letter:
            current_letter_count += 1
        else:
            output += str(current_letter_count) + current_letter
            current_letter_count = 1
            current_letter = letter
    output += str(current_letter_count) + current_letter
    return output

def main():
    text = '3113322113'
    for _ in range(40):
        text = look_and_say(text)
    print(len(text))

if __name__ == '__main__':
    main()

