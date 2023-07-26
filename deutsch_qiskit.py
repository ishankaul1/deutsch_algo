from qiskit import QuantumCircuit, Aer, transpile, assemble, execute
from qiskit.visualization import plot_histogram

def deutsch_algorithm(oracle):
    # Create a quantum circuit with two qubits and two classical bits
    circuit = QuantumCircuit(2, 2)
    
    # Apply the Hadamard gate to both qubits
    circuit.h([0, 1])
    
    # Apply the oracle gate (the black box function)
    if oracle == "constant":
        pass  # Do nothing for a constant oracle
    elif oracle == "balanced":
        circuit.cx(0, 1)  # Apply CNOT gate for balanced oracle
    
    # Apply the Hadamard gate to the first qubit
    circuit.h(0)
    
    # Measure both qubits
    circuit.measure([0, 1], [0, 1])
    
    return circuit

def deusch_2(ora):
     # Create a quantum circuit with two qubits and two classical bits
    circuit = QuantumCircuit(2, 2)
    
    # Apply the Hadamard gate to both qubits
    circuit.h([0, 1])
    
    ora(circuit)
    
    # Apply the Hadamard gate to the first qubit
    circuit.h(0)
    
    # Measure both qubits
    circuit.measure([0, 1], [0, 1])
    
    return circuit

def constant_oracle(circuit):
    pass

def balanced_oracle(circuit):
     circuit.cx(0, 1)

# Run the algorithm with a constant oracle
#circuit_constant = deutsch_algorithm("constant")

circuit_constant = deusch_2(constant_oracle)
backend = Aer.get_backend('qasm_simulator')
job_constant = execute(circuit_constant, backend, shots=1024)
result_constant = job_constant.result()
counts_constant = result_constant.get_counts(circuit_constant)

# Run the algorithm with a balanced oracle
#circuit_balanced = deutsch_algorithm("balanced")
circuit_balanced = deusch_2(balanced_oracle)
job_balanced = execute(circuit_balanced, backend, shots=1024)
result_balanced = job_balanced.result()
counts_balanced = result_balanced.get_counts(circuit_balanced)

# Plot the results
print("Constant Oracle Results:", counts_constant)
print("Balanced Oracle Results:", counts_balanced)