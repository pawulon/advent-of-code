from day_10_1 import look_and_say

def main():
    text = '3113322113'
    for _ in range(50):
        text = look_and_say(text)
    print(len(text))

if __name__ == '__main__':
    main()

