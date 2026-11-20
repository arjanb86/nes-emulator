class CPU:
    def __init__(self):
        self.a = 0
        self.x = 0
        self.y = 0
        self.pc = 0
        self.sp = 0xFD
        self.status = 0

    def execute_alu(self, operatie, waarde):
        pass

    def execute_alu(self, operatie, register, waarde):
        resultaat, carry, overflow, zero, negative = alu(operatie, register, waarde)



cpu1 = CPU()
cpu2 = CPU()

cpu1.a = 15

print(cpu1.a)
print(cpu2.a)