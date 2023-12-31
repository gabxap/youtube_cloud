<p align="center">
  <img src="res/logo-2.png" alt="YouTube Cloud Logo" width="300"/>
</p>

<h1 align="center">YouTube Cloud</h1>
<p align="center">
Built for YouTube, this tool encodes any file into a video and seamlessly decodes the video back to the original file.</p>
<p align="center">📄 ➡️ 🎥 ➡️ 📄</p>


## Why?
<p style="text-align: justify;">
YouTube serves as a limitless, free cloud storage platform, designed to store video files in formats such as .MP4, .AVI, and similar types. YouTube Cloud extends YouTube's utility beyond traditional video content, allowing for the encoding of any file type into a YouTube-compatible video and facilitating its seamless decoding back to the original file, thus unlocking YouTube's potential for versatile file storage and access. This project is just a proof of concept, and even thought it does work, I wouldn't recommend to upload your whole hard drive to YouTube as it is not practical and can go against Google's policies. 
</p>


## How?

<p style="text-align: justify;">
In this <a href="https://www.youtube.com/watch?v=_w6PCHutmb4">video</a>, BK Binary explores the intriguing concept of encoding files into YouTube videos. This tool builds on that idea, utilizing version 40 QR codes to encode binary data from files into videos, where each video frame can store up to 2953 bytes of data. Additionally, the tool features a versatile decoder that can process videos whether stored locally or directly from a YouTube URL, simplifying the retrieval and decoding of files.</p>

## Getting Started

### Prerequisites

Before installing YouTube Cloud, you need to have the following tools installed on your system:

- `youtube-dl`: A command-line program to download videos from YouTube.com and other video sites.
- `zbar`: A command-line utility for reading barcodes from various sources such as images and video streams.

Please refer to the official documentation for installation instructions:

- [youtube-dl installation guide](https://github.com/ytdl-org/youtube-dl#installation)
- [zbar installation guide](https://github.com/mchehab/zbar)

### Installation

```bash
git clone https://github.com/gabxap/youtube_cloud.git
cd youtube_cloud
pip install -r requirements.txt
```

## How to use

### Encoding Files into Videos 

Follow these steps to encode your files into a video:

1. **Prepare Your File**: Make sure the file you want to encode is saved on your computer and you know its path.

2. **Open the Terminal**: Navigate to the directory where you have installed YouTube Cloud.

3. **Run the Encode Command**: Use the `encode` command to convert your file into a video. Replace `<file_path>` with the path to your file. The command format is as follows:

    ```bash
    python youtube_cloud.py encode <file_path>
    ```

    For example, if your file is named document.pdf and located in your Documents folder, the command might look like this:
    ```bash
    python youtube_cloud.py encode /Users/yourusername/Documents/document.pdf
    ```
4. **Locate the Output Video**: After the encoding process completes, find the generated video in the same directory as your original file. The video will have the same name as your file but with an extra `.mp4` extension.

### Decoding Videos into Files 
To decode a video back into its original file, follow these steps:

1. **Prepare Your Video**: Ensure the video you want to decode is either downloaded on your computer or available on YouTube.

2. **Open the Terminal**: Go to the directory where YouTube Cloud is installed.

3. **Run the Decode Command**: Use the `decode` command to convert your video back into the original file. Replace `<video_path_or_url>` with the path to your video file or the YouTube URL. The command format is: 

    ```bash
    python youtube_cloud.py decode <video_path_or_url>
    ```

    For example, to decode a local video file named document.pdf.mp4, your command might be:

    ```bash
    python youtube_cloud.py decode /Users/yourusername/Documents/document.pdf.mp4
    ```

    Alternatively, to decode a video from YouTube, your command might look like this:

    ```bash
    python youtube_cloud.py decode https://www.youtube.com/watch?v=7Ib19pl5Di0
    ```
4. **Locate the Decoded File**: Once the decoding process is complete, you'll find the restored original file in the same directory as the video. The file will have its original name and format, just as it was before encoding.

