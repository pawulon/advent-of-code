from pathlib import Path


class Computer:
    def __init__(self, registry_a: int, registry_b: int, registry_c: int, program: list[int]):
        self.registry_a = registry_a
        self.initial_registry_a = registry_a
        self.registry_b = registry_b
        self.registry_c = registry_c
        self.program = program
        self.pointer = 0
        self.output = []

    def __str__(self):
        return f"Computer(registry_a={self.registry_a}, registry_b={self.registry_b}, registry_c={self.registry_c}, program={self.program})"

    def reset(self):
        self.pointer = 0
        self.output = []

    def print_output(self):
        print(",".join(list(map(str, self.output))))

    def run_program(self):
        halt = False
        self.reset()
        while not halt:
            try:
                opcode = self.program[self.pointer]
                operand = self.program[self.pointer + 1]
            except IndexError:
                halt = True
                continue
            self.pointer += 2
            self.process_operation(opcode, operand)

    def process_operation(self, opcode: int, operand: int):
        match opcode:
            case 0:
                self.adv(operand)
            case 1:
                self.bxl(operand)
            case 2:
                self.bst(operand)
            case 3:
                self.jnz(operand)
            case 4:
                self.bxc()
            case 5:
                self.out(operand)
            case 6:
                self.bdv(operand)
            case 7:
                self.cdv(operand)

    def adv(self, operand: int):
        numerator = self.registry_a
        denominator = self.power(self.combo_value(operand))
        self.registry_a = self.division(numerator, denominator)

    def bxl(self, operand: int):
        self.registry_b = self.xor(self.registry_b, operand)

    def bst(self, operand: int):
        self.registry_b = self.modulo(self.combo_value(operand))

    def jnz(self, operand: int):
        if self.registry_a != 0:
            self.pointer = operand

    def bxc(self):
        self.registry_b = self.xor(self.registry_b, self.registry_c)

    def out(self, operand: int):
        output = self.modulo(self.combo_value(operand))
        self.output.append(output)

    def bdv(self, operand: int):
        numerator = self.registry_a
        denominator = self.power(self.combo_value(operand))
        self.registry_b = self.division(numerator, denominator)

    def cdv(self, operand: int):
        numerator = self.registry_a
        denominator = self.power(self.combo_value(operand))
        self.registry_c = self.division(numerator, denominator)

    def combo_value(self, operand: int) -> int:
        if operand <= 3:
            return operand
        match operand:
            case 4:
                return self.registry_a
            case 5:
                return self.registry_b
            case 6:
                return self.registry_c

    def modulo(self, a) -> int:
        return a % 8

    def xor(self, a, b) -> int:
        return a ^ b

    def power(self, a: int) -> int:
        return pow(2, a)

    def division(self, a: int, b: int) -> int:
        return int(a / b)


def read_computer(input_path: Path) -> Computer:
    lines = input_path.read_text().splitlines()
    registry_a = int(lines[0].split()[-1])
    registry_b = int(lines[1].split()[-1])
    registry_c = int(lines[2].split()[-1])
    program = list(map(int, lines[4].split()[-1].split(",")))
    return Computer(registry_a=registry_a, registry_b=registry_b, registry_c=registry_c, program=program)


def main():
    computer = read_computer(Path("input.txt"))
    print(computer)
    computer.run_program()
    print(computer)
    computer.print_output()


if __name__ == '__main__':
    main()
