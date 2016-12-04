#program prints the full path of files in current directory.

import pathlib
pth = pathlib.Path('./')

for f in pth.iterdir():
	print(f)


