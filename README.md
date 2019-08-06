# dp-file-uploader

Tool for easily uploading files to an IBM DataPower® Gateway file system.

![GitHub release](https://img.shields.io/github/release/IBM/dp-file-uploader)
![GitHub](https://img.shields.io/github/license/IBM/dp-file-uploader)

## Pre-requisites

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

## Installation

1. Clone or download the repository from the [Releases](https://github.com/IBM/dp-file-uploader/releases) page

    ```bash
    $ git clone git@github.com:IBM/dp-file-uploader.git
    $ cd dp-file-uploader/
    ```

2. Install package via `pip3`

    ```bash
    $ pip3 install .
    ```

    Note: Installing via `pip3` adds the `dp-file-uploader` executable to your PATH.

3. Validate the installation

    ```bash
    $ dp-file-uploader --version
    ```

## Usage

This script can be used to upload a single file, or multiple files, to a target IBM DataPower® Gateway filesystem. You control the behavior of the script through command-line arguments. The minimum usage would be as follows:

```bash
$ dp-file-uploader my.datapower.com "local:///sandbox/" file.txt
```

This would upload the `file.txt` file to the IBM DataPower® Gateway at hostname (`my.datapower.com`) and store the file within the `local:///sandbox/` directory.

Since no other arguments were provided, some defaults were used:

- `user` defaults to `admin`
- `password` defaults to `admin`
- `port` defaults to `5550`

You can specify each of these via command-line argument. For example:

```bash
$ dp-file-uploader \
    --user "myaccount" \
    --password "mypassword" \
    --port 9550 \
    my.datapower.com "local:///sandbox/" file.txt
```

You can also upload multiple files at once, using either wildcards or specifying multiple names manually.

```bash
# using wildcards
$ dp-file-uploader my.datapower.com "local:///sandbox/" file*.txt

# specifying each manually
$ dp-file-uploader my.datapower.com "local:///sandbox/" file1.txt file2.txt file3.txt
```

## Troubleshooting

You can enable verbose output via the `-V, --verbose` command line argument to get a little more detail from the script as it runs. If this does not help to solve your problem, please feel free to [open an issue](https://github.com/IBM/dp-file-uploader/issues/new).
