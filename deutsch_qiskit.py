from qiskit import QuantumCircuit, Aer, transpile, assemble, execute
from qiskit.visualization import plot_histogram

def deusch_2(ora):
     # Create a basic quantum circuit needed for Deutch's Algorithm. 2 qubits, 1 classical bits
    circuit = QuantumCircuit(2, 1)
    
    #  Apply a Pauli-X gate on the second qubit. Pauli-X gates effectively flip the state of the qubit.
    circuit.x(1)
    
    # Apply the Hadamard gate to both qubits. Puts both gates in a superposition of states.
    circuit.h([0, 1])
    
    # Call the 'oracle function' that is passed into deutsch's algorithm as a parameter.
    ora(circuit)
    
    # Apply hadamard gate to qubits again. This puts them back into a superposition of states and prepares them for measurement.
    circuit.h([0, 1])
    
    # Measure the circuit's first qubit and put it into the classical bit
    circuit.measure(0, 0)
    
    return circuit

def constant_oracle(circuit):
    pass

#Balanced oracle runs a controlled not gate on the oracle. This gate will flip the second qubit, if first qubit is in a state of |1>.
#This is considered 'balanced' because it will flip the state of qubit 1 depending on the state of qubit 0.
def balanced_oracle(circuit):
     circuit.cx(0, 1)

#TODO - edit this code a bit

# Run the algorithm with a constant oracle (no-op) on the qasm quantum simulator
circuit_constant = deusch_2(constant_oracle)
backend = Aer.get_backend('qasm_simulator')
job_constant = execute(circuit_constant, backend, shots=1024)
result_constant = job_constant.result()
counts_constant = result_constant.get_counts(circuit_constant)

# Run the algorithm with a balanced oracle. In this case, our balanced oracle is a cnot gate
circuit_balanced = deusch_2(balanced_oracle)
job_balanced = execute(circuit_balanced, backend, shots=1024)
result_balanced = job_balanced.result()
counts_balanced = result_balanced.get_counts(circuit_balanced)

# Plot the results
print("Constant Oracle Results:", counts_constant)
print("Balanced Oracle Results:", counts_balanced)