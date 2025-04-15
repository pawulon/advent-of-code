from pathlib import Path

from day_07_1 import Circuit, read_circuit, connect_wires

def main():
    circuit = read_circuit(Path("input.txt"))
    connected_circuit = connect_wires(circuit)
    circuit['b'] = connected_circuit['a']
    new_circuit = connect_wires(circuit)
    print(new_circuit['a'])



if __name__ == '__main__':
    main()
