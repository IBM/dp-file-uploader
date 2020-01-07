import base64
import requests
import urllib3
import re
import xml.dom.minidom
import os.path


# Disable warnings, as XML Mgmt often has a self-signed certificate
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Global for verbose logging, set via --verbose argument
VERBOSE = False


def get_user(args):
    if args.user is not None:
        user = args.user[0]
    else:
        user = 'admin'
    return user


def get_password(args):
    if args.password is not None:
        password = args.password[0]
    else:
        password = 'admin'
    return password


def get_port(args):
    if args.port is not None:
        port = str(args.port[0])
    else:
        port = '5550'
    return port


def normalize_directory(directory):
    if directory.endswith('/'):
        return directory
    else:
        return directory + '/'


def build_url(hostname, port):
    url = 'https://' + hostname + ':' + port + '/'
    if VERBOSE:
        print('URL:', url)
    return url


def print_pretty_xml(xml_str):
    length = len(xml_str)
    print(f'XML string length = {length}')
    if length > 10000:
        print('Omitting XML nodeset from log due to size')
    else:
        dom = xml.dom.minidom.parseString(xml_str)
        dom_pretty = dom.toprettyxml()
        print('\n' + dom_pretty)


def build_xml(directory, filename, data):
    fileTarget = directory + filename
    if VERBOSE:
        print('Building XML request')
        print('File target:', fileTarget)
    fileContent = base64.b64encode(data).decode('ascii')
    xmlTemplate = '''<env:Envelope xmlns:env="http://schemas.xmlsoap.org/soap/envelope/">
                        <env:Body>
                            <dp:request xmlns:dp="http://www.datapower.com/schemas/management">
                                <dp:set-file name="{}">{}</dp:set-file>
                            </dp:request>
                        </env:Body>
                    </env:Envelope>'''
    xmlRequestStr = xmlTemplate.format(fileTarget, fileContent).replace('\n', '')
    xmlRequest = re.sub(r'> +<', '><', xmlRequestStr)
    if VERBOSE:
        print('Generated XML:')
        print_pretty_xml(xmlRequest)
    return xmlRequest


def process_file(filename, directory, url, user, password):
    print('Preparing to send file: ' + filename)
    with open(filename, 'rb') as lines:
        data = lines.read()
    if os.path.isabs(filename):
        target_filename = os.path.basename(filename)
    else:
        target_filename = os.path.basename(os.path.abspath(filename))
    xml = build_xml(directory, target_filename, data)
    if VERBOSE:
        print('Sending POST request')
    r = requests.post(url, auth=(user, password), data=xml, verify=False)
    if VERBOSE:
        print('HTTP Request Headers:', r.request.headers)
        print('HTTP Response Code:', r.status_code)
        print('HTTP Response Headers:', r.headers)
        print('Response XML:')
        print_pretty_xml(r.text)
    if r.status_code == 200:
        if '<dp:result>OK</dp:result>' in r.text:
            print('File uploaded successfully')
        else:
            print('File upload failed')
            reason = re.search(r'<dp:result>(.+)</dp:result>', r.text)
            print('Reason:', reason.group(1))


def run_with_args(args):
    if args.verbose:
        global VERBOSE
        VERBOSE = True
        print(args)
    hostname = args.hostname[0]
    port = get_port(args)
    url = build_url(hostname, port)
    user = get_user(args)
    password = get_password(args)
    directory = normalize_directory(args.directory[0])
    for filename in args.fileName:
        process_file(filename, directory, url, user, password)
