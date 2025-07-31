# Importing the required library
import qrcode

# Prompting the user to enter their UPI ID
upi_id = input("Enter your UPI ID = ")

# Constructing UPI payment URLs for different apps (PhonePe, Paytm, Google Pay)
# 'pa' is the payee address (UPI ID), 'pn' is the payee name, 'mc' is a merchant code (optional)
phonepe_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
google_pay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

# Generating QR codes for each UPI URL
phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

# Saving the generated QR codes as image files
phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('paytm_qr.png')
google_pay_qr.save('google_pay_qr.png')

# Displaying the generated QR codes (opens the image in the default viewer)
phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()
