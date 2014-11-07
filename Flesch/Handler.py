__author__ = 'Ryan Strug'


class Handler:
    @staticmethod
    def error(error=None):
        if error == FileNotFoundError:
            print('The specified file was not found.')

    @staticmethod
    def print_help():
        Handler.print_usage()
        print('\n-h Help\n-v Version')

    @staticmethod
    def print_usage():
        print('Usage: python<version> Flesch [-hv] FILE')

    @staticmethod
    def print_version():
        print('Flesch Readability Index v', __version__, '\nWritten by Ryan Strug')