from os.path \
    import \
    isdir, \
    isfile, \
    join

from math \
    import \
    floor

from HM.objects.operators.counter \
    import Counter


class Extractor:
    def __init__(
            self,
            save_location: str,
            path_to_video: str,
            save_frames_as: str = 'jpg'
    ):
        self.counter = Counter()

        self.save_location: str = save_location
        self.path_to_video: str = path_to_video

        self.video_clip: None
        self.save_frames_as_format: str = save_frames_as
        self.snapshot_at: float = 1.0

    def __del__(self):
        pass

    def execute(self):
        if self.exist_video_file() \
           and \
           self.exist_save_location():
            pass
        else:
            return

        self.set_video_clip(
            None
        )

        self.process_video()

    def process_video(self):
        counter_of_frames = self.get_counter()

    def exist_video_file(self) -> bool:
        return isfile(
            self.path_to_video
        )

    def exist_save_location(self) -> bool:
        return isdir(
            self.get_save_location()
        )

    def get_counter(
            self
    ) -> Counter:
        return self.counter

    def get_save_location(
            self
    ) -> str:
        return self.save_location

    def get_path_to_video(
            self
    ) -> str:
        return self.path_to_video

    def get_video_clip(
            self
    ) -> None:
        return self.video_clip

    def get_save_frames_as_format(
            self
    ) -> str:
        return self.save_frames_as_format

    def set_save_frames_as_format(
            self,
            value: str
    ) -> None:
        self.save_frames_as_format = value

    def set_counter(
            self,
            value: Counter
    ) -> None:
        self.counter = value

    def set_save_location(
            self,
            value: str
    ) -> None:
        self.save_location = value

    def set_path_to_video(
            self,
            value: str
    ) -> None:
        self.path_to_video = value

    def set_video_clip(
            self,
            value: None
    ) -> None:
        self.video_clip = value
