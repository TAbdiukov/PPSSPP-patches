# Significance   
  
JAL(R) 3.1 ... 3.4 are the functions/logic identified to be clearly involved in menu options preprocessing  
  
If options are cut off at this point, then we will likely see it here.  
  
However, since the behavior is identical both at Home and in Park, the action removal logic is not here.  
  
## Listing jals 3.x  
  
* 0888FBAC (3.1, investigated)  
* 0888FBD4 (3.2)  
* 0888FC0C (3.3)  
* 0888FC2C (3.4, jalr)  
* 0887DF34 (Known "having already started" cutoff point)  
  
# investigating JAL 3.2 .. 3.4 - Home  
  
## JAL 3.2 (0888FBD4)   
  
→ 0882F4EC → 0882F4F0 (false) → 0882F500 (false) → 0882F510 (false)  
→ 0882F534 (jr ra)  
  
## JAL 3.3 (0888FC0C)  
  
→ 0888FE34 → 0888FE7C (false) → 0888FE98 (jalr)  
  
### JALR 3.3.1  
  
→ 088B757C → 088B7588 (false) → 088B75A0 (JALR)  
→→ JALR 3.3.1.1: 08B3711C (jr ra) → 088B75AC (back, jr ra)  
   
### JAL 3.3 back from 1  
  
→ 0888FEA0 → 0888FEA4 (jal 3.3.2)  
  
### JAL 3.3.2 (0888FEA4)  
  
→ 088C219C → 088C21A8 (jr ra)  
  
### JAL 3.3 back from 2  
  
→ 0888FEAC → 0888FEB0 (false) → 0888FEB8 (b) → 0888FF1C (jal 3.3.3)  
  
### JAL 3.3.3  
  
→ 088C1AA4 → 088C1AB4 (jr ra)  
  
### JAL 3.3 back from 3  
  
→ 0888FF24 → (long linear run) → 0888FFB8 (false) → 0888FFD0 (jalr)  
  
### JALR 3.3.4  
  
→ 088B757C → 088B7588 (false) → 088B75A0 (jalr)  
  
#### JALR 3.3.4.1  
  
→ 088B75A0 → jr ra  
  
### back from to JALR 3.3.4  
  
→ 088B75A8 → 088B75AC (jr ra)  
  
### JAL 3.3 back from 4  
  
→ 0888FFD8 → 08890018 (true) → 088900C4 (jalr)  
  
### JALR 3.3.5  
  
→ 08B39EE4 (jr ra)  
  
### JAL 3.3 back from 5  
  
→ 088900CC → 088900DC (jal)  
  
### JAL 3.3.6  
  
→ 0887ADE8 → 0887AE18 (jr ra)  
  
### JAL 3.3 back from 6  
  
→ 088900E4 → 088900E8 (jal)  
  
### JAL 3.3.7  
  
→ 0887ADB0 → 0887ADE0 (jr ra)  
  
### JAL 3.3 back from 7  
  
→ 088900F0 → 0889014C (jal)  
  
### JAL 3.3.8  
  
→ 08AD742C → 08AD7478 (false) → 08AD7490 (any: true/false) → (long run)  
→ 08AD7628 (b) → 08AD7668 (land)   
  
→ 08AD76B0 (false) → 08AD76BC (false) → 08AD76FC (JAL)  
  
#### JAL 3.3.8.1  
  
→ 08AD1230 → 08AD1274 (true) → 08AD127C (jr ra)  
  
### back from to JAL 3.3.8  
  
→ 08AD7704 (false) → 08AD7714 (false) → 08AD7754 (jal)   
  
#### JAL 3.3.8.2  
*same as JAL 3.3.8.1*  
  
→ 08AD1230 → 08AD1274 (true) → 08AD127C (jr ra)  
  
### back from to JAL 3.3.8  
  
→ 08AD775C (false) → 08AD7770 (jump back true)  
  
  
→ 08AD76B0 (false) → 08AD76BC (true)   
→ 08AD7714 (true) → 08AD7770 (jump back true)   
  
→ 08AD76B0 (false) → 08AD76BC (true)   
→ 08AD7714 (true) → 08AD7770 (jump back true)   
  
