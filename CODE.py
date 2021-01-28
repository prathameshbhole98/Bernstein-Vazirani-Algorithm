from qiskit import *
%matplotlib inline
from qiskit.tools.visualization import plot_histogram
s = 101011 #random number, you can insert in any number here for the program to guess
qc = QuantumCircuit(6+1, 6)
qc.h([0,1,2,3,4,5])
qc.x(6)
qc.h(6)
qc.barrier()
qc.cx(5, 6)
qc.cx(3, 6)
qc.cx(1, 6)
qc.cx(0, 6)
qc.barrier()
qc.h([0,1,2,3,4,5])
qc.measure([0,1,2,3,4,5], [0,1,2,3,4,5])
qc.draw('mpl')
simulator = Aer.get_backend('qasm_simulator')
result = execute(qc, backend = simulator, shots = 1).result()
counts = result.get_counts()
print(counts)
