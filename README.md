# PPSSPP-patches

My cheats, fixes and workarounds for PPSSPP games and apps.

## See also

* [LunaMoo/PPSSPP_workarounds](https://github.com/LunaMoo/PPSSPP_workarounds/) – Inspiration.

--------------------

* <ins>**TAbdiukov/PPSSPP-patches</ins>** – My cheats, fixes and workarounds for PPSSPP games and apps.
* [TAbdiukov/Ikejime](https://github.com/TAbdiukov/Ikejime) – Various patches for Windows OS and apps.
* [TAbdiukov/Ikejime-Private](https://github.com/TAbdiukov/Ikejime-Private) – <ins>Private</ins> patches.
* [TAbdiukov/WinRegistry](https://github.com/TAbdiukov/WinRegistry) – Windows Registry tweaks.

## Docs

**Extemely useful** (though contradictory)

* [Data Crystal Wiki](https://datacrystal.romhacking.net/wiki/CwCheat)
* [Informal explanation on GBATemp](https://gbatemp.net/threads/guide-how-to-create-gateway-cheat-codes.410926/)

**Additional resources**

* [How to use "Condition" in debugger](https://forums.ppsspp.org/showthread.php?tid=22400&page=2)

## Local guides
*(not something readily achievable with CWCheat functionality)*

* [Sims 2 The – Teleport anywhere](./guides/Sims2The_Teleport_anywhere.md)
* [TDU – repack game to improve graphics and performance](./guides/TDU-hard-improvements.md) *(complementary to the CWCheat patches)*
* [TDU – (other) interesting parameters](./guides/TDU-interesting-params.md) *(if you feel adventurous)*
* [TDU – Teleport anywhere, including secret islands](./guides/TDU-tp-islands.md) *(or "assembly for beginners")*

## Templates

### Pointer

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

### Safety checks

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

## Other notes
* CWCheat doesn't obey the  traditional virtual memory mapping scheme, so to convert from the traditional address to the CWCheat one, subtract ```0x08800000``` HEX from it. Or use the following tool,
```
python3 helpy.py
```

### Update 2023+ – Note about some patches

In more modern PPSSPP builds (for example, PPSSPP 1.13.2) it was observed that some patches are being applied automatically, thus increasing playability, performance and experience for general players. For example,  

* Test Drive Unlimited [US] – remove GBA-like pixelization.

If you observe that the patch was already applied, then there is no need to apply it again. Just enjoy it.
