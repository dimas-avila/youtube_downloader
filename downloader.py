from pytube import YouTube
import os
import pathlib


class Downloader():

    def __init__(self, path):
        self.path = path
        cmd = f'mkdir {self.path}'
        os.system(cmd)

    def printStreams(self, link_video):
        yt = YouTube(link_video)
        for stream in yt.streams:
            print("Stream ->", stream)

    def download(self, link_video, isAudio, **kwargs):
        yt = YouTube(link_video)
        title = yt.title.split()[0]
        full_path = self.path.joinpath(title)
        os.system(f'mkdir {full_path}')
        if (isAudio):
            yt.streams.filter(mime_type='audio/mp4').first().download(
                filename=f'audio_{title}', output_path=full_path)
        else:
            quality = kwargs.get('quality', None)
            audio_file = f'audio_{title}'
            video_file = f'video_{title}'
            yt.streams.filter(
                mime_type='audio/mp4').first().download(filename=audio_file, output_path=full_path)
            yt.streams.filter(mime_type='video/mp4', res=quality).first().download(
                filename=video_file, output_path=full_path)
            audio = audio_file+'.mp4'
            video = video_file+'.mp4'
            todo = title+'.mp4'
            cmd = f'ffmpeg -i {full_path.joinpath(video)} -i {full_path.joinpath(audio)} -c:v copy -c:a aac {full_path.joinpath(todo)}'
            os.system(cmd)
            cmd = f'del /f {full_path.joinpath(audio)} {full_path.joinpath(video)}'
            os.system(cmd)