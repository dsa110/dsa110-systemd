# systemd science pipeline services

Check the systemd [tutorial](https://github.com/torfsen/python-systemd-tutorial) for more info.

## Services

service | location | user
------- | -------- | ----
antmc   | antservice | ubuntu
corr | corr01-16 | ubuntu
search | corr17-20 | ubuntu
T2 | corr00 | ubuntu
voltage | corr01-16 | ubuntu
bfcopy | dsastorage | user
calibration_preprocessing | dsastorage | user
calibration | dsastorage | user

## Ensure start after networking is up
To ensure the service is started after networking is up(nice for those services connecting to etcd), add the following under the [Unit] declaration:

`After=network-online.target`

## Enable. To start after a reboot
'systemctl --user enable <service>`

## Run

`systemctl --user start <service>`

## Logging

`journalctl --user-unit <service>`
