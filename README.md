# CoffeeHousePy

CoffeeHousePy is the full Python implementation for CoffeeHouse, and it's server
components. The [Makefile](Makefile) contains all the setup procedures
used in order to install CoffeeHousePy, and it's components onto the machine.


## Prepare the system

The system must have `python3.8` installed, `pip` and `gcc`. To prepare the system run
the following command

```shell
sudo make system_prep_python system_prep_pip system_prep_gcc
```


## Install CoffeeHousePy

Depending on the hardware, the installation procedure may take a while. To install
CoffeeHousePy run the following command

```shell
sudo -H make clean build install
```