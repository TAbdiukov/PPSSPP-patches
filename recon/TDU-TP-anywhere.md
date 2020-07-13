# Project: TDU TP anywhere

## Milestones:

I. TP to marker

II. Put marker anywhere

III. Take care of the Height

## Essentials

Conseq | 32-bit conseq | Ltr | Literal meaning | Humane meaning
---- | ---- | ---- | ---- | ----
1 | 0(+8) | X | Left-Right | West - East
2 | 4(+8) | Y | Low-High | Ground - Sky (Height)
3 | 8(+8) | Z | Up-Down | North - South
4 | C(+8) | W | ??? | Unused here

### I. 

Implementation attempt: Redirect "Return struct" to "Marker struct" via hooking on reading

#### Reading table

Reading: 000008D49568 (return pos x)

**bold** for the candidates

##### Round 1

Address  |  Assembly | Thus struct pointer offset | On "sub.s f3, f3, f3" | Preliminary notes
----- | ---- |  ---- | ---- | ----
**08A1D250** |  lwc1  f3,0x30(v0) | 0x30 | Soft/Hardlock, no further reads | #1, passes >=1 frame till next . Sth core?
~~0894D858~~ | 	lwc1 f3,0x0(s0) | 0x0 | Nothing changes (2 times) | rep 2 times; seems to copy one struct to another - possibly for the long-term future ingame use
~~089D14A4~~ |	lwc1 f3,0x0(a1) | 0x0 | Nothing changes (2 times) | rep 2 times; Quick function/code block that quickly adds data down the struct 
~~0894D858~~ | - | | | Cascaded | 
~~089D14A4~~ | - | | | Cascaded |  
**08A87B74** | lwc1	f3,0x30(v0) | 0x30 | Game loads, but the car immediately is invinsible - signalling the TP occurred? | So far so good |  
~~08A18EA0~~ | lwc1	f3,0x0(v0) | 0x0 | Nothing changes (1 time) | Part of the HUGE function


##### Round 2

Address | From Round 1, on zeroing out | On immediate hotswapping and returning of values (Home -> Shop)
---- | ---- | ----
08A1D250 | Soft/Hardlock, no further reads | A ton of reads, but TP success
08A87B74 | Game loads, but the car immediately is invinsible - signalling the TP occurred? | TP success

##### for speed and flexibility: Try 08A87B74

```
old reading offset: 0x30
new reading offset: 
	000008D62400 (target pos X) - 000008D49568 (return pos) + 0x30 (initial)
=	0x08D62400 - 0x08D49568 + 0x30
=	0x18EC8
```
hmmm

V0 default: 08D49538

VO formed at:
08A87B08 -> 
0894D468


Specifically,
```
0x	00	00	00	00	| Beg
0x	08	D5	00	00	| LUI
0x	08	D4	94	14	| -0x6BEC
0x	08	D4	95	38	| +0x124 @ 0894D468
```

```
Target:
0)	0x000008D62400 - 0x30 =  0x8D623D0
1)	0x8D623D0 - 0x124 = 0x8D622AC

2)	0x08D50000 + X = 0x8D622AC
--	X = 0x8D622AC - 0x08D50000
--	X = 0x122AC
Try with addiu - not so easy
```


I think I know how to implement the safest way:

Address | Old | New | Notes
---- | ---- | ---- | ----
08A87B04 | 	lui	a0,0x8D5 | 	lui	a0,0x8D6 | aka lui. Loads hi
08A87B0C | 	addiu	a0,a0,-0x6BEC | 	addiu	a0,a0,0x22AC | lo fixup

It worked! Now to compile data info CWCheat


Address | Old ASM | New ASM | Old HEX | New HEX 
---- | ---- | ---- | ---- | ----
08A87B04 | 	lui	a0,0x8D5 | 	lui	a0,0x8D6 | 3C0408D5 | 3C0408D6
08A87B0C | 	addiu	a0,a0,-0x6BEC | 	addiu	a0,a0,0x22AC | 24849414 | 248422AC
