# whither
[![PyPI](https://img.shields.io/pypi/v/whither.svg?style=flat-square)](https://pypi.python.org/pypi/whither) &nbsp;[![Codacy grade][codacy]](https://www.codacy.com/app/Antergos/whither) &nbsp;[![Python Versions](https://img.shields.io/pypi/pyversions/whither.svg?style=flat-square)]()

### Universal Linux Application SDK - Create once. Run everywhere.

## Install It

### Distro Packages
|Distro|Install Command/Links|
|:---:|:---:|
|![antergos][antergos]|`sudo pacman -S python-whither`|
|![arch][arch]        |`yaourt -S python-whither`|
|![fedora][fedora]    |`dnf copr enable antergos/python3-whither`|
|![openSUSE][openSUSE]|[1 Click Install](https://software.opensuse.org/ymp/home:antergos/openSUSE_Leap_42.2/whither.ymp?base=openSUSE%3ALeap%3A42.2&query=python3-whither)|
|![ubuntu][ubuntu]    |[OBS Repo](https://software.opensuse.org/download.html?project=home:antergos&package=python3-whither)|

### From Source

#### Dependencies
|                       | ![antergos][antergos] &nbsp;&nbsp; ![arch][arch] | ![ubuntu][ubuntu] | ![fedora][fedora] | ![openSUSE][openSUSE] | 
|-----------------------|--------------------------------------------------|-------------------|-------------------|-----------------------|
|**pyqt5**              |python-pyqt5                                      |python3-pyqt5      |python3-qt5        |python3-qt5            |
|**qt5-webengine**      |qt5-webengine                                     |libqt5webengine5   |qt5-qtwebengine    |libqt5-qtwebengine     |

> ***NOTE:*** These instructions are for the `master` branch. To build the latest release, please see the `stable` branch.

#### Use pip
```sh
sudo pip install whither
```
#### Download & Install
```sh
git clone https://github.com/Antergos/whither.git /tmp/whither
cd /tmp/whither
sudo python setup.py install
```

[antergos]: https://www.dropbox.com/s/tju7maccr328w87/logo-square26x26.png?dl=1 "antergos"
[arch]: https://www.dropbox.com/s/q8ypd345cqcd0b5/archlogo26x26.png?dl=1 "arch"
[fedora]: https://www.dropbox.com/s/b8q448vuwopb0cl/fedora-logo.png?dl=1 "fedora"
[openSUSE]: https://www.dropbox.com/s/jhirpw85ztgl59h/Geeko-button-bling7.png?dl=1 "openSUSE"
[ubuntu]: https://www.dropbox.com/s/nev98nld2u1qbgl/ubuntu_orange_hex.png?dl=1 "ubuntu"

[codacy]: https://img.shields.io/codacy/grade/140ddf3d48af4497bc691e4f957aa164.svg?style=flat-square "Codacy Grade"
