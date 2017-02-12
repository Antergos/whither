# whither
[![PyPI](https://img.shields.io/pypi/v/whither.svg?style=flat-square)](https://pypi.python.org/pypi/whither) &nbsp;[![Codacy grade][codacy]](https://www.codacy.com/app/Antergos/whither) &nbsp;[![Python Versions](https://img.shields.io/pypi/pyversions/whither.svg?style=flat-square)]()

#### Universal Linux Application SDK - Create once. Run everywhere.
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

[antergos]: https://dl.dropboxusercontent.com/u/60521097/logo-square26x26.png "antergos"
[arch]: https://dl.dropboxusercontent.com/u/60521097/archlogo26x26.png "arch"
[fedora]: https://dl.dropboxusercontent.com/u/60521097/fedora-logo.png "fedora"
[openSUSE]: https://dl.dropboxusercontent.com/u/60521097/Geeko-button-bling7.png "openSUSE"
[ubuntu]: https://dl.dropboxusercontent.com/u/60521097/ubuntu_orange_hex.png "ubuntu"

[codacy]: https://img.shields.io/codacy/grade/140ddf3d48af4497bc691e4f957aa164.svg?style=flat-square "Codacy Grade"
