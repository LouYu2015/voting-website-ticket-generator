# Page dimension (e.g. A4, Letter...)
format = "A3"
orientation = "L"

# Number of tickets
row_per_page = 5
column_per_page = 3
number_of_pages = 10

# Background image
bg_path = "~/Documents/program/2021/ticket_generator/semifinal_front.png"
bg_width = 130

# Folder used to store QR codes
temp_folder = "/media/ramdisk/tmp"

# URL format string
# "{serial}" will be replaced with the serial number
url = "https://vote.cssauw.org/qr_code/{serial}"

# Position of the QR code on the background image, in pixels
qr_x = 2004
qr_y = 581
qr_width = 2350 - qr_x

# QR code format
background_color = (255, 255, 255)

# Serial number format
font = "Arial"
font_style = "B"
font_size = 4

# Position of the serial number on the background image, in pixels
serial_x = 2105
serial_y = 920

# File path for output

# PDF of tickets
tickets_pdf_file = "/media/ramdisk/test.pdf"
# List of serial numbers
serial_number_list_file = "/media/ramdisk/serial_numbers.txt"
