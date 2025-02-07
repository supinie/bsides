import matplotlib.pyplot as plt

# Data for encryption schemes
encryption_schemes = {
    "NTRUPrime": {"pub_size": 1505, "priv_size": 2254, "cipher_size": 1349, "gen_time": 1523540, "enc_time": 62704, "dec_time": 80654},
    "NTRU": {"pub_size": 1230, "priv_size": 1592, "cipher_size": 1230, "gen_time": 381476, "enc_time": 71238, "dec_time": 77848},
    "Kyber": {"pub_size": 1184, "priv_size": 2400, "cipher_size": 1088, "gen_time": 52732, "enc_time": 67624, "dec_time": 53156},
    "Saber": {"pub_size": 992, "priv_size": 1440, "cipher_size": 1088, "gen_time": 131000, "enc_time": 159000, "dec_time": 165000},
    "SIKE": {"pub_size": 462, "priv_size": 524, "cipher_size": 486, "gen_time": 160401000, "enc_time": 294628000, "dec_time": 296577000},
    "Classic McElise": {"pub_size": 1047319, "priv_size": 13948, "cipher_size": 194, "gen_time": 240328382, "enc_time": 147192, "dec_time": 287218}
}

# Data for digital signature schemes
signature_schemes = {
    "Dilithium": {"pub_size": 1952, "priv_size": 4032, "sig_size": 3293, "gen_time": 256403, "sign_time": 529106, "verify_time": 179424},
    "SPHINCS+": {"pub_size": 48, "priv_size": 96, "sig_size": 16224, "gen_time": 3220902, "sign_time": 89875552, "verify_time": 4783424},
    "Falcon": {"pub_size": 1793, "priv_size": 2305, "sig_size": 1280, "gen_time": 63135000, "sign_time": 789497, "verify_time": 168423},
    "Hawk": {"pub_size": 2329, "priv_size": 2561, "sig_size": 1195, "gen_time": 43660958, "sign_time": 85381, "verify_time": 255312},
    "SQISIGN": {"pub_size": 96, "priv_size": 1138, "sig_size": 263, "gen_time": 23734000000, "sign_time": 43760000000, "verify_time": 654000000},
    "Cross": {"pub_size": 56, "priv_size": 24, "sig_size": 17429, "gen_time": 70000, "sign_time": 18060000, "verify_time": 12240000},
    "FuLeeca": {"pub_size": 1982, "priv_size": 3964, "sig_size": 1620, "gen_time": 110918000, "sign_time": 2111156000, "verify_time": 2447000},
    "Mayo": {"pub_size": 2986, "priv_size": 32, "sig_size": 681, "gen_time": 574472, "sign_time": 1476585, "verify_time": 664631},
    "ALTEQ": {"pub_size": 31944, "priv_size": 24, "sig_size": 49000, "gen_time": 1964572, "sign_time": 36460660, "verify_time": 46054633}
}

# Compute memory and speed for each scheme
def compute_memory_and_speed(schemes):
    memory = []
    speed = []
    labels = []
    for scheme, values in schemes.items():
        total_size = sum([values[key] for key in values if 'size' in key])
        total_time = sum([values[key] for key in values if 'time' in key])
        memory.append(total_size)
        speed.append(total_time)
        labels.append(scheme)
    return memory, speed, labels

encryption_memory, encryption_speed, encryption_labels = compute_memory_and_speed(encryption_schemes)
signature_memory, signature_speed, signature_labels = compute_memory_and_speed(signature_schemes)

# Normalize data
def normalize(data):
    min_val = min(data)
    max_val = max(data)
    return [(val - min_val) / (max_val - min_val) for val in data]

normalized_encryption_memory = normalize(encryption_memory)
normalized_encryption_speed = normalize(encryption_speed)
normalized_signature_memory = normalize(signature_memory)
normalized_signature_speed = normalize(signature_speed)

# Plotting encryption schemes
plt.figure(figsize=(12, 8))

plt.scatter(normalized_encryption_speed, normalized_encryption_memory, color='blue', label='Encryption Schemes')
for i, label in enumerate(encryption_labels):
    plt.annotate(label, (normalized_encryption_speed[i], normalized_encryption_memory[i]))

plt.xlabel('Normalized Speed (sum of times)')
plt.ylabel('Normalized Memory (sum of sizes)')
plt.title('Memory vs Speed for Encryption Schemes')
plt.legend()
plt.grid(True)
plt.show()

# Plotting signature schemes
plt.figure(figsize=(12, 8))

plt.scatter(normalized_signature_speed, normalized_signature_memory, color='green', label='Signature Schemes')
for i, label in enumerate(signature_labels):
    plt.annotate(label, (normalized_signature_speed[i], normalized_signature_memory[i]))

plt.xlabel('Normalized Speed (sum of times)')
plt.ylabel('Normalized Memory (sum of sizes)')
plt.title('Memory vs Speed for Signature Schemes')
plt.legend()
plt.grid(True)
plt.show()
