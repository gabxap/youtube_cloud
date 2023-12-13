<p align="center">
  <img src="res/logo-2.png" alt="YouTube Cloud Logo" width="300"/>
</p>

<h1 align="center">YouTube Cloud</h1>
<p align="center">
  A tool that encodes any file into a video, and seamlessly decodes a video back to the original file.
</p>
<p align="center">📄 ➡️ 🎥 ➡️ 📄</p>


## Why?
<p style="text-align: justify;">
YouTube serves as a limitless, free cloud storage platform, designed to store video files in formats such as .MP4, .AVI, and similar types. YouTube Cloud extends YouTube's utility beyond traditional video content, allowing for the encoding of any file type into a YouTube-compatible video and facilitating its seamless decoding back to the original file, thus unlocking YouTube's potential for versatile file storage and access. This project is just a proof of concept, and even thought it does work, I wouldn't recommend to upload your whole hard drive to YouTube as it is not practical and can go against Google's policies. 
</p>


## How?

<p style="text-align: justify;">
Inspired by BK Binary's <a href="https://www.youtube.com/watch?v=_w6PCHutmb4">video</a>, this tool introduces the implementation of version 40 QR codes for encoding the binary data that compose a file, where each frame of the generated video can store up to 2953 bytes of data. Additionally, the tool includes a versatile decoder that can process videos either stored locally or directly from a YouTube URL, facilitating easy retrieval and decoding of the original files.
</p>

## Getting Started

### Installation

```bash
git clone https://github.com/yourusername/youtube_cloud.git
cd youtube_cloud
pip install -r requirements.txt
