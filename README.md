# PPSSPP-patches
My cheats, fixes and workarounds

# Friendly repos
* [LunaMoo/PPSSPP_workarounds](https://github.com/LunaMoo/PPSSPP_workarounds/) - gotten inspired by this repo

# Docs
* [Some Wiki](https://datacrystal.romhacking.net/wiki/CwCheat)
* [Human explanation on some forum](https://gbatemp.net/threads/guide-how-to-create-gateway-cheat-codes.410926/)

# Notes
* Let X -> First number in address - ```2^X``` is how many bytes to change in any given line
* CWCheat indeed doesn't obey the  traditional virtual memory mapping scheme, so to convert from the traditional address to the cwcheat one, take away ```0x08800000``` HEX from it

# Pointers

Surprisingly, this crazy syntax is correct?

```
_L 0x6AAAAAAA 0xVVVVVVVV

_L 0x000Y0001 0xIIIIIIII
	AAAAAAA = pointer location

IIIIIIII = pointer offset (subtract this value to the address to get effective address)

VVVVVVVV = value to write

Y = 3 for byte write, 4 for halfword and 5 for word) 
```


Also do I need to clear the ~~fake~~ offset register after use? 