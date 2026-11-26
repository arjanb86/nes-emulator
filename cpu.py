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
                self.lda_absoulute_y(waarde)

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

cpu.x = 10
cpu.y = 200

cpu.status = 0b11000011
cpu.sty_zero_page_x(0xFA)

print(cpu.memory[0x04])
print(cpu.x)
print(cpu.y)
print(bin(cpu.status))