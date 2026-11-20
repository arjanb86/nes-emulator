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


cpu = CPU()
cpu.a = 25
cpu.execute_alu("SUB", cpu.a, 25, "a")

flags = test_alu.lees_status_register(cpu.status)

print("Accumulator:", cpu.a)
print("Zero:", flags)
