# less-hex-swapper

This is for those times when you copy the mockup CSS right out of the browser and there are all those hex color values in there. If you are storing your color palette in a `.less` constants file, this script will swap the hex out for you, so you don't have to do it all manually.

Alter the paths appropriately at the top of `no-hex.py` and then launch the python script. It will overwrite the file, swapping out all of the hex for `.less` variables.

`_broccoli copy.less` is here to make restoring the unswapped values easier (since they do get overwritten) during development.

I wrote this in Python3. I don't know if it will work in Python2. The simplest way to run a Python script is download `IDLE Python3`.
