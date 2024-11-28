import pytest
import numpy as np
from quantum_enhanced_lwe.core.quantum_enhanced_lwe import QuantumEnhancedLWE

@pytest.fixture
def lwe():
    return QuantumEnhancedLWE(n=256, q=4093, sigma=1.0)

def test_keypair_generation(lwe):
    pk, sk = lwe.gen_keypair()
    assert isinstance(pk, tuple)
    assert len(pk) == 2
    assert isinstance(sk, np.ndarray)
    assert sk.shape == (lwe.n,)

def test_encryption_decryption(lwe):
    pk, sk = lwe.gen_keypair()
    message = 1
    ciphertext = lwe.encrypt(pk, message)
    decrypted = lwe.decrypt(sk, ciphertext)
    assert decrypted == message

def test_quantum_enhanced_encryption(lwe):
    pk, sk = lwe.gen_keypair()
    message = 0
    ciphertext = lwe.quantum_enhanced_encrypt(pk, message)
    decrypted = lwe.decrypt(sk, ciphertext)
    assert decrypted == message