→ 08AD76B0 (false) → 08AD76BC (true)   
→ 08AD7714 (true) → 08AD7770 (jump back false)   
  
→ 08AD77B8 (jr ra to JAL 3.3)  
  
### JAL 3.3 back from 8  
  
→ 08890154 (false) → 0889016C (jalr)  
  
#### JALR 3.3.9  
  
→ 0881C2BC → 0881C2E0 (jal)  
  
##### JAL 3.3.9.1  
  
→ 088E9830 → 088E9834 (jr ra) → 0881C2E8 (false)   
→ 0881C300 (true) → 0881C310 (jal)  
  
###### JAL 3.3.9.1.1  
  
088F6474 → 088F647C (jr ra)   
  
##### Back from JAL 3.3.9.1.1 to 3.3.9.1  
  
→ 0881C318 (jal)  
  
###### JAL 3.3.9.1.2  
  
→ 088F67C4 → 088F67D8 (true) → 088F6810 → 088F6824 (jr ra)  
  
  
##### Back from JAL 3.3.9.1.2 to 3.3.9.1  
  
→ 0881C320 → 0881C324 (jal)  
  
###### JAL 3.3.9.1.3  
  
→ 088B946C → 088B9480 (false) → 088B9494 (true) →   
→ 088B9598 → 088B95A8 (jr ra)  
  
##### Back from JAL 3.3.9.1.3 to 3.3.9.1  
  
→ 0881C32C → 0881C330 (false) → 0881C33C (jal)   
  
###### JAL 3.3.9.1.4  
  
08809C34 → 08809C44 (false) → 08809C58 (false) → 08809C68 (jal)  
  
####### JAL 3.3.9.1.4.1  
  
08809C70 / 0881C344 - is a known location for settting up temporary bins/containers for actions. Already a cutoff.  
  
##### (Skip back) JAL 3.3 back from 9  
  
→ 08890174 (b) → 08890180 → 088901B0 (jr ra, end of jal 3.3)  
  
## back to JAL 3 from 3.3  
  
→ 0888FC14 (false) → 0888FC2C (jalr 3.4)  
  
### JALR 3.4 (0888FC2C)  
  
→ 088B757C → 088B7588 (false) → 088B75A0 (jalr)  
  
#### JALR 3.4.1   
  
→ 08B3711C (jr ra)  
  
### back to JALR 3.4 from 3.4.1  
  
→ 088B75A8 → 088B75AC (jr ra, end of jalr 3.4)  
  
# investigating JAL 3.2 .. 3.4 - Park  
  
## JAL 3.2 (0888FBD4)   
  
→ 0882F4EC → 0882F4F0 (false) → 0882F500 (false) → 0882F510 (false)  
→ 0882F534 (jr ra)  
  
## JAL 3.3 (0888FC0C)  
  
→ 0888FE34 → 0888FE7C (false) → 0888FE98 (jalr)  
  
### JALR 3.3.1  
  
→ 088B757C → 088B7588 (false) → 088B75A0 (JALR)  
→→ JALR 3.3.1.1: 08B3711C (jr ra) → 088B75AC (back, jr ra)  
   
### JAL 3.3 back from 1  
  
→ 0888FEA0 → 0888FEA4 (jal 3.3.2)  
  
### JAL 3.3.2 (0888FEA4)  
  
→ 088C219C → 088C21A8 (jr ra)  
  
### JAL 3.3 back from 2  
  
→ 0888FEAC → 0888FEB0 (false) → 0888FEB8 (b) → 0888FF1C (jal 3.3.3)  
  
### JAL 3.3.3  
  
→ 088C1AA4 → 088C1AB4 (jr ra)  
  
### JAL 3.3 back from 3  
  
→ 0888FF24 → (long linear run) → 0888FFB8 (false) → 0888FFD0 (jalr)  
  
### JALR 3.3.4  
  
→ 088B757C → 088B7588 (false) → 088B75A0 (jalr)  
  
#### JALR 3.3.4.1  
  
→ 088B75A0 → jr ra  
  
### back from to JALR 3.3.4  
  
→ 088B75A8 → 088B75AC (jr ra)  
  
### JAL 3.3 back from 4  
  
→ 0888FFD8 → 08890018 (true) → 088900C4 (jalr)  
  
### JALR 3.3.5  
  
