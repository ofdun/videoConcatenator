import subprocess
import os
import shutil
import platform
from configparser import ConfigParser

def create_start_video(FFMPEG_PATH: str) -> None:
    if 'start.mp4' in os.listdir('special/'):
        return
        # 'start.mp4 already exists'
    # ALL VIDEOS SHOULD BE ENCODED WITH
    # LIBX264 FOR VIDEO
    # AAC FOR SOUND
    # SCALED 1920X1080 
    # 24 FRAMERATE (optionally but preffered)
    #TODO reencode start videos
    command = [
        FFMPEG_PATH,
        '-f', 'concat',
        '-safe', '0',
        '-i', 'special/input.txt',
        '-c', 'copy',
        '-fps_mode', '0',
        'special/start.mp4'
    ]
    subprocess.run(command)
    
def concat_videos(FFMPEG_PATH: str, output_filename='output.mp4') -> None:
    command = [
        FFMPEG_PATH,
        '-f', 'concat',
        '-safe', '0',
        '-i', 'videos.txt',
        '-r', '24',
        '-s', '1920x1080',
        '-c:v', 'libx264',
        '-c:a', 'aac',
        '-b:v', cfg.get("DEFAULT", "video_bitrate"),
        '-b:a', cfg.get("DEFAULT", "audio_bitrate"),
        '-ar', cfg.get("DEFAULT", "audio_rate"),
        output_filename
    ]
    subprocess.run(command)
    
def encode_video(FFMPEG_PATH: str, video_path: str) -> None:
    command  = [
        FFMPEG_PATH,
        '-i', video_path,
        '-r', '24',
        '-s', '1920x1080',
        '-c:v', 'libx264',
        '-c:a', 'aac',
        '-b:v', cfg.get("DEFAULT", "video_bitrate"),
        '-b:a', cfg.get("DEFAULT", "video_bitrate"),
        '-ar', cfg.get("DEFAULT", "audio_rate"),
        video_path.replace('videos/', 'encoded_videos/', 1)
    ]
    subprocess.run(command)
    
def encode_all_videos(FFMPEG_PATH: str) -> None:
    if 'encoded_videos' not in os.listdir():
        os.mkdir('encoded_videos')
    for video in os.listdir('videos/'):
        if video != '.DS_Store': # Stupid mac os thing
            encode_video(FFMPEG_PATH, 'videos/' + video)

def create_videos_input_file() -> None:
    # Add start video
    string = 'file special/start.mp4\n'
    
    # Add videos
    for video in os.listdir('encoded_videos/'):
        if video != '.DS_Store': # Stupid mac os thing
            string += 'file encoded_videos/' + video + '\n'
            string += 'file special/transition_encoded.mp4\n'
    
    string += 'file special/outro_encoded.mp4\n'
    with open('videos.txt', 'w') as f:
        f.write(string)
        
def delete_temp():
    if 'videos.txt' in os.listdir():
        os.remove('videos.txt')
    if 'encoded_videos' in os.listdir():
        shutil.rmtree('encoded_videos')
        
def platform_support() -> bool | str:
    system = platform.system()
    if system == 'Darwin':
        FFMPEG_PATH = 'ffmpeg/ffmpeg_macos'
        return FFMPEG_PATH
    elif system == 'Windows':
        FFMPEG_PATH = 'ffmpeg/ffmpeg_windows.exe'
        return FFMPEG_PATH
    else:
        print("Platform is not supported")
        return False

if __name__ == '__main__':
    FFMPEG_PATH = platform_support()
    cfg = ConfigParser()
    cfg.read('config.cfg')
    if FFMPEG_PATH:
        output_filename = input("Enter the output filename (e.g. output.mp4): ")
        create_start_video(FFMPEG_PATH)
        encode_all_videos(FFMPEG_PATH)
        create_videos_input_file()
        concat_videos(FFMPEG_PATH=FFMPEG_PATH, output_filename=output_filename)
        delete_temp()