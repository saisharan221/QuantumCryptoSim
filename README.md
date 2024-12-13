
# QuantumCryptoSim

**QuantumCryptoSim** is a Python-based simulation toolkit demonstrating the BB84 quantum key distribution (QKD) protocol using Qiskit and Aer simulators. It allows you to:

- Generate random quantum bits (qubits) prepared in different bases.
- Simulate the quantum transmission of these qubits.
- Measure and sift the resulting keys to understand how secure quantum key distribution works.

## Features

- **BB84 Simulation**: Encode and measure qubits in random bases to establish a secret key.
- **Key Sifting**: Compare bases used by sender (Alice) and receiver (Bob) to extract a shared key.
- **Extensible Design**: Future support for eavesdropping simulations, error correction, and privacy amplification.

## Getting Started

1. Clone this repository:
   ```bash
   git clone https://github.com/saisharan221/QuantumCryptoSim.git
   cd QuantumCryptoSim
