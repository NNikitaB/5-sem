;sum_int_2 proc a:DWORD, b:DWORD
;mov EAX, a
;add EAX, b
;ret
;sum_int_2 endp
;End LibMain

.386
.MODEL FLAT, STDCALL
OPTION CASEMAP: NONE
include E:\masm32\include\windows.inc
include E:\masm32\include\kernel32.inc
include E:\masm32\include\user32.inc
includelib E:\masm32\lib\user32.lib
includelib E:\masm32\lib\kernel32.lib
include E:\masm32\include\msvcrt.inc
includelib E:\masm32\lib\msvcrt.lib

;.DATA
;a DD 0,2,-1,-8,6,6,6,0,-7,7
;poss DD 10 dup(?)
;negs DD 10 dup(?)
;len DD 10
;poss_c DD 5
;.CONST
;N dd 16
.CODE

DllMain proc hlnstDLL:DWORD, reason:DWORD, unused:DWORD
mov EAX, 1
ret
DllMain Endp

_sort proc
	PUSH ECX 
	PUSH EBX
	PUSH ESI
	PUSH EDI
	PUSH EDX
	PUSH EAX
	PUSH EBP
	XOR EDX,EDX
	MOV ESI,[ESP+4*8]
	MOV EBP,[ESP+4*9]
	DEC EBP
	FINIT
for1:
	INC EDX
	
	MOV ECX,EDX
	MOV EDI,EDX
	DEC EDI
	for2:
	CMP ECX,0
	JBE  j8
	FLD DWORD PTR[ESI+ECX*4];J
	FLD DWORD PTR[ESI+EDI*4];J-1
	db 0dfh, 0f0h+1;;FCOMIP ST(0),ST(1)	
	JBE j9 ;JBE j9 ;X<=Y
	;x[j-1]<=x[j]
	
	;;;;;;SWAP
	MOV EAX,[ESI+ECX*4]
	MOV EBX,[ESI+EDI*4]
	MOV [ESI+ECX*4],EBX
	MOV [ESI+EDI*4],EAX
	;;;;;;SWAP
	
	j9:
	FFREE ST(0)
	DEC ECX
	DEC EDI
	JMP for2
	j8:
	
	CMP EDX,EBP;X<Y
	JL for1
		
	POP EBP
	POP EAX
	POP EDX
	POP EDI
	POP ESI
	POP EBX
	POP ECX
	RET 8
_sort endp


_ssort proc
	PUSH ECX 
	PUSH EBX
	PUSH ESI
	PUSH EDI
	PUSH EDX
	PUSH EAX
	PUSH EBP
	XOR EDX,EDX
	MOV ESI,[ESP+4*8]
	MOV EBP,[ESP+4*9]
	DEC EBP
	FINIT
for1:
	INC EDX
	
	MOV ECX,EDX
	MOV EDI,EDX
	DEC EDI
	for2:
	CMP ECX,0
	JBE  j8
	
	FLD DWORD PTR[ESI+EDI*4];J-1
	FLD DWORD PTR[ESI+ECX*4];J
	db 0dfh, 0f0h+1;;FCOMIP ST(0),ST(1)	
	JBE j9 ;JBE j9 ;X<=Y
	;x[j-1]<=x[j]
	
	;;;;;;SWAP
	MOV EAX,[ESI+ECX*4]
	MOV EBX,[ESI+EDI*4]
	MOV [ESI+ECX*4],EBX
	MOV [ESI+EDI*4],EAX
	;;;;;;SWAP
	
	j9:
	FFREE ST(0)
	DEC ECX
	DEC EDI
	JMP for2
	j8:
	
	CMP EDX,EBP;X<Y
	JL for1
		
	POP EBP
	POP EAX
	POP EDX
	POP EDI
	POP ESI
	POP EBX
	POP ECX
	RET 8
_ssort endp
;sum_int_2c proc stdcall a:DWORD, b:DWORD; 
sorts_arg proc stdcall a1:DWORD, a2:DWORD, a3:DWORD, a4:DWORD, a5:DWORD;
	PUSH ECX 
	PUSH EBX
	PUSH ESI
	PUSH EDI
	PUSH EDX
	MOV ESI,a1;FLOAT POS_RES
	MOV EDI,a2;FLOAT NEG_RES
	;MOV EBX,[ESP+4*8];INT * POS_COUNT
	MOV EBX,a4;FLOAT * A
	MOV ECX,a5;INT LENGHT
	XOR EDX,EDX
	CMP ECX ,0
	JLE j1  ;X<=0
	FINIT
	FLDZ
