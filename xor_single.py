import argparse
from pathlib import Path
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def load_rgb(path: Path) -> np.ndarray:
    img = Image.open(path).convert("RGB")
    arr = np.asarray(img, dtype=np.uint8)
    return arr

def save_rgb(arr: np.ndarray, path: Path) -> None:
    Image.fromarray(arr, mode="RGB").save(path)

def make_key(shape, seed: int) -> np.ndarray:
    # RGB için 0-255 arası uint8 değerler üret
    rng = np.random.default_rng(seed)
    h, w, c = shape
    key = rng.integers(0, 256, size=(h, w, c), dtype=np.uint8)
    return key

def xor_encrypt(img: np.ndarray, key: np.ndarray) -> np.ndarray:
    # XOR işlemi: uint8 seviyesinde piksel bazlı
    return np.bitwise_xor(img, key).astype(np.uint8)

def plot_hist(arr: np.ndarray, outpath: Path, title: str):
    # Tüm kanalları tek histogramda topluca gösterelim
    flat = arr.reshape(-1, 3)
    plt.figure()
    plt.hist(flat[:, 0], bins=256, range=(0, 255), alpha=0.5, label="R")
    plt.hist(flat[:, 1], bins=256, range=(0, 255), alpha=0.5, label="G")
    plt.hist(flat[:, 2], bins=256, range=(0, 255), alpha=0.5, label="B")
    plt.title(title)
    plt.xlabel("Piksel Değeri")
    plt.ylabel("Frekans")
    plt.legend()
    plt.tight_layout()
    plt.savefig(outpath)
    plt.close()

def main():
    parser = argparse.ArgumentParser(description="Seed tabanlı XOR görüntü şifreleme / çözme")
    parser.add_argument("--input", required=True, help="Girdi görüntü yolu (jpg/png vs.)")
    parser.add_argument("--seed", required=True, type=int, help="Rastgele tohum (seed) değeri")
    parser.add_argument("--outdir", required=True, help="Çıktı klasörü")
    parser.add_argument("--no-hist", action="store_true", help="Histogramları kaydetme")
    args = parser.parse_args()

    in_path = Path(args.input)
    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    # 1) Görüntüyü yükle (RGB)
    img = load_rgb(in_path)

    # 2) Seed ile aynı boyutta key üret
    key = make_key(img.shape, args.seed)

    # 3) XOR ile şifrele
    enc = xor_encrypt(img, key)

    # 4) Aynı key ile tekrar XOR → orijinale dönüş (doğrulama)
    dec = xor_encrypt(enc, key)

    # 5) Kaydet
    key_path = outdir / f"key_seed{args.seed}.png"
    enc_path = outdir / f"encrypted_seed{args.seed}.png"
    dec_path = outdir / f"decrypted_seed{args.seed}.png"

    save_rgb(key, key_path)
    save_rgb(enc, enc_path)
    save_rgb(dec, dec_path)

    # 6) İsteğe bağlı histogramlar
    if not args.no_hist:
        plot_hist(img, outdir / "hist_original.png", "Orijinal Histogram")
        plot_hist(enc, outdir / "hist_encrypted.png", "Şifreli Histogram")

    # 7) Konsol özeti
    print("=== XOR Görüntü Şifreleme Tamam ===")
    print(f"Girdi:        {in_path}")
    print(f"Seed:         {args.seed}")
    print(f"Anahtar:      {key_path}")
    print(f"Şifreli:      {enc_path}")
    print(f"Çözülmüş:     {dec_path}")
    if not args.no_hist:
        print(f"Histogramlar: {outdir / 'hist_original.png'} , {outdir / 'hist_encrypted.png'}")

if __name__ == "__main__":
    main()
