MOV AX , 0000H
MOV DS , AX

MOV CX , 1104H
MOV AX , 4224H
MOV [1010H] , AX
MOV [1060] , CX

ADD CX , [1010H]

MOV [1060H] , CX

HLT