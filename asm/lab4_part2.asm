.386
.MODEL FLAT, STDCALL
OPTION CASEMAP: NONE
include E:\masm32\include\windows.inc
include E:\masm32\include\kernel32.inc
include E:\masm32\include\user32.inc
includelib E:\masm32\lib\user32.lib
includelib E:\masm32\lib\kernel32.lib
.DATA
k db 1
n db 2
x dw 00001h,00000h,00000h, 00000h ; 8 bite
y dw 00001h,00000h,00000h,00000h ; 8 bite
s dd 2 dup(?)  
cons_2 dd 2
cons_8 dd 8
.CODE

t proc
MOV EAX,[ESP+4];EAX
MOV EBX,[ESP+8];EBX
CMP EAX,5
JA  j1;операнд_1 > операнд_2
INC EBX
j1:
MOV ECX,EAX
MOV EAX,EBX
CDQ
lop:
IMUL EBX
LOOPE lop
RET 8
t endp

cln proc
XOR EAX,EAX
XOR EBX,EBX
XOR EDI,EDI
XOR EBP,EBP
XOR EDX,EDX
RET 0
cln endp

START:
MOVZX ECX,n;СЧЁТЧИК
XOR ESI,ESI
CALL cln
j8:
MOVSX EBX,x[ESI]
MOVSX EAX,y[ESI]
CDQ
IMUL EAX
IMUL EBX
MOV EDI,2
IMUL EDI
XOR EDI,EDI
ADD EAX,EBX ;EAX=Xi+2*Xi*Yi*Yi
ADC EDX ,0
MOV EDI,EAX;  SAVE RES IN REGISTRS
MOV EBP,EDX
XOR EAX,EAX
XOR EDX,EDX
MOVSX EAX,y[ESI]
CDQ
IMUL EAX
IMUL y[ESI]
IMUL cons_8
ADD EDI,EAX
ADC EBP,EDX ;=Xi+2*Xi*Yi*Yi +8*Yi*Yi*Yi
;
PUSH EBX
PUSH ECX
XOR EBX,EBX
XOR ECX,ECX


JMP j6
j7:
XOR EAX,ECX
XOR ECX,EAX
XOR EAX,ECX
JMP j8
j6:

MOVSX EBX,x[ESI]
MOVZX ECX,k
CALL t;RETURN RES EDX:EAX

POP ECX
POP EBX

ADD EDI,EAX
ADC EBP,EDX

MOV EAX,s[0]
MOV EDX,s[4]

ADD EAX,EDI
ADC EDX,EBP
MOV s[0],EAX; SAVE RES
MOV s[4],EDX
;CLEAN
CALL cln

MOVSX AX,n
DEC AX
MOV n,AL

INC ECX
INC ECX

XOR EAX,ECX
XOR ECX,EAX
XOR EAX,ECX
LOOP j7

push NULL
call ExitProcess
END START