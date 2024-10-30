
from quantum_enhanced_lwe import EnhancedQuantumLWE

def basic_encryption_example():
    # Initialize the system
    lwe = EnhancedQuantumLWE()
    
    # Generate keypair
    public_key, private_key = lwe.gen_keypair()
    
    # Encrypt a message
    message = 1
    ciphertext = lwe.quantum_enhanced_encrypt(public_key, message)
    
    # Decrypt the message
    decrypted = lwe.decrypt(private_key, ciphertext)
    
    print(f"Original message: {message}")
    print(f"Decrypted message: {decrypted}")
    print(f"Success: {message == decrypted}")

if __name__ == "__main__":
    basic_encryption_example()
