import ctypes
import os
import time


class File:
    _allowed_file_types = ('bmp', 'gif', 'jpg', 'png', 'tif', 'dib', 'jfif', 'jpe', 'jpeg', 'wdp')

    def __init__(self, absolute_path: str):
        self.absolute_path = absolute_path
        self.time_when_modified = os.stat(absolute_path).st_mtime

    def is_modified(self) -> bool:
        """Checks whether file is modified or not, updates time_when_modified attribute"""
        time_stamp = os.stat(self.absolute_path).st_mtime
        if time_stamp != self.time_when_modified:
            self.time_when_modified = time_stamp
            return True
        return False

    def set_as_desktop_background(self) -> None:
        """Sets the file as a desktop background"""
        if self.absolute_path.split(".")[-1] not in self._allowed_file_types:
            raise TypeError("Not supported file type.")
        ctypes.windll.user32.SystemParametersInfoW(20, 0, self.absolute_path, 0)


def main():
    # paste your absolute path to file here
    wallpaper = File(absolute_path=r"C:\Users\Амирка Програмист\Desktop\wallpaper.jpg")

    print("Press Ctrl+C to exit the program.")
    while True:
        try:
            time.sleep(1)
            if wallpaper.is_modified():
                wallpaper.set_as_desktop_background()
        except KeyboardInterrupt:
            print("Done")
            break


if __name__ == "__main__":
    main()
