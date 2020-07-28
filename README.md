# PPSSPP-patches

My cheats, fixes and workarounds. Happy to collab!

# Friendly repos
* [LunaMoo/PPSSPP_workarounds](https://github.com/LunaMoo/PPSSPP_workarounds/) - gotten inspired by this repo

# Docs

**Extemely useful** (although contradictory)

* [Some Wiki](https://datacrystal.romhacking.net/wiki/CwCheat)
* [Human explanation on some forum](https://gbatemp.net/threads/guide-how-to-create-gateway-cheat-codes.410926/)

**Additional resources**

* [How to use "Condition" in debugger](https://forums.ppsspp.org/showthread.php?tid=22400&page=2)

# Notes
* CWCheat indeed doesn't obey the  traditional virtual memory mapping scheme, so to convert from the traditional address to the CWCheat one, take away ```0x08800000``` HEX from it. Or 
```
python3 helpy.py
```

# Templates

## Pointer

Surprisingly, this crazy syntax is correct?

```
_L 0x6AAAAAAA 0xVVVVVVVV
_L 0x000Y0001 0xIIIIIIII

AAAAAAA = pointer location
IIIIIIII = pointer offset (subtract this value to the address to get effective address)
VVVVVVVV = value to write
Y = 3 for byte write, 4 for halfword and 5 for word) 
```

Also do I need to clear the ~~fake~~ offset register after use? Apparently not.  

## Safety checks

Taken from Fired Up (the game), but you'd get the idea
```
_C0 Infinite ammo [Enable]
_L 0xE00200A0 0x000BDFE4 // check, 1/2
_L 0xE001AE05 0x000BDFE6 // check, 2/2
_L 0x200BDFE4 0x00000000 // nop
//
_C0 Infinite ammo [Disable]
_L 0xE0020000 0x000BDFE4 // check, 1/2
_L 0xE0010000 0x000BDFE6 // check, 2/2
_L 0x200BDFE4 0xAE0500A0 // orig
//
// 088BDFE4:AE0500A0 // orig
// 088BDFE4:00000000 //mod
//
```

