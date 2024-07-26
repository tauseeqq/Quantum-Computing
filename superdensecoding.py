from qiskit import QuantumCircuit
from qiskit import __all__
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

def prepare_bell_state():
    qc = QuantumCircuit(2, 2)
    qc.h(0)
    qc.cx(0, 1)
    return qc

def alice_encoding(qc, message):
    if message == '00':
        pass  # No gate
    elif message == '01':
        qc.x(0)  # Pauli X gatex
    elif message == '10':
        qc.z(0)  # Pauli Z gate
    elif message == '11':
        qc.z(0)
        qc.x(0)  # Z followed by X (or equivalently X followed by Z)
    return qc

def bob_decoding(qc):
    qc.cx(0, 1)
    qc.h(0)
    return qc

def main():
    
    while True:
        message = input("Enter the message to send (00, 01, 10, 11): ")
        if message not in ['00', '01', '10', '11']:
            print("Invalid input. Please enter one of the following: 00, 01, 10, 11")
            continue
        
        # Prepare Bell State
        qc = prepare_bell_state()
        
        # Alice Encoding
        qc = alice_encoding(qc, message)
        print(f"Alice encodes the message: {message}")
        
        # Bob Decoding
        qc = bob_decoding(qc)
        
        # Measurement
        count = qc.measure([0, 1], [0, 1])
        
        
        
        # Display results
        print("Notification: Message received by Bob.")
        decode = input("Bob, would you like to decode the message? (yes/no): ").strip().lower()
        
        if decode == 'yes':
            print(f"Classical bits received by Bob: {list(counts.keys())[0]}")
        else:
            print("Decoding skipped.")
        
        again = input("Would you like to send another message? (yes/no): ").strip().lower()
        if again != 'yes':
            break

if __name__ == "__main__":
    main()
