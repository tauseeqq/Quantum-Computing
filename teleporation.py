from qiskit import QuantumCircuit, execute, Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

def create_entangled_pair(qc, qubit1, qubit2):
    qc.h(qubit1)
    qc.cx(qubit1, qubit2)

def bell_state_measurement(qc, qubit1, qubit2):
    qc.cx(qubit1, qubit2)
    qc.h(qubit1)
    qc.measure([qubit1, qubit2], [0, 1])

def apply_corrections(qc, qubit, classical_bits):
    qc.x(qubit).c_if(classical_bits, 1)  # Apply X gate if the first classical bit is 1
    qc.z(qubit).c_if(classical_bits, 2)  # Apply Z gate if the second classical bit is 1

def teleportation_circuit():
    # Create a quantum circuit with 3 qubits and 2 classical bits
    qc = QuantumCircuit(3, 2)
    
    # Prepare an arbitrary state on qubit 0 (Alice's qubit to be teleported)
    qc.u3(0.3, 0.2, 0.1, 0)  # Example arbitrary state preparation
    
    # Create entangled pair between qubits 1 and 2
    create_entangled_pair(qc, 1, 2)
    
    # Perform Bell-state measurement on qubits 0 and 1 (Alice's qubits)
    bell_state_measurement(qc, 0, 1)
    
    # Apply corrections on qubit 2 (Bob's qubit) based on classical bits
    apply_corrections(qc, 2, [0, 1])
    
    # Measure Bob's qubit to verify teleportation
    qc.measure(2, 0)
    
    return qc

# Create the teleportation circuit
qc = teleportation_circuit()

# Execute the circuit on the qasm simulator
backend = Aer.get_backend('qasm_simulator')
job = execute(qc, backend, shots=1024)
result = job.result()
counts = result.get_counts(qc)

# Display the results
print("\nTotal counts for each state:")
print(counts)
plot_histogram(counts)
plt.show()
