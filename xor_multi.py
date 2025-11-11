import argparse
from pathlib import Path
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def load_rgb(path: Path) -> np.ndarray:
    img = Image.open(path).convert("RGB")
    return np.asarray(img, dtype=np.uint8)

def save_rgb(arr: np.ndarray, path: Path):
    Image.fromarray(arr, mode="RGB").save(path)

def make_key(shape, seed: int) -> np.ndarray:
    rng = np.random.default_rng(seed)
    h, w, c = shape
    return rng.integers(0, 256, size=(h, w, c), dtype=np.uint8)

def xor_encrypt(img: np.ndarray, key: np.ndarray) -> np.ndarray:
    return np.bitwise_xor(img, key).astype(np.uint8)

def plot_hist(arr: np.ndarray, outpath: Path, title: str):
    flat = arr.reshape(-1, 3)
    plt.figure()
    plt.hist(flat[:, 0], bins=256, range=(0,255), alpha=0.5, label="R")
    plt.hist(flat[:, 1], bins=256, range=(0,255), alpha=0.5, label="G")
    plt.hist(flat[:, 2], bins=256, range=(0,255), alpha=0.5, label="B")
    plt.title(title)
    plt.legend()
    plt.tight_layout()
    plt.savefig(outpath)
    plt.close()

def process_seed(img, outdir: Path, seed: int, hist: bool):
    key = make_key(img.shape, seed)
    enc = xor_encrypt(img, key)
    dec = xor_encrypt(enc, key)

    save_rgb(key, outdir / f"key_seed{seed}.png")
    save_rgb(enc, outdir / f"encrypted_seed{seed}.png")
    save_rgb(dec, outdir / f"decrypted_seed{seed}.png")

    if hist:
        plot_hist(img, outdir / f"hist_original_seed{seed}.png", f"Orijinal Histogram (seed={seed})")
        plot_hist(enc, outdir / f"hist_encrypted_seed{seed}.png", f"Şifreli Histogram (seed={seed})")

    print(f"[OK] seed={seed} → key/encrypted/decrypted dosyaları kaydedildi.")

def main():
    parser = argparse.ArgumentParser(description="Seed tabanlı XOR görüntü şifreleme / çözme (çoklu seed)")
    parser.add_argument("--input", required=True, help="Girdi görüntü yolu (jpg/png)")
    parser.add_argument("--seeds", required=True, nargs="+", type=int, help="Seed değerleri (birden fazla girilebilir)")
    parser.add_argument("--outdir", required=True, help="Çıktı klasörü")
    parser.add_argument("--no-hist", action="store_true", help="Histogramları kaydetme")
    args = parser.parse_args()

    in_path = Path(args.input)
    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    img = load_rgb(in_path)

    for seed in args.seeds:
        process_seed(img, outdir, seed, hist=not args.no_hist)

if __name__ == "__main__":
    main()
