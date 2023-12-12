import click
import cv2
import numpy as np
import os


def generate_video_from_images(qr_codes_temp_folder, output_video_path, frame_width=1920, frame_height=1080, fps=30):
    """
    Generates a video from a series of images stored in a directory.

    This function reads each image file from the specified folder, centers it on a blank frame of the given dimensions,
    and writes it to the output video file. A progress bar is displayed to show the progress of video generation.

    Args:
        qr_codes_temp_folder (str): Path to the folder containing the images to be compiled into the video.
        output_video_path (str): Path where the generated video will be saved.
        frame_width (int, optional): Width of the video frames. Defaults to 1920 pixels.
        frame_height (int, optional): Height of the video frames. Defaults to 1080 pixels.
        fps (int, optional): Frames per second for the video. Defaults to 30.

    Returns:
        None: The function writes the generated video to 'output_video_path'.
    """
    image_files = sorted(os.listdir(qr_codes_temp_folder), key=lambda x: int(x.split('.')[0]))

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video_writer = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))

    with click.progressbar(length=len(image_files), label='Generating Video') as bar:
        for image_file in image_files:
            image_path = os.path.join(qr_codes_temp_folder, image_file)
            frame = cv2.imread(image_path)

            if frame is None:
                continue

            blank_frame = np.zeros((frame_height, frame_width, 3), np.uint8)

            height, width = frame.shape[:2]

            x_offset = (frame_width - width) // 2
            y_offset = (frame_height - height) // 2

            if x_offset >= 0 and y_offset >= 0:
                blank_frame[y_offset:y_offset + height, x_offset:x_offset + width] = frame
            else:
                resized_frame = cv2.resize(frame, (frame_width, frame_height))
                blank_frame = resized_frame

            video_writer.write(blank_frame)
            bar.update(1)

    video_writer.release()

    click.echo(f"Video saved at {output_video_path}")
