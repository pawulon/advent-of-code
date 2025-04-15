from pathlib import Path

Circuit = dict[str, str]


def read_circuit(input_path: Path) -> Circuit:
    input_lines = input_path.read_text().split('\n')
    circuit: Circuit = {}
    for line in input_lines:
        left, right = line.split("->")
        circuit[right.strip()] = left.strip()
    return circuit

def connect_wires(circuit: Circuit) -> Circuit:
    evaluated_circuit: Circuit = {}
    repeat = True
    while repeat:
        repeat = False
        for wire, wire_value in circuit.items():
            try:
                if 'AND' in wire_value:
                    evaluated_circuit[wire] = str(and_gate_output(wire_value, evaluated_circuit))
                elif 'OR' in wire_value:
                    evaluated_circuit[wire] = str(or_gate_output(wire_value, evaluated_circuit))
                elif 'LSHIFT' in wire_value:
                    evaluated_circuit[wire] = str(lshift_gate_output(wire_value, evaluated_circuit))
                elif 'RSHIFT' in wire_value:
                    evaluated_circuit[wire] = str(rshift_gate_output(wire_value, evaluated_circuit))
                elif 'NOT' in wire_value:
                    evaluated_circuit[wire] = str(not_gate_output(wire_value, evaluated_circuit))
                else:
                    wire_value = get_real_value(wire_value, evaluated_circuit)
                    evaluated_circuit[wire] = wire_value
            except KeyError:
                repeat = True
                continue
    return evaluated_circuit

def and_gate_output(and_gate: str, evaluated_circuit: Circuit) -> int:
    a, _, b = and_gate.split()
    a = get_real_value(a, evaluated_circuit)
    b = get_real_value(b, evaluated_circuit)
    return int(a) & int(b)

def or_gate_output(or_gate: str, evaluated_circuit: Circuit) -> int:
    a, _, b = or_gate.split()
    a = get_real_value(a, evaluated_circuit)
    b = get_real_value(b, evaluated_circuit)
    return int(a) | int(b)

def lshift_gate_output(left_shift: str, evaluated_circuit: Circuit) -> int:
    a, _, b = left_shift.split()
    a = get_real_value(a, evaluated_circuit)
    b = get_real_value(b, evaluated_circuit)
    return int(a) << int(b)

def rshift_gate_output(right_shift: str, evaluated_circuit: Circuit) -> int:
    a, _, b = right_shift.split()
    a = get_real_value(a, evaluated_circuit)
    b = get_real_value(b, evaluated_circuit)
    return int(a) >> int(b)

def not_gate_output(not_gate: str, evaluated_circuit: Circuit) -> int:
    _, a = not_gate.split()
    a = get_real_value(a, evaluated_circuit)
    return ~int(a) & 0xFFFF

def get_real_value(value: str, evaluated_circuit: Circuit) -> str:
    try:
        int(value)
        return value
    except ValueError:
        return evaluated_circuit[value]

def main():
    circuit = read_circuit(Path("input.txt"))
    print(connect_wires(circuit))


if __name__ == '__main__':
    main()
