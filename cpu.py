import test_alu

class CPU:
    def __init__(self):
        self.a = 0
        self.x = 0
        self.y = 0
        self.pc = 0
        self.sp = 0xFD
        self.status = 0
        self.memory = [0] * 65536

    def execute_alu(self, operatie, register, waarde, bestemming):
        carry, zero, interrupt_disable, decimal, overflow, negative = test_alu.lees_status_register(self.status)

        resultaat, carry, overflow, zero, negative = test_alu.alu(operatie, register, waarde)

        if bestemming == "a":
            self.a = resultaat
        elif bestemming == "x":
            self.x = resultaat
        elif bestemming == "y":
            self.y = resultaat

        self.status = test_alu.maak_status_register(carry, zero, interrupt_disable, decimal, overflow, negative)

    def lees_adres(self, adres):
        lage_byte = self.memory[adres]
        hoge_adres = (adres + 1) & 0xFF
        hoge_byte = self.memory[hoge_adres]

        adres = (hoge_byte << 8) | lage_byte
        return adres

    def lda(self, waarde):
        self.a = waarde

        carry, zero, interrupt_disable, decimal, overflow, negative = test_alu.lees_status_register(self.status)

        if waarde == 0:
            zero = 1
        else:
            zero = 0

        negative = (waarde >> 7) & 1

        self.status = test_alu.maak_status_register(carry, zero, interrupt_disable, decimal, overflow, negative)

    def lda_absolute(self, adres):
        waarde = self.memory[adres]
        self.lda(waarde)

    def lda_zero_page(self, adres):   
        waarde = self.memory[adres]
        self.lda(waarde)

    def lda_absolute_x(self, adres):
        effectief_adres = self.memory[adres + self.x]
        waarde = effectief_adres
        self.lda(waarde)

    def lda_absolute_y(self, adres):
        effectief_adres = self.memory[adres + self.y]
        waarde = effectief_adres
        self.lda(waarde)

    def lda_zero_page_x(self, adres):
        effectief_adres = (adres + self.x) & 0xFF
        waarde = self.memory[effectief_adres]
        self.lda(waarde)

    def lda_indirect_y(self, adres):
        effectief_adres = self.lees_adres(adres) + self.y
        waarde = self.memory[effectief_adres]
        self.lda(waarde)

    def sta_indirect_y(self, adres):
        effectief_adres = (self.lees_adres(adres) + self.y) & 0xFFFF
        self.memory[effectief_adres] = self.a

    def sta_absolute(self, adres):
        self.memory[adres] = self.a

    def sta_absolute_x(self, adres):
        effectief_adres = adres + self.x
        self.memory[effectief_adres] = self.a

    def sta_zero_page(self, adres):
        self.memory[adres] = self.a

    def sta_zero_page_x(self, adres):
        effectief_adres = (adres + self.x) & 0xFF
        self.memory[effectief_adres] = self.a

    def stx_absolute(self, adres):
        self.memory[adres] = self.x

    def sty_absolute(self, adres):
        self.memory[adres] = self.y

    def stx_zero_page(self, adres):
        self.memory[adres] = self.x

    def sty_zero_page(self, adres):
        self.memory[adres] = self.y

    def stx_zero_page_y(self, adres):
        effectieve_adres = (adres + self.y) & 0xFF
        self.memory[effectieve_adres] = self.x

    def sty_zero_page_x(self, adres):
        effectieve_adres = (adres + self.x) & 0xFF
        self.memory[effectieve_adres] = self.y

    def cmp(self, waarde):
        carry, zero, interrupt_disable, decimal, overflow, negative = test_alu.lees_status_register(self.status)

        if self.a - waarde == 0:
            zero = 1
        else:
            zero = 0

        if self.a >= waarde:
            carry = 1
        else:
            carry = 0

        resultaat = (self.a - waarde) & 0xFF
        negative = (resultaat >> 7) & 1

        self.status = test_alu.maak_status_register(carry, zero, interrupt_disable, decimal, overflow, negative)

    def cpx(self, waarde):
        carry, zero, interrupt_disable, decimal, overflow, negative = test_alu.lees_status_register(self.status)

        if self.x - waarde == 0:
            zero = 1
        else:
            zero = 0

        if self.x >= waarde:
            carry = 1
        else:
            carry = 0

        resultaat = (self.x - waarde) & 0xFF
        negative = (resultaat >> 7) & 1

        self.status = test_alu.maak_status_register(carry, zero, interrupt_disable, decimal, overflow, negative)

    def cpy(self, waarde):
        carry, zero, interrupt_disable, decimal, overflow, negative = test_alu.lees_status_register(self.status)

        if self.y - waarde == 0:
            zero = 1
        else:
            zero = 0

        if self.y >= waarde:
            carry = 1
        else:
            carry = 0

        resultaat = (self.y - waarde) & 0xFF
        negative = (resultaat >> 7) & 1

        self.status = test_alu.maak_status_register(carry, zero, interrupt_disable, decimal, overflow, negative)

    def ldx(self, waarde):
        self.x = waarde

        carry, zero, interrupt_disable, decimal, overflow, negative = test_alu.lees_status_register(self.status)

        if waarde == 0:
            zero = 1
        else:
            zero = 0

        negative = (waarde >> 7) & 1

        self.status = test_alu.maak_status_register(carry, zero, interrupt_disable, decimal, overflow, negative)

    def ldy(self, waarde):
        self.y = waarde

        carry, zero, interrupt_disable, decimal, overflow, negative = test_alu.lees_status_register(self.status)

        if waarde == 0:
            zero = 1
        else:
            zero = 0

        negative = (waarde >> 7) & 1

        self.status = test_alu.maak_status_register(carry, zero, interrupt_disable, decimal, overflow, negative)

    def inx(self):
        self.x = (self.x + 1) & 0xFF

        carry, zero, interrupt_disable, decimal, overflow, negative = test_alu.lees_status_register(self.status)

        if self.x == 0:
            zero = 1
        else:
            zero = 0

        negative = (self.x >> 7) & 1

        self.status = test_alu.maak_status_register(carry, zero, interrupt_disable, decimal, overflow, negative)

    def iny(self):
        self.y = (self.y + 1) & 0xFF

        carry, zero, interrupt_disable, decimal, overflow, negative = test_alu.lees_status_register(self.status)

        if self.y == 0:
            zero = 1
        else:
            zero = 0

        negative = (self.y >> 7) & 1

        self.status = test_alu.maak_status_register(carry, zero, interrupt_disable, decimal, overflow, negative)

    def tax(self):
        self.x = self.a

        carry, zero, interrupt_disable, decimal, overflow, negative = test_alu.lees_status_register(self.status)

        if self.x == 0:
            zero = 1
        else:
            zero = 0

        negative = (self.x >> 7) & 1

        self.status = test_alu.maak_status_register(carry, zero, interrupt_disable, decimal, overflow, negative)

    def tay(self):
        self.y = self.a

        carry, zero, interrupt_disable, decimal, overflow, negative = test_alu.lees_status_register(self.status)

        if self.y == 0:
            zero = 1
        else:
            zero = 0

        negative = (self.y >> 7) & 1

        self.status = test_alu.maak_status_register(carry, zero, interrupt_disable, decimal, overflow, negative)

    def txa(self):
        self.a = self.x

        carry, zero, interrupt_disable, decimal, overflow, negative = test_alu.lees_status_register(self.status)

        if self.a == 0:
            zero = 1
        else:
            zero = 0

        negative = (self.a >> 7) & 1

        self.status = test_alu.maak_status_register(carry, zero, interrupt_disable, decimal, overflow, negative)

    def tya(self):
        self.a = self.y

        carry, zero, interrupt_disable, decimal, overflow, negative = test_alu.lees_status_register(self.status)

        if self.a == 0:
            zero = 1
        else:
            zero = 0

        negative = (self.a >> 7) & 1

        self.status = test_alu.maak_status_register(carry, zero, interrupt_disable, decimal, overflow, negative)

    def and_(self, waarde):
        resultaat = test_alu.alu("AND", self.a, waarde)[0]

        carry, zero, interrupt_disable, decimal, overflow, negative = test_alu.lees_status_register(self.status)

        self.a = resultaat

        if resultaat == 0:
            zero = 1
        else:
            zero = 0

        negative = (resultaat >> 7) & 1

        self.status = test_alu.maak_status_register(carry, zero, interrupt_disable, decimal, overflow, negative)

    def ora(self, waarde):
        resultaat = test_alu.alu("OR", self.a, waarde)[0]

        carry, zero, interrupt_disable, decimal, overflow, negative = test_alu.lees_status_register(self.status)

        self.a = resultaat

        if resultaat == 0:
            zero = 1
        else:
            zero = 0

        negative = (resultaat >> 7) & 1

        self.status = test_alu.maak_status_register(carry, zero, interrupt_disable, decimal, overflow, negative)

    def eor(self, waarde):
        resultaat = test_alu.alu("XOR", self.a, waarde)[0]

        carry, zero, interrupt_disable, decimal, overflow, negative = test_alu.lees_status_register(self.status)

        self.a = resultaat

        if resultaat == 0:
            zero = 1
        else:
            zero = 0

        negative = (resultaat >> 7) & 1

        self.status = test_alu.maak_status_register(carry, zero, interrupt_disable, decimal, overflow, negative)

    def asl(self):
        carry, zero, interrupt_disable, decimal, overflow, negative = test_alu.lees_status_register(self.status)
        
        resultaat, carry, _, _, _ = test_alu.alu("SHL", self.a, 0)

        self.a = resultaat

        if resultaat == 0:
            zero = 1
        else:
            zero = 0

        negative = (resultaat >> 7) & 1

        self.status = test_alu.maak_status_register(carry, zero, interrupt_disable, decimal, overflow, negative)

    def lsr(self):
        carry, zero, interrupt_disable, decimal, overflow, negative = test_alu.lees_status_register(self.status)
        
        resultaat, carry, _, _, _ = test_alu.alu("SHR", self.a, 0)

        self.a = resultaat

        if resultaat == 0:
            zero = 1
        else:
            zero = 0

        negative = (resultaat >> 7) & 1

        self.status = test_alu.maak_status_register(carry, zero, interrupt_disable, decimal, overflow, negative)

    def rol(self):
        carry, zero, interrupt_disable, decimal, overflow, negative = test_alu.lees_status_register(self.status)

        oude_carry = carry
        resultaat = ((self.a << 1) | oude_carry) & 0xFF

        nieuwe_carry = (self.a >> 7) & 1
        carry = nieuwe_carry

        self.a = resultaat

        if resultaat == 0:
            zero = 1
        else:
            zero = 0

        negative = (resultaat >> 7) & 1

        self.status = test_alu.maak_status_register(carry, zero, interrupt_disable, decimal, overflow, negative)

    def ror(self):
        carry, zero, interrupt_disable, decimal, overflow, negative = test_alu.lees_status_register(self.status)

        oude_carry = carry
        resultaat = (oude_carry << 7 | (self.a >> 1)) & 0xFF

        nieuwe_carry = self.a & 1
        carry = nieuwe_carry
        self.a = resultaat

        if resultaat == 0:
            zero = 1
        else:
            zero = 0

        negative = (resultaat >> 7) & 1

        self.status = test_alu.maak_status_register(carry, zero, interrupt_disable, decimal, overflow, negative)

    def adc(self, waarde):
        carry, zero, interrupt_disable, decimal, overflow, negative = test_alu.lees_status_register(self.status)

        resultaat = self.a + waarde + carry
        teken_a = (self.a >> 7) & 1
        self.a = resultaat & 0xFF
        carry = (resultaat >> 8) & 1

        if self.a == 0:
            zero = 1
        else:
            zero = 0

        negative = (self.a >> 7) & 1

        teken_waarde = (waarde >> 7) & 1
        teken_resultaat = (self.a >> 7) & 1

        if teken_a == teken_waarde and teken_resultaat != teken_a:
            overflow = 1
        else:
            overflow = 0

        self.status = test_alu.maak_status_register(carry, zero, interrupt_disable, decimal, overflow, negative)

    def sbc(self, waarde):
        carry, zero, interrupt_disable, decimal, overflow, negative = test_alu.lees_status_register(self.status)
        
        resultaat = self.a - waarde - (1 - carry)
        teken_a = (self.a >> 7) & 1

        if resultaat >= 0:
            carry = 1
        else:
            carry = 0

        self.a = resultaat & 0xFF

        if self.a == 0:
            zero = 1
        else:
            zero = 0

        negative = (self.a >> 7) & 1

        teken_waarde = (waarde >> 7) & 1
        teken_resultaat = (self.a >> 7) & 1

        if teken_a != teken_waarde and teken_resultaat != teken_a:
            overflow = 1
        else:
            overflow = 0

        self.status = test_alu.maak_status_register(carry, zero, interrupt_disable, decimal, overflow, negative)

    def dex(self):
        self.x = (self.x - 1) & 0xFF

        carry, zero, interrupt_disable, decimal, overflow, negative = test_alu.lees_status_register(self.status)

        if self.x == 0:
            zero = 1
        else:
            zero = 0

        negative = (self.x >> 7) & 1

        self.status = test_alu.maak_status_register(carry, zero, interrupt_disable, decimal, overflow, negative)

    def dey(self):
        self.y = (self.y - 1) & 0xFF

        carry, zero, interrupt_disable, decimal, overflow, negative = test_alu.lees_status_register(self.status)

        if self.y == 0:
            zero = 1
        else:
            zero = 0

        negative = (self.y >> 7) & 1

        self.status = test_alu.maak_status_register(carry, zero, interrupt_disable, decimal, overflow, negative)

    def dec(self, adres):
        carry, zero, interrupt_disable, decimal, overflow, negative = test_alu.lees_status_register(self.status)

        waarde = self.memory[adres]
        waarde = (waarde -1) & 0xFF
        self.memory[adres] = waarde

        if waarde == 0:
            zero = 1
        else:
            zero = 0

        negative = (waarde >> 7) & 1

        self.status = test_alu.maak_status_register(carry, zero, interrupt_disable, decimal, overflow, negative)

    def pha(self):
        adres = 0x0100 + self.sp
        self.memory[adres] = self.a
        self.sp = (self.sp - 1) & 0xFF

    def pla(self):
        carry, zero, interrupt_disable, decimal, overflow, negative = test_alu.lees_status_register(self.status)

        self.sp = (self.sp + 1) & 0xFF
        adres = 0x0100 + self.sp
        waarde = self.memory[adres]
        self.a = waarde

        if waarde == 0:
            zero = 1
        else:
            zero = 0

        negative = (waarde >> 7) & 1

        self.status = test_alu.maak_status_register(carry, zero, interrupt_disable, decimal, overflow, negative)

    def voer_programma_uit(self, programma):
        self.pc = 0

        while self.pc < len(programma):

            instructie, waarde = programma[self.pc]

            if instructie == "LDA":
                self.lda(waarde)

            elif instructie == "LDA_ABSOLUTE":
                self.lda_absolute(waarde)

            elif instructie == "LDA_ABSOLUTE_X":
                self.lda_absolute_x(waarde)

            elif instructie == "LDA_ZERO_PAGE":
                self.lda_zero_page(waarde)

            elif instructie == "LDA_ZERO_PAGE_X":
                self.lda_zero_page_x(waarde)

            elif instructie == "LDA_ABSOLUTE_Y":
                self.lda_absolute_y(waarde)

            elif instructie == "LDA_INDIRECT_Y":
                self.lda_indirect_y(waarde)

            elif instructie == "STA_ABSOLUTE":
                self.sta_absolute(waarde)

            elif instructie == "STA_ABSOLUTE_X":
                self.sta_absolute_x(waarde)

            elif instructie == "STA_INDIRECT_Y":
                self.sta_indirect_y(waarde)

            elif instructie == "STA_ZERO_PAGE_X":
                self.sta_zero_page_x(waarde)

            elif instructie == "STA_ZERO_PAGE":
                self.sta_zero_page(waarde)

            elif instructie == "STX_ABSOLUTE":
                self.stx_absolute(waarde)

            elif instructie == "STY_ABSOLUTE":
                self.sty_absolute(waarde)

            elif instructie == "STX_ZERO_PAGE":
                self.stx_zero_page(waarde)

            elif instructie == "STY_ZERO_PAGE":
                self.sty_zero_page(waarde)

            elif instructie == "STX_ZERO_PAGE_Y":
                self.stx_zero_page_y(waarde)

            elif instructie == "STY_ZERO_PAGE_X":
                self.sty_zero_page_x(waarde)

            elif instructie == "ASL":
                self.asl()

            elif instructie == "LSR":
                self.lsr()

            elif instructie == "ROL":
                self.rol()

            elif instructie == "ROR":
                self.ror()

            elif instructie == "ADC":
                self.adc(waarde)

            elif instructie == "SBC":
                self.sbc(waarde)

            elif instructie == "DEX":
                self.dex()

            elif instructie == "DEY":
                self.dey()

            elif instructie == "DEC":
                self.dec(waarde)

            elif instructie == "CMP":
                self.cmp(waarde)

            elif instructie == "CPX":
                self.cpx(waarde)

            elif instructie == "CPY":
                self.cpy(waarde)

            elif instructie == "AND_":
                self.and_(waarde)

            elif instructie == "ORA":
                self.ora(waarde)

            elif instructie == "EOR":
                self.eor(waarde)

            elif instructie == "LDX":
                self.ldx(waarde)

            elif instructie == "LDY":
                self.ldy(waarde)

            elif instructie == "JMP":
                self.pc = waarde

            elif instructie == "BEQ":
                carry, zero, interrupt_disable, decimal, overflow, negative = test_alu.lees_status_register(self.status)
                if zero == 1:
                    self.pc = waarde
                else:
                    self.pc += 1

            elif instructie == "BNE":
                carry, zero, interrupt_disable, decimal, overflow, negative = test_alu.lees_status_register(self.status)
                if zero == 0:
                    self.pc = waarde
                else:
                    self.pc += 1

            elif instructie == "INX":
                self.inx()

            elif instructie == "INY":
                self.iny()

            elif instructie == "TAX":
                self.tax()

            elif instructie == "TAY":
                self.tay()

            elif instructie == "TXA":
                self.txa()

            elif instructie == "TYA":
                self.tya()

            elif instructie == "PHA":
                self.pha()

            elif instructie == "PLA":
                self.pla()

            if instructie not in ("JMP", "BEQ", "BNE"):
                self.pc += 1
            print(self.pc)


programma = [
    ("LDA_ABSOLUTE", 100),
    ("TAX", 0),
    ("INX", 0),
    ("TXA", 0),
    ("TAY", 0),
    ("INY", 0),
    ("TYA", 0),
    ("BNE", 9),
    ("LDA", 0),
    ("LDX", 50)
]

cpu = CPU()

cpu.a = 42
cpu.sp = 0xFD

cpu.pha()

print(cpu.memory[0x01FD])
print(cpu.sp)
print(cpu.a)
