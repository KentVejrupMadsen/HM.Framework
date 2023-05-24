from os.path \
    import isfile

from moviepy.editor import *

from math import floor

path_to_movie = 'C:\\Workspace\\video-frame-extractor\\video\\test.mp4'


def get_path_to_movie():
    global path_to_movie
    return path_to_movie


def exist_movie() -> bool:
    return isfile(get_path_to_movie())


def main():
    print('video frame extractor')

    if exist_movie():
        print('opening: ', get_path_to_movie())

        video = VideoFileClip(get_path_to_movie())

        duration_of_video = floor(video.duration)

        print('duration: ', str(duration_of_video))

        video.close()



if __name__ == '__main__':
    main()
