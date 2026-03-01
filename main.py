import numpy as np

# Parameters
n = 4
q = 97


def generate_keys():
    A = np.random.randint(0, q, (n, n))
    s = np.random.randint(0, q, (n, 1))
    e = np.random.randint(0, q, (n, 1))

    b = (A @ s + e) % q

    public_key = (A, b)
    private_key = s

    return public_key, private_key


def encrypt(public_key, message):
    A, b = public_key

    r = np.random.randint(0, q, (n, 1))
    e1 = np.random.randint(0, q, (n, 1))
    e2 = np.random.randint(0, q, (1, 1))

    u = (A.T @ r + e1) % q
    v = (b.T @ r + e2 + message) % q

    return (u, v)


def decrypt(private_key, ciphertext):
    u, v = ciphertext
    s = private_key

    recovered = (v - s.T @ u) % q
    return int(recovered[0][0])


def main():
    print("=== Post-Quantum Lattice Encryption Demo ===")

    public_key, private_key = generate_keys()

    message = 15
    print("Original Message:", message)

    ciphertext = encrypt(public_key, message)
    print("Ciphertext:", ciphertext)

    decrypted = decrypt(private_key, ciphertext)
    print("Decrypted Message:", decrypted)


if __name__ == "__main__":
    main()
