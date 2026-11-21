import test_alu

class CPU:
    def __init__(self):
        self.a = 0
        self.x = 0
        self.y = 0
        self.pc = 0
        self.sp = 0xFD
        self.status = 0

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

    def lda(self, waarde):
        self.a = waarde

        carry, zero, interrupt_disable, decimal, overflow, negative = test_alu.lees_status_register(self.status)

        if waarde == 0:
            zero = 1
        else:
            zero = 0

        negative = (waarde >> 7) & 1

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



    def voer_programma_uit(self, programma):

        self.pc = 0

        while self.pc < len(programma):

            instructie, waarde = programma[self.pc]

            if instructie == "LDA":
                self.lda(waarde)

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

            if instructie not in ("JMP", "BEQ", "BNE"):
                self.pc += 1
            print(self.pc)


programma = [
    ("LDA", 10),
    ("LDX", 127),
    ("INX", 0),
    ("INY", 0),
    ("BNE", 5),
    ("LDY", 50)
]

cpu = CPU()
cpu.a = 0
cpu.tay()

print(cpu.a, cpu.x, cpu.y)
print(test_alu.lees_status_register(cpu.status))


