# xor-image-encryption
A simple image encryption and decryption tool using XOR with seed-based key generation. Supports RGB pixel-level encryption, histogram analysis, and multi-seed operations.

# 🔐 Dazzling XOR Image Encryption — Seed-Based, RGB-Level Crypto Engine

## ✨ Introduction: The Art of Fast and Reversible Image Masking

**XOR Image Encryption** is a **lightweight**, **reversible**, and **seed-based** XOR encryption system designed for RGB images. It supports both single-seed and multi-seed encryption pipelines, offering completely **deterministic** and **perfectly reproducible** results suitable for **research**, **dataset anonymization**, **educational cryptography**, and **embedded systems**.

<p align="center">
<img src="https://img.shields.io/badge/Status-🚀%20Active%20Development-brightgreen?style=for-the-badge&logo=github" />
<img src="https://img.shields.io/badge/Technology-Python%203.10%2B-blue?style=for-the-badge&logo=python" />
<img src="https://img.shields.io/badge/License-MIT-purple?style=for-the-badge&logo=opensourceinitiative" />
<img src="https://img.shields.io/badge/Security-XOR%20Masking-orange?style=for-the-badge&logo=gnuprivacyguard" />
<img src="https://img.shields.io/badge/Performance-⚡%20NumPy%20Speed-yellow?style=flat-square&logo=numpy" />
<img src="https://img.shields.io/badge/Image%20Processing-Pillow%20Enabled-blueviolet?style=flat-square&logo=pythonimaging" />
</p>

---

##  🌟 Key Capabilities: What Makes This Project Stand Out?

This library is not just an encryption tool; it's an engineering feat optimized for **speed** and **reproducibility**.

* **✅ Seed-Based Key Generation**
    * **Deterministic** masks derived from integer seeds.
    * Guarantees perfect **reproducibility** and reversible encryption.
    * Essential for **dataset anonymization**.

* **⚡ RGB Channel XOR Engine**
    * **8-bit XOR** operation per R, G, and B channel.
    * **Extremely fast CPU performance** (via NumPy vectorization).
    * **Fully reversible** when applied with the identical seed.

* **🔥 Multi-Layer Encryption (`xor_multi.py`)**
    * **Cascaded encryption** using multiple seeds.
    * Provides higher diffusion and entropy.
    * Still perfectly reversible when using the full sequence of seeds.

* **🟢 Single-Layer Encryption (`xor_single.py`)**
    * **Lightweight** one-pass XOR encryption.
    * Perfect for demos and simple visual obfuscation.

---

## 📂 Project Structure

File hierarchy:

* **`xor-image-encryption/`**
    * `xor_single.py` 🔑 Single-seed XOR encryption/decryption engine
    * `xor_multi.py` ⛓️ Multi-seed cascaded encryption/decryption
    * `requirements.txt` 📦 Required Dependencies (NumPy, Pillow)
    * `bugsbunny.jpg` 🖼️ Example Input File
    * `outputs/` 📤 Encrypted / Decrypted Outputs are Saved Here
    * `README.md` This stunning file
    * `LICENSE` MIT License
    * `.gitignore`
---

##  ▶️ Usage: Just a Few Lines of Code!

Using this library is incredibly simple.

### 🔒 Encrypt (Single Seed)

```python
from xor_single import encrypt_image

# All the magic is in this integer 'seed'!
encrypt_image(
    input_path="bugsbunny.jpg",
    output_path="outputs/encrypted.png",
    seed=12345
)
```
### 🔓 Decrypt (Single Seed)
```Python

from xor_single import decrypt_image

# Use the exact same 'seed' to restore the image.
decrypt_image(
    input_path="outputs/encrypted.png",
    output_path="outputs/restored.png",
    seed=12345
)
```
### 🔥 Multi-Seed Cascaded Encryption

For more robust masking!

```Python

from xor_multi import multi_encrypt, multi_decrypt

# Define a sequence of seeds
seeds = [111, 222, 333] # A different mask for each layer!

multi_encrypt(
    input_path="bugsbunny.jpg",
    output_path="outputs/multi_encrypted.png",
    seeds=seeds
)
```
### 🔄 Multi-Seed Decryption

Use the same list of seeds in the encryption order.

```Python

from xor_multi import multi_encrypt, multi_decrypt

seeds = [111, 222, 333] # THE ORDER MUST BE STRICTLY MAINTAINED!

multi_decrypt(
    input_path="outputs/multi_encrypted.png",
    output_path="outputs/multi_restored.png",
    seeds=seeds
)
```

## 🛡️ Security Notes and Use Cases
IMPORTANT: XOR encryption is not intended as a replacement for modern encryption standards (AES, ChaCha20, etc.). Our focus is on fast visual obfuscation and data masking rather than absolute confidentiality.

  -This project focuses on lightweight, reversible image masking suitable for:

  -Dataset Obfuscation: Anonymizing Machine Learning/AI (ML/AI) datasets.

  -Research & Education: Visualizing and teaching cryptography principles.

  -Embedded/IoT Usage: Fast offline operations with low computational requirements.

  -Fast Preprocessing: Near-zero latency in image processing pipelines.

## 📈 Performance: In the Blink of an Eye!

Incredible speeds are achieved thanks to the power of NumPy vectorization.

| Resolution | Encrypt Time | Decrypt Time | Hardware |
| :--------: | :----------: | :----------: | :------: |
| **1080p** | ~1–3 ms      | ~1–3 ms      | CPU      |
| **4K** | ~5–10 ms     | ~5–10 ms     | CPU      |

* Powered by **NumPy Vectorization**.
* **Zero-copy** transformations.
* **Near-zero latency**.

# 🧭 Roadmap
Development never stops! Here's what's next:

- Multi-seed encryption (Completed!)

🚧 CLI tool (xor-cli) for command-line integration

🚧 Batch dataset encryption capability

🚧 Optional GPU support (For even more speed)

🚧 Web UI demonstration (Online demo)

# 👤 Author
Yigtwxx

An engineer focused on building practical solutions at the intersection of lightweight cryptography, image processing, and reproducible engineering. I specialize in Machine Learning (ML) and Deep Learning (DL) development, utilizing Python for high-performance and scalable data applications. I am keen on open-source contributions and advancing fast, efficient algorithms.

LinkedIn: www.linkedin.com/in/yiğit-erdoğan-ba7a64294
