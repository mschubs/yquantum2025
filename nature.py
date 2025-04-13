import numpy as np
import matplotlib.pyplot as plt
import qutip as qt

# Parameters
N = 33  # number of vertices on the cycle
tau_values = { '0': 0, '1': 2 }  # liveliness parameters for binary bits (example)
coin_dim = 3

# Initial state: position and coin state (uniform superposition over coin states)
pos0 = 0
coin0 = (1/np.sqrt(3)) * (qt.basis(coin_dim, 0) + qt.basis(coin_dim, 1) + qt.basis(coin_dim, 2))
psi0 = qt.tensor(qt.basis(N, pos0), coin0)

def shift_operator(N, tau):
    S = sum(
        qt.tensor(qt.basis(N, (x+1)%N)*qt.basis(N, x).dag(), qt.basis(coin_dim, 0)*qt.basis(coin_dim,0).dag()) +
        qt.tensor(qt.basis(N, (x-1)%N)*qt.basis(N, x).dag(), qt.basis(coin_dim, 1)*qt.basis(coin_dim,1).dag()) +
        qt.tensor(qt.basis(N, (x+tau)%N)*qt.basis(N, x).dag(), qt.basis(coin_dim, 2)*qt.basis(coin_dim,2).dag())
        for x in range(N)
    )
    return S

G = (2/3)*np.ones((coin_dim, coin_dim)) - np.eye(coin_dim)
coin_operator = qt.tensor(qt.qeye(N), qt.Qobj(G))

def evolution_operator(N, bit, tau_values):
    tau = tau_values[bit]
    return shift_operator(N, tau) * coin_operator

def controlled_quantum_walk_hash(msg, N, psi0, tau_values):
    psi = psi0
    for bit in msg:
        U = evolution_operator(N, bit, tau_values)
        psi = U * psi
    return psi

def generate_hash(psi_final, N, s=8, l=10):
    prob_dist = np.abs(psi_final.full())**2
    prob_pos = np.sum(prob_dist.reshape(N, coin_dim), axis=1).flatten()
    hash_bits = ''
    for p in prob_pos:
        scaled_p = int((p * 10**l) % (2**s))
        hash_bits += format(scaled_p, '0' + str(s) + 'b')
    return hash_bits

# Example message

def to_binary(text):
    return "".join(format(ord(char), "08b") for char in text)

def hash(text, live_0 = 0, live_1 = 2):
    message = to_binary(text)
    print(message)
    global tau_values
    tau_values = { "0": live_0, "1": live_1 }
    # Initial state defined previously (psi0)
    psi_final = controlled_quantum_walk_hash(message, N, psi0, tau_values)
    print(psi_final)
    # Generate hash value (with parameters s=8, l=10 as an example)
    hash_value = generate_hash(psi_final, N, s=8, l=10)
    print(hash_value)
    #print("Hash value:", hash_value)
    return hex(int(hash_value, 2))[2:]