
from quantum_enhanced_lwe import EnhancedQuantumLWE
import numpy as np

def batch_encryption_example():
    # Initialize the system
    lwe = EnhancedQuantumLWE()
    
    # Generate keypair
    public_key, private_key = lwe.gen_keypair()
    
    # Create batch of messages
    messages = np.random.randint(0, 2, 10)
    
    # Encrypt and decrypt batch
    ciphertexts = []
    decrypted_messages = []
    
    for msg in messages:
        # Encrypt
        ct = lwe.quantum_enhanced_encrypt(public_key, msg)
        ciphertexts.append(ct)
        
        # Decrypt
        dec = lwe.decrypt(private_key, ct)
        decrypted_messages.append(dec)
    
    # Verify results
    success_rate = sum(m == d for m, d in zip(messages, decrypted_messages)) / len(messages)
    print(f"Batch encryption/decryption success rate: {success_rate * 100}%")

if __name__ == "__main__":
    batch_encryption_example()
