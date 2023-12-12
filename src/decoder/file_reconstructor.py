import click


def remade_file(binary_files_temp_folder, total_parts):
    """
    Reconstructs a file from its individual parts stored in a specified folder.

    This function first reads the metadata from the initial part to determine the output file's name.
    Then, it iterates through each part, appending its content to the output file.
    A progress bar is displayed during the reconstruction process.

    Args:
        binary_files_temp_folder (str): The folder where the binary parts are stored.
        total_parts (int): The total number of parts to reconstruct from.

    Returns:
        None: The function writes the reconstructed file to the path specified in the metadata file.
    """

    try:
        with open(f"{binary_files_temp_folder}/0.bin", 'rb') as metadata_file:
            output_file_path = 'new-' + metadata_file.read().decode('utf-8')
    except IOError as e:
        print(f"Error reading metadata file: {e}")
        return

    with open(output_file_path, 'wb') as output_file:
        with click.progressbar(length=int(total_parts - 1), label='Reconstructing original file') as bar:
            for i in range(total_parts):
                if i == 0:
                    continue

                chunk_file_name = f"{binary_files_temp_folder}/{i}.bin"

                try:
                    with open(chunk_file_name, 'rb') as chunk_file:
                        chunk_data = chunk_file.read()
                        output_file.write(chunk_data)
                        bar.update(1)
                except IOError as e:
                    print(f"Error reading file {chunk_file_name}: {e}")
                    break

    click.echo(f"Reconstruction completed. File saved to {output_file_path}")
