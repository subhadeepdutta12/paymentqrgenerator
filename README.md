# Payment QR Code Generator 🧾

This simple Python script allows you to generate UPI payment QR codes for multiple platforms — PhonePe, Paytm, and Google Pay — using just your UPI ID.

## 🚀 Features

- Accepts any valid UPI ID
- Generates separate QR codes for:
  - 📱 PhonePe
  - 💳 Paytm
  - 🏦 Google Pay
- Saves each QR as a `.png` image
- Opens the QR code in your default image viewer automatically

## 🛠 Requirements

- Python 3.x
- `qrcode` module

Install the required module using pip:
```bash
pip install qrcode[pil]
```

## 🛆 How to Use

1. **Clone the repository**
```bash
git clone https://github.com/subhadeepdutta12/paymentqrgenerator.git
cd paymentqrgenerator
```

2. **Run the script**
```bash
python payment_qr_generator.py
```

3. **Enter your UPI ID**
You'll be prompted:
```
Enter your UPI ID =
```

4. **Result**
- You will get 3 PNG files: `phonepe_qr.png`, `paytm_qr.png`, and `google_pay_qr.png`
- They will also open in your default image viewer

## 📝 Example

If you enter:
```
Enter your UPI ID = example@upi
```

The script will generate UPI QR codes using:
```
upi://pay?pa=example@upi&pn=Recipient%20Name&mc=1234
```

## 📄 License

This project is open-source and free to use.

---

> Created by [Subhadeep Dutta](https://github.com/subhadeepdutta12)
