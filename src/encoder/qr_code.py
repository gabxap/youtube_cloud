import os
import click
import segno


def generate_qrs(temp_folder_location, file_location, file_name):
    """
    Generates a series of QR codes for the contents of a given file and a QR code for the file name.

    This function first creates a QR code for the file name and then splits the file into chunks,
    generating a QR code for each chunk. The QR codes are saved as PNG files in the specified temporary folder.
    A progress bar is displayed to show the progress of QR code generation.

    Args:
        temp_folder_location (str): Path to the folder where the QR codes will be saved.
        file_location (str): Path to the file that needs to be converted into QR codes.
        file_name (str): Name of the file, which is also converted into a QR code.
    """
    output_path = os.path.join(temp_folder_location, "0.png")
    generate_qr(file_name, output_path)

    chunk_size = 2953
    qr_count = 1
    with open(file_location, 'rb') as file:
        file_size = os.path.getsize(file_location)
        total_chunks = (file_size // chunk_size) + (1 if file_size % chunk_size else 0)

        with click.progressbar(length=total_chunks, label='Generating QR Codes') as bar:
            while True:
                chunk = file.read(chunk_size)
                if not chunk:
                    break

                output_path = os.path.join(temp_folder_location, f"{qr_count}.png")
                generate_qr(chunk, output_path)
                qr_count += 1

                bar.update(1)


def generate_qr(data, file_path):
    """
    Generates a QR code from the given data and saves it as a PNG file.

    Args:
        data (bytes): The data to be encoded in the QR code.
        file_path (str): The file path where the QR code image will be saved.
    """
    qr = segno.make(data, version=40)
    qr.save(file_path, scale=5, border=3)
