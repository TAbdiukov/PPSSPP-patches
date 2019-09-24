# Vars
Addr | type
---- | ----
000008C457A5 | int 1 byte
000008C457E4 | int 1 byte
000009CA11CC | int 4 bytes

# b's
## 000008C457A5

B on | Type | Addr | Instr | Order | Comment 
---- | ---- | ---- | ---- | ---- | ----
000008C457A5 | W | 0886A6CC | 	sb	v1,0x26B5(a0) | 01 | set to c 8
000008C457A5 | W | 0886A880 | 	sb	s1,0x26B5(s5) | 02 | set to **4**
000008C457E4 | W | 08869BD4 | 	sh	s2,0x2730(s0) | 03 | set to 2? Wtf?
000008C457A5 | R | 08869BDC | 	lbu	v1,0x26B5(s0) | 04 | ld from E4
000008C457E4 | W | 08869BEC | 	sb	v1,0x26F4(s0) | 05 | set from E4

# Try hack

0886A870: Nop ->li s1, 0x7F

# RET
0902EE24 -> 08FC5318 -> 08FC53F0


# 000009CA991C

08FC3744
08FC7FC8
08FC53FC
