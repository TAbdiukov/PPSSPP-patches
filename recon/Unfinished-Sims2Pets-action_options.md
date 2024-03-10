# Utilized addresses

Utilized addresses found, and they are static
```
08F0F99C - "Exchange $ to ¢"
08F0F9BC - "What are Pet Points?"
```

# Breakpoint on each addresses

Breakpoint on read. One byte is enough for the task

## At home

```
08B5E7C8: read 08F0F99C, afterwards jr to 0893EA4C
08B5E7C8: read 08F0F99C, afterwards jr to 0893EB2C
08B5E7C8: read 08F0F9BC, afterwards jr to 0893EA4C
08B5E7C8: read 08F0F9BC, afterwards jr to 0893EB2C

08B5E7C8: read 08F0F99C, afterwards jr to 0893EA4C
08B5E7C8: read 08F0F99C, afterwards jr to 0893EB2C
08B5E7C8: read 08F0F9BC, afterwards jr to 0893EA4C
08B5E7C8: read 08F0F9BC, afterwards jr to 0893EB2C

08AE0FEC: read 08F0F9BC (long), afterwards jr to 0897AA4C
0897B8C8: read 09C175E8 (?, according to debugger stats) 
```

## In park

```
08B5E7C8: read 08F0F99C, afterwards jr to 0893EA4C
08B5E7C8: read 08F0F99C, afterwards jr to 0893EB2C
08B5E7C8: read 08F0F99C, afterwards jr to 0893EA4C
08B5E7C8: read 08F0F99C, afterwards jr to 0893EB2C

08B5E7C8: read 08F0F9BC, afterwards jr to 0893EA4C
08B5E7C8: read 08F0F9BC, afterwards jr to 0893EB2C

08AE0FEC: read 08F0F9BC (long), afterwards jr to 


0897AA4C -> 088D5640 -> 08850158 (088502A8) -> 0882DDD4 -> 0882D794 -> 0887E06C -> 0888F85C -> 08890D40 -> 0887EA64 -> 0894AE04

0897B8C8: read ? 
08AE0FEC: read 08F0F9BC (long), afterwards jr to 0897AA4C -> 088D5640 -> 088502A8 ->
```


## Nopping instuctions

```
08B5E7C8 - no effect
0897B8C4 - empty texts
0897B8C8 - text corruption
```

## another breakpoint

At execution of 0x08AE0FEC , condition: **`a0==08F0F9BC`**

```
0882DDCC -> 0885014C (forces game to reload logic!) -> 088D5634 (3 calls, fetches names for Object actions) -> 0897AA40
```


3 calls are defined between: `0885014C` and `088D5634`,

```
Call 1 at: 08850150
Call 2 at: 088502A0
Call 3 at: 088502A0
```

# New functions to check

```
0882DCF8
0882DDC8
```

```
Home: 0882DD4C -> 0882D794 -> 0887E06C -> 0888F85C -> 08890D40 -> 0887EA64 -> 0894AE04 -> 08944710 -> 0894BA1C -> 08943848 -> 08943A34 -> 08944C7C -> 08944220 -> 08944100 -> 08811CFC -> 088113A4 -> 08A964DC -> 08A91470
Park: (unchecked)
```

Nop: 0882D78C - break actions

## 34 writes

```
0887D810 (home: 3F00FC24, park: 3E0AE99A)
0882DD00
```

### Values home

```
09A55290
09CFBA80
00000001
```

### Values park

```
09A55290
09D17C30
00000001

3F00FC24
```

# Park extra address values

```
09FFF260+0x34: 09D47790 (unconfirmed)
09FFF260+0x34: 09D17068
-> 09D19190 (set in 088F6838)
09FFF260+0x34: 09D19340 
```

a1= 09D19D68

# Save3


```
09D1AAF0 (1)
09D172A0 (2?)
09D56F68 (3)
```

# Watching change

### PARK

occurred in
```
0897A42C -> 088D5418 -> 088F6534 -> 088F6904 -> 
```


### HOME: 
```
0897A42C -> 088D5418 -> 088F6534 -> 088F6904 -> 0893EB64 -> 08809F48 -> 08809C70 -> 0881C344 ->
08890174 -> 0888FC14 -> 0887DF34 -> 
```

## Finding golden address

golden address = Only 1 call,

```
08809F48 - per X press
0893EB64 - per X press
088F6904 - per X press
088F6534 - per action count + 1
```

None found...

# Watching 1+4

```
Found: 088F654C
-> 088F6904 -> 
-> 0893EB64 -> 08809F48 -> 08809C70 -> 0881C344
-> 0882DD44 -> 0882D794 -> 0887E06C -> 
```

## Home

NONE


### Partial Conclusion

```
between 
088F6534 (action+1, ) and 088F654C (1+4) [maybe 088F6900 (Xpress lite), ]

12 12 123 123
```

I speculate this is a 'streaming function', waiting for the other thread


## Call list capture

```
09D1AAF0: 09D16818
09D1AAF4: 09D5C4D8
09D5C4D8 (quick: 0x08BE7F18) : 08C01920
09D5C4DC: 09D5B890
09D5B890: 08C01920
09D5B894: 00000000
```

Address for change: 08AF7CB8 and 08AF7CBC

### 08AF7CB8 (StepOut+)

```
-> 08ADF174 (nop=crash)
-> 08ADEF64 (nop=crash)
-> 08ADECFC
-> 08AA45A8
-> 08AA3BD8
-> 08835D48
-> 088113C8
-> 08A964DC
-> 08A91470
```


## Values alt

```
09D5F128: 09D16818
09D5F12C: 09D17C00
09D17C00: 08C01920
09D17C04: 09D00890
09D19CB0: 08C01920
09D19CB4: 00000000
```

1+4 write: 088F654C
```
-> 088F6904
-> 0893EB64
...
```

2+4 write: 088F654C


088F6544... - function of list entry generation
