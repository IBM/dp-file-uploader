# dp-file-uploader

Tool for easily uploading files to a DataPower Gateway file system.

## Pre-requisites

### Requests

This script depends on the [requests](https://2.python-requests.org/en/master/) package. You can install this dependency via `pip3` like so:

```bash
$ cd dp-file-uploader/
$ pip3 install -r requirements.txt
```

### XML Management Interface

Since this script is designed to upload files via the [XML management interface](https://www.ibm.com/support/knowledgecenter/SS9H2Y_7.7.0/com.ibm.dp.doc/networkaccess_xmi.html) the `xml-mgmt` object must be enabled and up in the `default` domain of the gateway you wish to target. You can validate this easily by logging into the CLI of the gateway and checking as follows:

```
idg# show xml-mgmt

xml-mgmt [up]
--------
 admin-state enabled
 ip-address 0.0.0.0
 port 5550
 acl xml-mgmt  [up]
 slm-peering 10 Seconds
 mode any+soma+v2004+amp+slm+wsrr-subscription
 ssl-config-type server
```

## Usage

This script can be used to upload a single file, or multiple files, to a target DataPower Gateway filesystem. You control the behavior of the script through command-line arguments. The minimum usage would be as follows:

```bash
$ python3 dp-file-uploader.py my.datapower.com "local:///sandbox/" file.txt
```

This would upload the `file.txt` file to the DataPower Gateway at hostname (`my.datapower.com`) and store the file within the `local:///sandbox/` directory.

Since no other arguments were provided, some defaults were used:

- `user` defaults to `admin`
- `password` defaults to `admin`
- `port` defaults to `5550`

You can specify each of these via command-line argument. For example:

```bash
$ python3 dp-file-uploader.py \
    --user "myaccount" \
    --password "mypassword" \
    --port 9550 \
    my.datapower.com "local:///sandbox/" file.txt
```

You can also upload multiple files at once, using either wildcards or specifying multiple names manually.

```bash
# using wildcards
$ python3 dp-file-uploader.py my.datapower.com "local:///sandbox/" file*.txt

# specifying each manually
$ python3 dp-file-uploader.py my.datapower.com "local:///sandbox/" file1.txt file2.txt file3.txt
```

## Troubleshooting

You can enable verbose output via the `-v, --verbose` command line argument to get a little more detail from the script as it runs. If this does not help to solve your problem, please feel free to [open an issue](https://github.com/IBM/dp-file-uploader/issues/new).
