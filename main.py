import os

from fpdf import FPDF
import qrcode
import config
import serial_number


def main():
    pdf = FPDF(format=config.format, unit="mm", orientation=config.orientation)

    # Load background image
    bg = pdf._parsepng(config.bg_path)
    bg_width_pixels = bg["w"]
    bg_height_pixels = bg["h"]
    print(f"Background size: {bg_width_pixels} * {bg_height_pixels}")

    # Calculate dimensions
    scale = config.bg_width / bg_width_pixels
    bg_width = config.bg_width
    bg_height = bg_height_pixels * scale

    padding_top = (pdf.h - config.row_per_page * bg_height) / 2
    padding_left = (pdf.w - config.column_per_page * bg_width) / 2

    # Print tickets
    for page in range(config.number_of_pages):
        pdf.add_page()
        for row in range(config.row_per_page):
            for column in range(config.column_per_page):
                x = padding_left + column * bg_width
                y = padding_top + row * bg_height

                # Print background image
                pdf.image(config.bg_path, x, y, bg_width, bg_height)

                # Generate QR code
                serial = serial_number.generate_serial_number()
                url = config.url.format(serial=serial)
                qr_path = os.path.join(config.temp_folder, f"{serial}.png")
                qr = qrcode.QRCode()
                qr.add_data(url)
                qr.make_image(back_color=config.background_color).save(qr_path)

                # Print QR code
                qr_x = x + config.qr_x * scale
                qr_y = y + config.qr_y * scale
                pdf.image(qr_path, qr_x, qr_y, config.qr_width * scale)

                # Print serial number
                pdf.set_x(x + config.serial_x * scale)
                pdf.set_y(y + config.serial_y * scale)
                pdf.set_font(config.font, config.font_style, config.font_size)
                pdf.text(x + config.serial_x * scale,
                         y + config.serial_y * scale,
                         serial_number.format(serial))

    pdf.output(config.tickets_pdf_file, "F")
    serial_number.save(config.serial_number_list_file)


if __name__ == '__main__':
    main()
