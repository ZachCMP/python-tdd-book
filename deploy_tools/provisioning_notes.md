Provisioning a new site
===

## Required Packages:

* nginx
* Python 3.6
* virtualenv + pip
* Git

eg, on ubuntu:

```bash
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install nginx git python36 python3.6-venv
```

## Nginx Virtual Host config

* see nginx.template.conf
* replace DOMAIN with, e.g., staging.my-domain.com

## Systemd service

* see gunicorn-systemd.template.service
* replace DOMAIN with, e.g., staging.my-domain.com