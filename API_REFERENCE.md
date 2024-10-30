
# API Reference

## QuantumEnhancedLWE Class

### Methods

#### `__init__(self, n=256, q=4093, sigma=1.0)`
Initializes the Quantum Enhanced LWE system with specified parameters.
- `n`: Dimension of the lattice (default: 256)
- `q`: Modulus for the lattice (default: 4093)
- `sigma`: Standard deviation for error sampling (default: 1.0)

#### `gen_keypair(self)`
Generates a public and private key pair for encryption and decryption.
- Returns: Tuple containing the public key and private key.

#### `encrypt(self, pk, m)`
Encrypts a message using the public key.
- `pk`: Public key
- `m`: Message to encrypt (0 or 1)
- Returns: Ciphertext as a tuple of (a, c)

#### `decrypt(self, sk, ct)`
Decrypts a ciphertext using the private key.
- `sk`: Private key
- `ct`: Ciphertext to decrypt
- Returns: Decrypted message (0 or 1)

#### `quantum_enhanced_encrypt(self, pk, m)`
Encrypts a message using quantum-enhanced techniques.
- `pk`: Public key
- `m`: Message to encrypt (0 or 1)
- Returns: Ciphertext as a tuple of (a, c)

## QuantumResonanceCircuit Class

### Methods

#### `__init__(self, resonance_freq=4.40e9, coupling_strength=0.1)`
Initializes the quantum resonance circuit with specified parameters.
- `resonance_freq`: Resonance frequency (default: 4.40 GHz)
- `coupling_strength`: Coupling strength between qubits (default: 0.1)

#### `initialize_state(self)`
Initializes the quantum state for the circuit.
- Returns: Initial quantum state as a complex numpy array.

#### `get_hamiltonian(self)`
Calculates the Hamiltonian matrix for the circuit.
- Returns: Hamiltonian matrix as a complex numpy array.

#### `evolve_state(self, state, time)`
Evolves the quantum state over time using the Hamiltonian.
- `state`: Initial quantum state
- `time`: Time duration for evolution
- Returns: Evolved quantum state as a complex numpy array.