loop1:
	FLD DWORD PTR[EBX+EDX]
	db 0dfh, 0f0h+1;;FCOMIP ST(0),ST(1)	
	JB j3 ;X<0
	;;
	PUSH EDI
	PUSH ESI
	MOV EDI ,EBX
	ADD EDI,EDX
	MOV EAX ,ESI
	MOV ESI,EDI
	MOV EDI,EAX
	;;
	MOVSD [ESI],[EDI];;[EBX+EDX]
	POP ESI
	POP EDI
	ADD ESI,4
	JMP j4
	j3:
	;;
	PUSH ESI
	MOV ESI ,EBX
	ADD ESI,EDX
	;;
	MOVSD [EDI],[ESI];;[EBX+EDX]
	POP ESI
	;;ADD EDI,4;;��� �� EDI CHANGE SELF
	j4:
	ADD EDX,4
	loop loop1
	
	FFREE ST(0)
	SUB ESI,a1;FLOAT POS_RES
	SUB EDI,a2;FLOAT NEG_RES
	
	MOV ECX,4
	MOV EAX,ESI
	CDQ
	DIV ECX
	MOV ESI,EAX
	MOV EAX,EDI
	CDQ
	DIV ECX
	MOV EDI,EAX
	MOV EAX,a3
	MOV DWORD PTR [EAX],ESI;INT * POS_COUNT
	JMP j2
j1:
MOV EDI,0
MOV EAX,a3
MOV DWORD PTR [EAX],EDI;INT * POS_COUNT
	j2:
	MOV EAX,EDI
	
	PUSH ESI
	MOV ESI,a1;FLOAT POS_RES
	PUSH ESI
	CALL _sort
	PUSH EDI
	MOV EDI,a2;FLOAT NEG_RES
	PUSH EDI
	CALL _ssort
	

	
	POP EDX
	POP EDI
	POP ESI
	POP EBX
	POP ECX
	RET 20
sorts_arg endp ;;RET 20



;sum_int_2c proc c a:DWORD, b:DWORD; ����� cdecl
sortc_arg proc c a1:DWORD, a2:DWORD, a3:DWORD, a4:DWORD, a5:DWORD;
	PUSH ECX 
	PUSH EBX
	PUSH ESI
	PUSH EDI
	PUSH EDX
	MOV ESI,a1;FLOAT POS_RES
	MOV EDI,a2;FLOAT NEG_RES
	;MOV EBX,[ESP+4*8];INT * POS_COUNT
	MOV EBX,a4;FLOAT * A
	MOV ECX,a5;INT LENGHT
	XOR EDX,EDX
	CMP ECX ,0
	JLE j1  ;X<=0
	FINIT
	FLDZ
loop1:
	FLD DWORD PTR[EBX+EDX]
	db 0dfh, 0f0h+1;;FCOMIP ST(0),ST(1)	
	JB j3 ;X<0
	;;
	PUSH EDI
	PUSH ESI
	MOV EDI ,EBX
	ADD EDI,EDX
	MOV EAX ,ESI
	MOV ESI,EDI
	MOV EDI,EAX
	;;
	MOVSD [ESI],[EDI];;[EBX+EDX]
	POP ESI
	POP EDI
	ADD ESI,4
	JMP j4
	j3:
	;;
	PUSH ESI
	MOV ESI ,EBX
	ADD ESI,EDX
	;;
	MOVSD [EDI],[ESI];;[EBX+EDX]
	POP ESI
	;;ADD EDI,4;;��� �� EDI CHANGE SELF
	j4:
	ADD EDX,4
	loop loop1
	
	FFREE ST(0)
	SUB ESI,a1;FLOAT POS_RES
	SUB EDI,a2;FLOAT NEG_RES
	
	MOV ECX,4
	MOV EAX,ESI
	CDQ
	DIV ECX
	MOV ESI,EAX
	MOV EAX,EDI
	CDQ
	DIV ECX
	MOV EDI,EAX
	MOV EAX,a3
	MOV DWORD PTR [EAX],ESI;INT * POS_COUNT
	JMP j2
