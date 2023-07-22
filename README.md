# Video Concatenator

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Notes](#notes)

## About <a name = "about"></a>

This small project can help you concatenate intro with any amount of videos and outro as fast as possible. It uses 100% of your machines power and doesn't have anything useless.

## Getting Started <a name = "getting_started"></a>


### Prerequisites

Install python 3.11.x or higher version (3.11.x is stable but you can try it even with a lower version)

### Installing

1. Copy the project using bash or cmd if you have Git installed:
```bash
git clone https://github.com/ofdun/videoConcatenator.git
```
2. If you don't have Git installed
press **Code** button on the repository page, then press **Download ZIP** and unzip  it somewhere on your PC.
3. ***VERY IMPORTANT***: unzip two archives in the ffmpeg folder and leave files there, without creating any new folders.
4. Create python venv or just use your global python interpreter because this project doesn't use any external libraries.

## Usage <a name = "usage"></a>

***VERY IMPORTANT:***

start.mp4 and outro.mp4 SHOULD BE ENCODED WITH

* LIBX264 FOR VIDEO
* AAC FOR SOUND
* SCALED 1920X1080 
* 24 FRAMERATE (optionally but preffered)

***All other videos that you add to the "videos" folder will be reencoded with this parameters.***

In order for script to work:

1. Add your videos to "videos" folder and add start.mp4 and outro.mp4 into "special" folder.

2. Run the script using any IDE or cmd:
```cmd
python main.py
```
3. Enter the output filename with its suffix (.mp4 preffered)

## Notes <a name = "notes"></a>

I already provided intro, outro and videos just for an example.

Project was written on ffmpeg and python without using any external  libraries by me - [@ofdun](https://github.com/ofdun)