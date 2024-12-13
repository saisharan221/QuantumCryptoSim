# examples/run_bb84.py
import numpy as np
from quantumcryptosim.bb84 import BB84
from quantumcryptosim.utils import sift_key
from quantumcryptosim.eavesdrop import Eavesdropper
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

def main():
    num_qubits = 50
    protocol = BB84(num_qubits=num_qubits)
    alice_bits = protocol.alice_bits
    alice_bases = protocol.alice_bases
    bob_bases = protocol.bob_bases

    # Introduce Eve with a 100% intercept probability for demonstration
    eve = Eavesdropper(num_qubits=num_qubits, eavesdrop_probability=1.0)
    # Eve intercepts and resends
    eve_resend_qc = eve.intercept_and_resend(alice_bits, alice_bases)

    # Now Bob measures the qubits he receives from Eve
    # Bob's measurement (just like in BB84 run_simulation, but now on eve_resend_qc)
    for i in range(num_qubits):
        if bob_bases[i] == 1:
            eve_resend_qc.h(i)
    eve_resend_qc.measure(range(num_qubits), range(num_qubits))

    simulator = AerSimulator()
    result = simulator.run(eve_resend_qc, shots=1).result()
    counts = result.get_counts(eve_resend_qc)
    measured_key = list(counts.keys())[0]
    bob_results = measured_key[::-1]

    print("Alice's Bits:  ", alice_bits)
    print("Alice's Bases: ", alice_bases)
    print("Bob's Bases:   ", bob_bases)
    print("Bob's Results: ", bob_results)

    # Sift the key
    alice_sifted, bob_sifted, indices = sift_key(
        alice_bases, bob_bases, alice_bits, bob_results
    )

    print("Sifted Alice Key:", alice_sifted)
    print("Sifted Bob Key:  ", bob_sifted)
    # The difference between alice_sifted and bob_sifted will show the presence of Eve (high QBER).

if __name__ == "__main__":
    main()