j1:
MOV EDI,0
MOV EAX,a3
MOV DWORD PTR [EAX],EDI;INT * POS_COUNT
	j2:
	MOV EAX,EDI
	
	PUSH ESI
	MOV ESI,a1;FLOAT POS_RES
	PUSH ESI
	CALL _sort
	PUSH EDI
	MOV EDI,a2;FLOAT NEG_RES
	PUSH EDI
	CALL _ssort
	

	
	POP EDX
	POP EDI
	POP ESI
	POP EBX
	POP ECX
	RET 
sortc_arg endp ;;RET 20


;sum_int_2p proc pascal a:DWORD, b:DWORD; ����� pascal
sortf proc
; ecx edx
    PUSH ECX 
	PUSH EBX
	PUSH ESI
	PUSH EDI
	PUSH EDX
	push edx
	push ecx
	MOV ESI,[ESP+4*6];FLOAT POS_RES
	MOV EDI,[ESP+4*7];FLOAT NEG_RES
	
	;MOV EBX,[ESP+4*8];INT * POS_COUNT
	MOV EBX,[ESP+4*9];FLOAT * A
	MOV ECX,[ESP+4*10];INT LENGHT
	XOR EDX,EDX
	CMP ECX ,0
	JLE j1  ;X<=0
	FINIT
	FLDZ
loop1:
	FLD DWORD PTR[EBX+EDX]
	db 0dfh, 0f0h+1;;FCOMIP ST(0),ST(1)	
	JB j3 ;X<0
	;;
	PUSH EDI
	PUSH ESI
	MOV EDI ,EBX
	ADD EDI,EDX
	MOV EAX ,ESI
	MOV ESI,EDI
	MOV EDI,EAX
	;;
	MOVSD [ESI],[EDI];;[EBX+EDX]
	POP ESI
	POP EDI
	ADD ESI,4
	JMP j4
	j3:
	;;
	PUSH ESI
	MOV ESI ,EBX
	ADD ESI,EDX
	;;
	MOVSD [EDI],[ESI];;[EBX+EDX]
	POP ESI
	;;ADD EDI,4;;��� �� EDI CHANGE SELF
	j4:
	ADD EDX,4
	loop loop1
	
	FFREE ST(0)
	SUB ESI,[ESP+4*6];FLOAT POS_RES
	SUB EDI,[ESP+4*7];FLOAT NEG_RES
	
	MOV ECX,4
	MOV EAX,ESI
	CDQ
	DIV ECX
	MOV ESI,EAX
	MOV EAX,EDI
	CDQ
	DIV ECX
	MOV EDI,EAX
	MOV EAX,[ESP+4*8]
	MOV DWORD PTR [EAX],ESI;INT * POS_COUNT
	JMP j2
j1:
MOV EDI,0
MOV EAX,[ESP+4*8]
MOV DWORD PTR [EAX],EDI;INT * POS_COUNT
	j2:
	MOV EAX,EDI
	
	PUSH ESI
	MOV ESI,[ESP+4*6+4];FLOAT POS_RES
	PUSH ESI
	CALL _sort
	PUSH EDI
	MOV EDI,[ESP+4*7+4];FLOAT NEG_RES
	PUSH EDI
	CALL _ssort
	
	pop eax
	pop edx
	
	POP EDX
	POP EDI
	POP ESI
	POP EBX
	POP ECX
	RET

sortf endp 



;sum_int_2c proc c a:DWORD, b:DWORD; ����� cdecl
sortc proc c
	PUSH ECX 
	PUSH EBX
	PUSH ESI
	PUSH EDI
	PUSH EDX
	MOV ESI,[ESP+4*6];FLOAT POS_RES
	MOV EDI,[ESP+4*7];FLOAT NEG_RES
	;MOV EBX,[ESP+4*8];INT * POS_COUNT
	MOV EBX,[ESP+4*9];FLOAT * A
	MOV ECX,[ESP+4*10];INT LENGHT
	XOR EDX,EDX
	CMP ECX ,0
	JLE j1  ;X<=0
	FINIT
	FLDZ
