# PPSSPP-patches

My cheats, fixes and workarounds for PSP games.

# Friendly repos
* [LunaMoo/PPSSPP_workarounds](https://github.com/LunaMoo/PPSSPP_workarounds/) - gotten inspired by this repo

# Docs

**Extemely useful** (although contradictory)

* [Data Crystal Wiki](https://datacrystal.romhacking.net/wiki/CwCheat)
* [Informal explanation on GBATemp](https://gbatemp.net/threads/guide-how-to-create-gateway-cheat-codes.410926/)

**Additional resources**

* [How to use "Condition" in debugger](https://forums.ppsspp.org/showthread.php?tid=22400&page=2)

## Local guides
*(not something readily achievable with CWCheat functionality)*


* [Sims 2 The - Teleport anywhere](./guides/Sims2The_Teleport_anywhere.md) 

# Notes
* CWCheat doesn't obey the  traditional virtual memory mapping scheme, so to convert from the traditional address to the CWCheat one, subtract ```0x08800000``` HEX from it. Or use the following tool,
```
python3 helpy.py
```

# Templates

## Pointer

Surprisingly, this syntax is correct

```
_L 0x6AAAAAAA 0xVVVVVVVV
_L 0x000Y0001 0xIIIIIIII

AAAAAAA = pointer location
IIIIIIII = pointer offset (subtract this value to the address to get effective address)
VVVVVVVV = value to write
Y = 3 for byte write, 4 for halfword and 5 for word) 
```

Must I clear the (fake) offset register after use — No.  

## Safety checks

Taken from Fired Up (the game), but you'll get the idea
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

## Update 2023 - Note about some cheats

In more modern PPSSPP builds (for example, PPSSPP 1.13.2) it was observed that some patches are being applied automatically, thus increasing playability, performance and experience for general players. For example
* Test Drive Unlimited [US] - remove GBA-like pixelization.

If you observe that the patch was already applied, then there is no need to apply it again. Just enjoy it.
