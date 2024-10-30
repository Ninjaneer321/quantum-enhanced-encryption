
import numpy as np
import time
from tqdm import tqdm

class GoldenHarmonicLWE:
    def __init__(self, n=256, q=4093, sigma=1.0, key_lifetime=3600):
        self.n = n
        self.q = q
        self.sigma = sigma
        self.phi = (1 + np.sqrt(5)) / 2  # Golden ratio
        self.base = 32  # Increased base for better granularity
        self.key_lifetime = key_lifetime
        self.generate_new_key()

    def generate_new_key(self):
        self.key = np.random.randint(0, self.q, size=self.n)
        self.key_generated_time = time.time()

    def is_key_valid(self):
        return time.time() - self.key_generated_time < self.key_lifetime

    def get_encryption_frequency(self):
        if not self.is_key_valid():
            self.generate_new_key()
        return (np.sum(self.key) % self.q) / self.q * 10 + self.phi  # Combine with golden ratio

    def generate_quantum_signal(self, message):
        t = np.linspace(0, 1, len(message))
        freq = self.get_encryption_frequency()
        return np.sin(2 * np.pi * freq * t) * message

    def encode_message(self, message):
        quantum_signal = self.generate_quantum_signal(message)
        encoded = np.rint((quantum_signal + 1) * (self.base - 1) / 2).astype(int)
        return encoded

    def decode_message(self, encoded):
        if not self.is_key_valid():
            raise ValueError("Decryption key has expired")
        t = np.linspace(0, 1, len(encoded))
        freq = self.get_encryption_frequency()
        carrier = np.sin(2 * np.pi * freq * t)
        decoded_signal = 2 * encoded.astype(float) / (self.base - 1) - 1
        return (decoded_signal * carrier > 0).astype(int)

def run_test_suite(message_lengths, num_trials):
    results = []
    for length in tqdm(message_lengths, desc="Testing message lengths"):
        success_rates = []
        for _ in range(num_trials):
            ghl = GoldenHarmonicLWE(key_lifetime=10)
            test_message = np.random.randint(0, 2, length)
            encoded = ghl.encode_message(test_message)
            decoded = ghl.decode_message(encoded)
            success_rate = np.mean(test_message == decoded) * 100
            success_rates.append(success_rate)
        avg_success_rate = np.mean(success_rates)
        std_success_rate = np.std(success_rates)
        results.append((length, avg_success_rate, std_success_rate))
    return results

if __name__ == "__main__":
    # Run the test suite
    message_lengths = [100, 500, 1000, 5000, 10000]
    num_trials = 50

    print("Running Golden Harmonic LWE Test Suite...")
    test_results = run_test_suite(message_lengths, num_trials)

    print("
Test Results:")
    print("Message Length | Avg Success Rate (%) | Std Dev")
    print("-------------------------------------------------")
    for length, avg_rate, std_rate in test_results:
        print(f"{length:14d} | {avg_rate:19.2f} | {std_rate:7.2f}")

    print("
Done")