loop1:
	FLD DWORD PTR[EBX+EDX]
	db 0dfh, 0f0h+1;;FCOMIP ST(0),ST(1)	
	JB j3 ;X<0
	;;
	PUSH EDI
	PUSH ESI
	MOV EDI ,EBX
	ADD EDI,EDX
	MOV EAX ,ESI
	MOV ESI,EDI
	MOV EDI,EAX
	;;
	MOVSD [ESI],[EDI];;[EBX+EDX]
	POP ESI
	POP EDI
	ADD ESI,4
	JMP j4
	j3:
	;;
	PUSH ESI
	MOV ESI ,EBX
	ADD ESI,EDX
	;;
	MOVSD [EDI],[ESI];;[EBX+EDX]
	POP ESI
	;;ADD EDI,4;;��� �� EDI CHANGE SELF
	j4:
	ADD EDX,4
	loop loop1
	
	FFREE ST(0)
	SUB ESI,[ESP+4*6];FLOAT POS_RES
	SUB EDI,[ESP+4*7];FLOAT NEG_RES
	
	MOV ECX,4
	MOV EAX,ESI
	CDQ
	DIV ECX
	MOV ESI,EAX
	MOV EAX,EDI
	CDQ
	DIV ECX
	MOV EDI,EAX
	MOV EAX,[ESP+4*8]
	MOV DWORD PTR [EAX],ESI;INT * POS_COUNT
	JMP j2
j1:
MOV EDI,0
MOV EAX,[ESP+4*8]
MOV DWORD PTR [EAX],EDI;INT * POS_COUNT
	j2:
	MOV EAX,EDI
	
	PUSH ESI
	MOV ESI,[ESP+4*6+4];FLOAT POS_RES
	PUSH ESI
	CALL _sort
	PUSH EDI
	MOV EDI,[ESP+4*7+4];FLOAT NEG_RES
	PUSH EDI
	CALL _ssort
	

	
	POP EDX
	POP EDI
	POP ESI
	POP EBX
	POP ECX
	RET 
sortc endp ;;RET 20

;sum_int_2s proc stdcall a:DWORD, b:DWORD; ����� stdcall
sorts proc stdcall
	PUSH ECX 
	PUSH EBX
	PUSH ESI
	PUSH EDI
	PUSH EDX
	MOV ESI,[ESP+4*6];FLOAT POS_RES
	MOV EDI,[ESP+4*7];FLOAT NEG_RES
	;MOV EBX,[ESP+4*8];INT * POS_COUNT
	MOV EBX,[ESP+4*9];FLOAT * A
	MOV ECX,[ESP+4*10];INT LENGHT
	XOR EDX,EDX
	CMP ECX ,0
	JLE j1  ;X<=0
	FINIT
	FLDZ
loop1:
	FLD DWORD PTR[EBX+EDX]
	db 0dfh, 0f0h+1;;FCOMIP ST(0),ST(1)	
	JB j3 ;X<0
	;;
	PUSH EDI
	PUSH ESI
	MOV EDI ,EBX
	ADD EDI,EDX
	MOV EAX ,ESI
	MOV ESI,EDI
	MOV EDI,EAX
	;;
	MOVSD [ESI],[EDI];;[EBX+EDX]
	POP ESI
	POP EDI
	ADD ESI,4
	JMP j4
	j3:
	;;
	PUSH ESI
	MOV ESI ,EBX
	ADD ESI,EDX
	;;
	MOVSD [EDI],[ESI];;[EBX+EDX]
	POP ESI
	;;ADD EDI,4;;��� �� EDI CHANGE SELF
	j4:
	ADD EDX,4
	loop loop1
	
	FFREE ST(0)
	SUB ESI,[ESP+4*6];FLOAT POS_RES
	SUB EDI,[ESP+4*7];FLOAT NEG_RES
	
	MOV ECX,4
	MOV EAX,ESI
	CDQ
	DIV ECX
	MOV ESI,EAX
	MOV EAX,EDI
	CDQ
	DIV ECX
	MOV EDI,EAX
	MOV EAX,[ESP+4*8]
	MOV DWORD PTR [EAX],ESI;INT * POS_COUNT
	JMP j2
j1:
MOV EDI,0
MOV EAX,[ESP+4*8]
MOV DWORD PTR [EAX],EDI;INT * POS_COUNT
	j2:
	MOV EAX,EDI
	
	PUSH ESI
	MOV ESI,[ESP+4*6+4];FLOAT POS_RES
	PUSH ESI
	CALL _sort
	PUSH EDI
	MOV EDI,[ESP+4*7+4];FLOAT NEG_RES
	PUSH EDI
	CALL _ssort
	

	
	POP EDX
	POP EDI
	POP ESI
	POP EBX
	POP ECX
	RET 20
sorts endp 
;
;START:
;	PUSH len
;	PUSH offset a
;	PUSH offset poss_c
;	PUSH offset negs
;	PUSH offset poss
;	CALL sorts
;	CALL crt__getch
;	push NULL
;	call ExitProcess
;END START
End DllMain