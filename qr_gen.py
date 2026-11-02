import qrcode


def main():
    data = input("Enter a link or text: ").strip()
    if not data:
        print("The link or text cannot be empty.")
        return

    filename = input("Enter a file name (for example, code.png): ").strip()
    if not filename:
        print("The file name cannot be empty.")
        return

    qr = qrcode.QRCode()
    qr.add_data(data)
    qr.make(fit=True)
    image = qr.make_image()
    image.save(filename)
    print(f"QR code saved as {filename}.")


if __name__ == "__main__":
    main()