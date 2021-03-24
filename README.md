# systemd science pipeline services

Check the systemd [tutorial](https://github.com/torfsen/python-systemd-tutorial) for more info.

## Services

service | location | user
------- | -------- | ----
corr | corr01-16 | ubuntu
search | corr17-20 | ubuntu
T2 | corr00 | ubuntu
voltage | corr01-16 | ubuntu
bfcopy | dsastorage | user
calibration_preprocessing | dsastorage | user
calibration | dsastorage | user

## Run

`systemctl --user start <service>`
`systemctl --user enable <service>`

## Logging

`journalctl --user-unit <service>`