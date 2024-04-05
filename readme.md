![Logo](https://raw.githubusercontent.com/mandarnaik016/UPX-Modifier/main/favicon.ico)

# UPX Modifier

Yet another project to modify headers of file compressed with UPX just to disable the decompression via **-d** command.

## Installation

Download the latest exe from here.

Also, you can use python script

```
git clone https://github.com/mandarnaik016/UPX-Modifier.git
cd UPX-Modifier
python upx.py
```

## Usage

```
upx.exe calc.exe calc.modified.exe
```

## Demo

![upx-cannot-decompress](image)

A calc.exe compressed with UPX typically in a HEX editor.

![calc upx compressed](image)

Whereas after running UPX modifier,

![comparison-between-upx-packed](image)

## Author

- [@mandarnaik016](https://github.com/mandarnaik016)

## Appendix

- [UPX](https://upx.github.io/)
- [akamai](https://www.akamai.com/blog/security/upx-packed-headaches)
- [stackexchange](https://reverseengineering.stackexchange.com/questions/3323/how-to-prevent-upx-d-on-an-upx-packed-executable)

## License

~~~
UPX Modifier
Copyright (C) 2024 Mandar Naik

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
~~~
