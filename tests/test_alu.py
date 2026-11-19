MAX_8BIT = 255


def optellen(accumulator, waarde):

    carry = 0
    overflow = 0

    totaal = waarde + accumulator
    oude_accumulator = accumulator
    accumulator = totaal % 256

    if totaal > MAX_8BIT:
        carry = 1

    if oude_accumulator <= 127 and waarde <= 127:
        if accumulator > 127:
            overflow = 1

    if oude_accumulator > 127 and waarde > 127:
        if accumulator <= 127:
            overflow = 1

    return accumulator, carry, overflow


def aftrekken(accumulator, waarde):

    carry = 0
    overflow = 0

    totaal = accumulator - waarde
    oude_accumulator = accumulator
    accumulator = totaal % 256

    if totaal >= 0:
        carry = 1

    if oude_accumulator <= 127 and waarde > 127:
        if accumulator > 127:
            overflow = 1

    if oude_accumulator > 127 and waarde <= 127:
        if accumulator <= 127:
            overflow = 1

    return accumulator, carry, overflow



def alu(operatie, a, b):

    zero = 0

    if operatie == "ADD":
       resultaat, carry, overflow = optellen(a, b)

    elif operatie == "SUB":
        resultaat, carry, overflow = aftrekken(a, b)

    elif operatie == "AND":
        resultaat = a & b
        carry = 0
        overflow = 0

    elif operatie == "OR":
        resultaat = a | b
        carry = 0
        overflow = 0

    elif operatie == "XOR":
        resultaat = a ^ b
        carry = 0
        overflow = 0

    elif operatie == "NOT":
        resultaat = (~a) & 0xFF
        carry = 0
        overflow = 0

    elif operatie == "SHL":
        resultaat = (a << 1) & 0xFF
        carry = (a >> 7) & 1
        overflow = 0

    elif operatie == "SHR":
        resultaat = (a >> 1) & 0xFF
        carry = a & 1
        overflow = 0
    
    if resultaat == 0:
        zero = 1
    else:
        zero = 0

    negative = (resultaat >> 7) & 1

    return resultaat, carry, overflow, zero, negative
  
print(alu("SUB", 25, 25))
print(alu("ADD", 100, 50))
print(alu("ADD", 28, 100))

# 0 t/m 127 = positief of nul.
# 128 t/m 255 = negatief.

# Accumulator: bevat altijd de 8-bit representatie (0–255).
# Carry: kijkt naar de unsigned berekening.
# Overflow: kijkt naar de signed berekening (-128 t/m 127).

# Bewerking	Python	Betekenis
# AND	&	Beide bits moeten 1 zijn
# OR	|	Minstens één bit is 1
# XOR	^	Bits zijn verschillend
# NOT	~	Bits omdraaien
# Shift left	<<	Bits naar links schuiven
# Shift right	>>	Bits naar rechts schuiven