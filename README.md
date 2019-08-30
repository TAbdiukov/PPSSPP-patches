# PPSSPP-patches
My cheats, fixes and workarounds

# Friendly repos
* [LunaMoo/PPSSPP_workarounds](https://github.com/LunaMoo/PPSSPP_workarounds/) - gotten inspired by this repo

# Docs
* [Some Wiki](https://datacrystal.romhacking.net/wiki/CwCheat)
* [Human explanation on some forum](https://gbatemp.net/threads/guide-how-to-create-gateway-cheat-codes.410926/)

# Notes
* Let X -> First number in address - ```2^X``` is how many bytes to change in any given line
* CWCheat indeed doesn't obey the  traditional virtual memory mapping scheme, so to convert from the traditional address to the cwcheat one, take away ```0x8800000``` HEX from it