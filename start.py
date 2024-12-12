import numpy as np
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# Number of qubits
num_qubits = 50

# Generate random bits and bases for Alice
alice_bits = np.random.randint(2, size=num_qubits)
alice_bases = np.random.randint(2, size=num_qubits)
bob_bases = np.random.randint(2, size=num_qubits)

qc = QuantumCircuit(num_qubits, num_qubits)

# Alice encodes qubits
for i in range(num_qubits):
    bit = alice_bits[i]
    basis = alice_bases[i]
    if basis == 0:  # Z-basis
        if bit == 1:
            qc.x(i)
    else:  # X-basis
        qc.h(i)
        if bit == 1:
            qc.z(i)

# Bob measures
for i in range(num_qubits):
    if bob_bases[i] == 1:  # X-basis measurement
        qc.h(i)

qc.measure(range(num_qubits), range(num_qubits))

# Use AerSimulator directly
simulator = AerSimulator()
result = simulator.run(qc, shots=1).result()  # No transpile step
counts = result.get_counts()

measured_key = list(counts.keys())[0]
bob_results = measured_key[::-1]

print("Alice's Bits:    ", alice_bits)
print("Alice's Bases:   ", alice_bases)
print("Bob's Bases:     ", bob_bases)
print("Bob's Results:   ", bob_results)
