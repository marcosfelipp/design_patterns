'''
Example: Implementation a screen builder. Factory produce Windows Screen, Linux Screen or IOS Screen.
'''

class ScreenFactory():
    @classmethod
    def generate_screen(self, screen_type):
        if screen_type == 'windows':
            return WindowsScreen()
        elif screen_type == 'linux':
            return LinuxScreen()
        elif screen_type == 'ios':
            return IOSScreen()


class WindowsScreen():
    def __init__(self):
        print('Windows Screen generated')

    def resolution(self):
        print('Resolution is 1024x768')

class LinuxScreen():
    def __init__(self):
        print('Linux Screen generated')

    def resolution(self):
        print('Resolution is 1920x1080')

class IOSScreen():
    def __init__(self):
        print('IOS screen generated')

    def resolution(self):
        print('Resolution is 3840x2160')


if __name__ == '__main__' :
    screen = ScreenFactory.generate_screen('linux')
    screen.resolution()