from pathlib import Path
from day_17_1 import read_computer


def main():
    computer = read_computer(Path("input.txt"))
    run = True
    i = 1
    program_length = len(computer.program)
    while run:
        computer.registry_a = i
        computer.run_program()
        if len(computer.output) < len(computer.program):
            i *= 8
            continue
        for j in range(program_length - 1, 0, -1):
            if computer.output[j] != computer.program[j]:
                i += pow(8, j)
                break
        if computer.output == computer.program:
            run = False
            continue
        i += 1
    print(i)

if __name__ == '__main__':
    main()
