import numpy as np
from qiskit import (
    QuantumCircuit,  # operazioni quantistiche
    execute,  # esecuzione
    Aer)  # simulatore
from qiskit.visualization import plot_histogram

# per visualizzare in SciView di Pycharm è necessario aggiungere:
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # scelgo il qasm_simulator
    simulator = Aer.get_backend('qasm_simulator')

    # Creo un Quantum Circuit con q=2 qubit e b=2 bit classici
    # inizializzati entrambi a zero
    circuit = QuantumCircuit(2, 2)

    # creiamo un circuito che genera una coppia di Bell:

    # Aggiungo una gate H sul qubit all'indice 0, creando una superposizione
    circuit.h(0)

    # Aggiungo una gate cx (CNOT) con il qubit controllore all'indice 0
    # ed il qubit target all'indice 1, entanglandoli
    circuit.cx(0, 1)

    # Passo l'intero registro quantistico e quello classico per poterli misurare
    # ovviamente all'i-esimo bit corrisponderà una misura sull'i-esimo bit classico
    circuit.measure([0, 1], [0, 1])

    # eseguo il circuito passando esso, il simulatore ed il numero di campioni
    job = execute(circuit, simulator, shots=1000)

    # prendiamo i risultati di misura dal circuito
    result = job.result()

    # stampiamo il conteggio dal risultato
    counts = result.get_counts(circuit)
    print("\nTotal count for 00 and 11 are:", counts)

    # Stampo il circuito
    print(circuit)
    """ 
    se mi trovassi su jupyter dovrei semplicemente scrivere in questo modo:
    circuit.draw()
    in realtà se modifico '~/.qiskit/settings.conf' :
    [default]
    circuit_drawer = mpl
    
    posso modificare il drawer con text, mpl, latex, e latex_source.
    
    con la print lo stampo in unicode su terminale
    """

    # plottiamo l'istogramma della probabilità di misurare 00 ed 11
    plot_histogram(counts)

    # per visualizzare in SciView di Pycharm è necessario aggiungere:
    plt.show()
