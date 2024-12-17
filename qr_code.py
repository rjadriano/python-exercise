# https://pypi.org/project/qrcode/
import qrcode

qr_data =  input('Enter the text or URL for the QR code: ').strip()
qr = qrcode.make(qr_data)

file_name_input = input('Enter the filename: ').strip()
file_name = file_name_input + '.png'

qr.save(file_name)
print(f'QR code save as {file_name}')