import dp_file_uploader
import argparse


def get_version():
    version = {}
    with open('./dp_file_uploader/version.py') as fp:
        exec(fp.read(), version)
    version_str = 'v{}'.format(version['__version__'])
    return version_str


def process_args():
    argparser = argparse.ArgumentParser(description='Push file(s) to a DataPower Gateway via the XML Management Interface.')
    argparser.add_argument('hostname', type=str, nargs=1, help='hostname of DataPower Gateway to upload file(s)')
    argparser.add_argument('directory', type=str, nargs=1, help='destination directory, i.e. "local:///sandbox/"')
    argparser.add_argument('-P', '--port', type=int, nargs=1, help='xml-mgmt port, default: 5550')
    argparser.add_argument('-u', '--user', type=str, nargs=1, help='username, default: admin')
    argparser.add_argument('-p', '--password', type=str, nargs=1, help='password, default: admin')
    argparser.add_argument('-V', '--verbose', action='store_true', help='verbose output')
    argparser.add_argument('-v', '--version', action='version', version=get_version())
    argparser.add_argument('fileName', type=str, nargs='+', help='file(s) to push')
    args = argparser.parse_args()
    return args


def main():
    args = process_args()
    dp_file_uploader.run_with_args(args)


if __name__ == '__main__':
    main()
