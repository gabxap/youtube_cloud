import click
import cv2
import subprocess
import tempfile


def read_video(binary_files_temp_folder, video_path):
    """
    Reads a video file frame by frame, extracts QR code data from each frame, and writes it to separate files.

    This function opens the video file, iterates over each frame, and processes it to extract QR code data.
    A progress bar is displayed to show the progress of reading frames from the video.

    Args:
        binary_files_temp_folder (str): Folder path to store the extracted QR code data.
        video_path (str): Path to the video file to be processed.

    Returns:
        int: The total number of frames successfully processed for QR code data.
    """
    # Initialize video capture from the given video path
    cap = cv2.VideoCapture(video_path)
    number_of_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    if not cap.isOpened():
        print("Error: Could not open video.")
        return None

    counter = 0
    with click.progressbar(length=number_of_frames, label='Reading data from video') as bar:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            if process_data_frame(binary_files_temp_folder, frame, counter):
                counter += 1
                bar.update(1)
            else:
                click.echo("\nThere has been an error reading the data.")
                break

    cap.release()
    cv2.destroyAllWindows()

    return counter


def process_data_frame(binary_files_temp_folder, frame, counter):
    """
    Processes a single frame of the video to extract and store QR code content in a binary file.

    The function saves the frame as a temporary image, uses 'zbarimg' command to extract QR code data,
    and writes the data to a binary file named with the frame number.

    Args:
        binary_files_temp_folder (str): Folder path to store the extracted QR code data.
        frame (ndarray): The current frame of the video.
        counter (int): The frame number.

    Returns:
        bool: True if QR code data is successfully extracted and written; False otherwise.
    """
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_image:
        cv2.imwrite(temp_image.name, frame)

        # Command to extract QR code data from the image using Zbarimg
        command = ["zbarimg", "--oneshot", "-Sbinary", "--raw", temp_image.name]
        output_file_path = f"{binary_files_temp_folder}/{counter}.bin"

        with open(output_file_path, "wb") as output_file:
            result = subprocess.run(command, stdout=output_file, stderr=subprocess.PIPE).stderr.decode('utf-8')

            # Check for errors in QR code extraction
            if result.split()[1] == "0":
                return False

        return True
