import os
import shutil
import subprocess
import tempfile


def create_temp_folder():
    """
    Creates a temporary directory and returns its path.

    Returns:
        str: The path to the newly created temporary directory.
    """
    temp_dir = tempfile.mkdtemp()
    return temp_dir


def remove_temp_folder(folder_address):
    """
    Attempts to remove a specified directory and its contents.

    Args:
        folder_address (str): The path of the directory to be removed.
    """
    try:
        shutil.rmtree(folder_address)
    except Exception as e:
        print(f"Failed to remove temporary directory {folder_address}. Reason: {e}")


def download_youtube_video(url, temp_folder):
    """
    Downloads a YouTube video to a specified folder.

    Args:
        url (str): The URL of the YouTube video to download.
        temp_folder (str): The folder where the downloaded video will be saved.

    Returns:
        str: The path to the downloaded video file.
    """
    save_location = os.path.join(temp_folder, "video.mp4")
    try:
        # Download the best quality video available
        # try best
        command = ['youtube-dl', '-f', '137', '-o', save_location, url]
        subprocess.run(command, check=True)
        print("Video downloaded successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return save_location


def get_file_name(file_path):
    """
    Extracts the file name from a given file path.

    Args:
        file_path (str): The complete file path.

    Returns:
        str: The extracted file name.
    """
    return os.path.basename(file_path)


def extract_number_from_filename(filename):
    """
    Extracts a number from a filename, assuming the filename contains a number.

    Args:
        filename (str): The filename to extract the number from.

    Returns:
        int: The extracted number.
    """
    name, _ = os.path.splitext(filename)
    return int(''.join(filter(str.isdigit, name)))


def safe_file_read(file_path, mode='rb'):
    """
    Safely reads a file and handles exceptions.

    Args:
        file_path (str): Path of the file to read.
        mode (str): Mode in which the file is to be opened.

    Returns:
        bytes or None: The content of the file, or None if an error occurred.
    """
    try:
        with open(file_path, mode) as file:
            return file.read()
    except Exception as e:
        print(f"Failed to read file {file_path}. Reason: {e}")
        return None


def remove_files_from_folder(folder_name):
    """
    Deletes all files within a specified folder.

    Args:
        folder_name (str): The name of the folder from which files will be deleted.
    """
    try:
        if os.path.exists(folder_name) and os.path.isdir(folder_name):
            for filename in os.listdir(folder_name):
                file_path = os.path.join(folder_name, filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                except Exception as e:
                    print(f'Failed to delete {file_path}. Reason: {e}')
        else:
            print(f"The directory {folder_name} does not exist.")
    except Exception as e:
        print(f'An error occurred: {e}')
