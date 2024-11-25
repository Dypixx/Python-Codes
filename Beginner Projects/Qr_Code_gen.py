# pip install qrcode (Must Install)

import qrcode as Q
def generate_qr_code():
    print("============================")
    print("     Created By @Dypixx")
    print("============================\n")
    print("1. Text to QR Code")
    print("2. URL to QR Code")
    
    data = input("Choose (1/2): ").strip()
    if data == '1':
        data = input("Enter text: ").strip()
        file_name = input("File name (no extension): ").strip() + ".png"
    elif data == '2':
        data = input("Enter URL: ").strip()
        file_name = input("File name (no extension): ").strip() + ".png"
    else:
        print("Invalid Input..!")
        return
    
    qr = Q.QRCode(version=1, error_correction=Q.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_name)
    print(f"QR Code saved as '{file_name}'!")

if __name__ == "__main__":
    generate_qr_code()
