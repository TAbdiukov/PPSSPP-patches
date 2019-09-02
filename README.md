# PPSSPP-patches
My cheats, fixes and workarounds

# Friendly repos
* [LunaMoo/PPSSPP_workarounds](https://github.com/LunaMoo/PPSSPP_workarounds/) - gotten inspired by this repo

# Docs
* [Some Wiki](https://datacrystal.romhacking.net/wiki/CwCheat)
* [Human explanation on some forum](https://gbatemp.net/threads/guide-how-to-create-gateway-cheat-codes.410926/)

# Notes
* Let X -> First number in address - ```2^X``` is how many bytes to change in any given line
* CWCheat indeed doesn't obey the  traditional virtual memory mapping scheme, so to convert from the traditional address to the cwcheat one, take away ``0x08800000``` HEX from it

# Pointers

There is this, but how do I use that in practice?

> D3000000 13BA110C – sets the offset to 0x13BA110C
> B0000000 00000000 – loads the 32-bit value at address 0x13BA110C into the offset register, replacing our current offset. So if the value at 0x13BA110C is 0x368F39C3, this will be our new offset (Note: when viewing hex values in a hex editor on your pc or the gateway cheat menu, take endianness into account!)
> 20000000 00000063 – writes an 8-bit value of 0x63 (99) to the address at 0x368F39C3 (0x368F39C3 + 0x00000000 = 0x368F39C3) 

Also do I need to clear the ~~fake~~ offset register after use? 