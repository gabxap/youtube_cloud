#!/usr/bin/env python3
# coding: utf-8

import click
from decoder.file_reconstructor import remade_file
from decoder.video_reader import read_video
from encoder.qr_code import generate_qrs
from encoder.video_generator import generate_video_from_images
from utils import get_file_name, download_youtube_video, create_temp_folder, remove_temp_folder
import validators



@click.group()
def cli():
    """
    Youtube_cloud
    """
    pass


@cli.command()
@click.argument('file_address')
def encode(file_address):
    """Encode a file into a video."""
    file_name = get_file_name(file_address)
    qr_codes_temp_folder = create_temp_folder()
    generate_qrs(qr_codes_temp_folder, file_address, file_name)
    generate_video_from_images(qr_codes_temp_folder, f"{file_name}.mp4")
    remove_temp_folder(qr_codes_temp_folder)


@cli.command()
@click.argument('video_address')
def decode(video_address):
    """Decode a video into a file. It accepts both local files and YouTube urls."""
    temp_folder = create_temp_folder()
    if validators.url(video_address):
        video_address = download_youtube_video(video_address, temp_folder)

    number_chunks = read_video(temp_folder, video_address)
    remade_file(temp_folder, number_chunks)
    remove_temp_folder(temp_folder)


if __name__ == "__main__":
    cli()
