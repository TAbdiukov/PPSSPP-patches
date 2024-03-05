## Generic

Green bed: 09B45E08
Trash: 09B79960 09B79960
Newspaper: 09B57D88
Kate: 09B37BF0
Buster: 09B1BC18
Deltoid: 09B1CE08
Carpool: 09B64BC8 09B64A38
Arcade: 09B53030

Linda: 09B1C140 09B1C140

DeBingo  chair (1): 09B4BB00 09B4BB00
Computer chair (2): 09B6A668 09B6A668

## Park

Pet bakery:       09B47D48 09B47AF0
Pet Kennel:       09B49580 09B49328
Pet Emporium:     09B49BC0 09B49968
Pet Purveyors:    09B4A200 09B49FA8
Pet Salon (Wash): 09B4A9D0 09B4A778
Pet Toy Store:    09B4B010 09B4ADB8

Park phone: 09B53418 09B53418
ATM:       09B61518 09B61518
Fountain:  09B61770 09B615E0 164995840


Coffee Cart:         09B482C0 09B481F8


Drink Water machine: 09B54160 09B54160
HotDog Vending Mach: 09B54228 09B54228

Go to town square:   09B652D0 09B652D0

# Chairs

Note: ID numbers are decimal.

```
ID	Containr	PtrValue
01	09B4BB7C	09B4BB00
02	09B6A6E4	09B6A668
03	09B4B924	09B4B8A8
04	09B6B044	09B6AFC8
05	09B4BC44	09B4BBC8
06	09B4BAB4	09B4BA38
07	09B6AD24	09B6ACA8
08	09B4B9EC	09B4B970
09	09B6A48C	09B6A410
10	09B9EA1C	09B6AD70
11	09B6AEB4	09B6AE38
12	09B6D68C	09B6D548
13	09B6AACC	09B6AA50
14	09B6A554	09B6A4D8
15	09B6AB94	09B6AB18
16	09B6E0B4	09B6DF70
17	09B6AC5C	09B6ABE0
18	09B6F504	09B6F3C0
19	09B6A93C	09B6A8C0
20	09B6B10C	09B6B090
21	09B6AF7C	09B6AF00
22	09B6E30C	09B6E1C8
23	09B6E564	09B6E420
24	09B6A7AC	09B6A730
```

# Lamps

Breakpoint at address: 08A3F294
s3 is PtrValue

# Solution


_C0 Replace buy-menu chairs with overpowered park assets [Enable]
_L 0xE01A09B4 0x0134BB7E // Check, Chair01 expected header (Little-Endian)
_L 0xE01909B6 0x0136D68E // Check, Chair12 expected header (Little-Endian)
_L 0xE01809B6 0x0136A7AE // Check, Chair24 expected header (Little-Endian)
_L 0xE017BB00 0x0134BB7C // Check, Chair01 expected tail
_L 0xE016A668 0x0136A6E4 // Check, Chair02 expected tail
_L 0xE015B8A8 0x0134B924 // Check, Chair03 expected tail
_L 0xE014B044 0x0136B044 // Check, Chair04 expected tail
_L 0xE013BC44 0x0134BC44 // Check, Chair05 expected tail
_L 0xE012BA44 0x0134BAB4 // Check, Chair06 expected tail
_L 0xE011AD24 0x0136AD24 // Check, Chair07 expected tail
_L 0xE010B9EC 0x0134B9EC // Check, Chair08 expected tail
_L 0xE00FA48C 0x0136A48C // Check, Chair09 expected tail
_L 0xE00EEA1C 0x0139EA1C // Check, Chair10 expected tail
_L 0xE00DAEB4 0x0136AEB4 // Check, Chair11 expected tail
_L 0xE00CD68C 0x0136D68C // Check, Chair12 expected tail
_L 0x2134BB7C 0x09B47AF0 // Write, Chair01 buymenu container
_L 0x2136A6E4 0x09B49328 // Write, Chair02 buymenu container
_L 0x2134B924 0x09B49968 // Write, Chair03 buymenu container
_L 0x2136B044 0x09B49FA8 // Write, Chair04 buymenu container
_L 0x2134BC44 0x09B4A778 // Write, Chair05 buymenu container
_L 0x2134BAB4 0x09B4ADB8 // Write, Chair06 buymenu container
_L 0x2136AD24 0x09B53418 // Write, Chair07 buymenu container
_L 0x2134B9EC 0x09B61518 // Write, Chair08 buymenu container
_L 0x2136A48C 0x09B615E0 // Write, Chair09 buymenu container
_L 0x2139EA1C 0x09B481F8 // Write, Chair10 buymenu container
_L 0x2136AEB4 0x09B54160 // Write, Chair11 buymenu container
_L 0x2136D68C 0x09B652D0 // Write, Chair12 buymenu container
//
_C0 Replace buy-menu chairs with overpowered park assets [Disable]
_L 0xE01A09B4 0x0134BB7E // Check, Chair01 expected header (Little-Endian)
_L 0xE01909B6 0x0136D68E // Check, Chair12 expected header (Little-Endian)
_L 0xE01809B6 0x0136A7AE // Check, Chair24 expected header (Little-Endian)
_L 0xE0177AF0 0x0134BB7C // Check, Chair01 expected tail
_L 0xE0169328 0x0136A6E4 // Check, Chair02 expected tail
_L 0xE0159968 0x0134B924 // Check, Chair03 expected tail
_L 0xE0149FA8 0x0136B044 // Check, Chair04 expected tail
_L 0xE013A778 0x0134BC44 // Check, Chair05 expected tail
_L 0xE012ADB8 0x0134BAB4 // Check, Chair06 expected tail
_L 0xE0113418 0x0136AD24 // Check, Chair07 expected tail
_L 0xE0101518 0x0134B9EC // Check, Chair08 expected tail
_L 0xE00F15E0 0x0136A48C // Check, Chair09 expected tail
_L 0xE00E81F8 0x0139EA1C // Check, Chair10 expected tail
_L 0xE00D4160 0x0136AEB4 // Check, Chair11 expected tail
_L 0xE00C52D0 0x0136D68C // Check, Chair12 expected tail
_L 0x2134BB7C 0x09B4BB00 // Write, Chair01 buymenu container
_L 0x2136A6E4 0x09B6A668 // Write, Chair02 buymenu container
_L 0x2134B924 0x09B4B8A8 // Write, Chair03 buymenu container
_L 0x2136B044 0x09B6AFC8 // Write, Chair04 buymenu container
_L 0x2134BC44 0x09B4BBC8 // Write, Chair05 buymenu container
_L 0x2134BAB4 0x09B4BA38 // Write, Chair06 buymenu container
_L 0x2136AD24 0x09B6ACA8 // Write, Chair07 buymenu container
_L 0x2134B9EC 0x09B4B970 // Write, Chair08 buymenu container
_L 0x2136A48C 0x09B6A410 // Write, Chair09 buymenu container
_L 0x2139EA1C 0x09B6AD70 // Write, Chair10 buymenu container
_L 0x2136AEB4 0x09B6AE38 // Write, Chair11 buymenu container
_L 0x2136D68C 0x09B6D548 // Write, Chair12 buymenu container
//

_L 0xE0FF1234 0x0136D68C // Check, ChairXX expected tail