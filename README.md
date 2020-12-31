# CoffeeHousePy

CoffeeHousePy is the full Python implementation for CoffeeHouse, and it's server
components. The [Makefile](Makefile) contains all the setup procedures
used in order to install CoffeeHousePy, and it's components onto the machine.


## Prepare the system

The system must have `python3.6` installed, `pip` and `gcc`. To prepare the system run
the following command, this is designed to run on Ubuntu 18.04

```shell
sudo make system_prep_python system_prep_pip system_prep_gcc
```


## Install CoffeeHousePy

Depending on the hardware, the installation procedure may take a while. To install
CoffeeHousePy run the following command

```shell
sudo -H make clean build install
```


## Services

Once CoffeeHousePy is installed, you can start it's services indvidually.

```shell
make start_langdetect # Starts the language detection server, runs on port 5606
make start_spamdetect # Starts the spam detection server, runs on port 5601
make start_translate # Starts the translation server, runs on port 5603
```

### Services Ports

| Name                           | Protocol | Port |
|--------------------------------|----------|------|
| CoffeeHouse Language Detection | HTTP     | 5606 |
| CoffeeHouse Spam Detection     | HTTP     | 5601 |
| CoffeeHouse Translate          | HTTP     | 5603 |