→ 08B39EE4 (jr ra)  
  
### JAL 3.3 back from 5  
  
→ 088900CC → 088900DC (jal)  
  
### JAL 3.3.6  
  
→ 0887ADE8 → 0887AE18 (jr ra)  
  
### JAL 3.3 back from 6  
  
→ 088900E4 → 088900E8 (jal)  
  
### JAL 3.3.7  
  
→ 0887ADB0 → 0887ADE0 (jr ra)  
  
### JAL 3.3 back from 7  
  
→ 088900F0 → 0889014C (jal)  
  
### JAL 3.3.8  
  
→ 08AD742C → 08AD7478 (false) → 08AD7490 (any: true/false) → 08AD74A8 (true) → (long run)  
→ 08AD7628 (b) → 08AD7668 (land)   
  
→ 08AD76B0 (false) → 08AD76BC (false) → 08AD76FC (JAL)  
  
#### JAL 3.3.8.1  
  
→ 08AD1230 → 08AD1274 (true) → 08AD127C (jr ra)  
  
### back from to JAL 3.3.8  
  
→ 08AD7704 (false) → 08AD7714 (false) → 08AD7754 (jal)   
  
#### JAL 3.3.8.2  
*same as JAL 3.3.8.1*  
  
→ 08AD1230 → 08AD1274 (true) → 08AD127C (jr ra)  
  
### back from to JAL 3.3.8  
  
→ 08AD775C (false) → 08AD7770 (jump back true)  
  
  
→ 08AD76B0 (false) → 08AD76BC (true)   
→ 08AD7714 (true) → 08AD7770 (jump back true)   
  
→ 08AD76B0 (false) → 08AD76BC (true)   
→ 08AD7714 (true) → 08AD7770 (jump back true)   
  
→ 08AD76B0 (false) → 08AD76BC (true)   
→ 08AD7714 (true) → 08AD7770 (jump back false)   
  
→ 08AD77B8 (jr ra to JAL 3.3)  
  
### JAL 3.3 back from 8  
  
→ 08890154 (false) → 0889016C (jalr)  
  
#### JALR 3.3.9  
  
→ 0881C2BC → 0881C2E0 (jal)  
  
##### JAL 3.3.9.1  
  
→ 088E9830 → 088E9834 (jr ra) → 0881C2E8 (false)   
→ 0881C300 (true) → 0881C310 (jal)  
  
###### JAL 3.3.9.1.1  
  
088F6474 → 088F647C (jr ra)   
  
##### Back from JAL 3.3.9.1.1 to 3.3.9.1  
  
→ 0881C318 (jal)  
  
###### JAL 3.3.9.1.2  
  
→ 088F67C4 → 088F67D8 (true) → 088F6810 → 088F6824 (jr ra)  
  
  
##### Back from JAL 3.3.9.1.2 to 3.3.9.1  
  
→ 0881C320 → 0881C324 (jal)  
  
###### JAL 3.3.9.1.3  
  
→ 088B946C → 088B9480 (false) → 088B9494 (true) →   
→ 088B9598 → 088B95A8 (jr ra)  
  
##### Back from JAL 3.3.9.1.3 to 3.3.9.1  
  
→ 0881C32C → 0881C330 (false) → 0881C33C (jal)   
  
###### JAL 3.3.9.1.4  
  
08809C34 → 08809C44 (false) → 08809C58 (false) → 08809C68 (jal)  
  
####### JAL 3.3.9.1.4.1  
  
08809C70 / 0881C344 - is a known location for settting up temporary bins/containers for actions. Already a cutoff.  
  
##### (Skip back) JAL 3.3 back from 9  
  
→ 08890174 (b) → 08890180 → 088901B0 (jr ra, end of jal 3.3)  
  
## back to JAL 3 from 3.3  
  
→ 0888FC14 (false) → 0888FC2C (jalr 3.4)  
  
### JALR 3.4 (0888FC2C)  
  
→ 088B757C → 088B7588 (false) → 088B75A0 (jalr)  
  
#### JALR 3.4.1   
  
→ 08B3711C (jr ra)  
  
### back to JALR 3.4 from 3.4.1  
  
→ 088B75A8 → 088B75AC (jr ra, end of jalr 3.4)  
