from oldresistor import OldResistor
from resistor import Resistor
from voltage import VoltageResistance


r0 = OldResistor(10.2E2)
print(f"______________ klasa {r0.__class__.__name__} _______________")
print(r0)
print(r0.get_ohms())
r0.set_ohms(5.5E2)
print(r0.get_ohms())

r1 = Resistor(5.0E3)
print(f"______________ klasa {r1.__class__.__name__} _______________")
print(r1.ohms)
r1.ohms = 2.2E3
print(r1.ohms)

r2 = VoltageResistance(1.1E3)
print(f"______________ klasa {r2.__class__.__name__} _______________")
print(f'układ elektryczny - stan początkowy:\noporność: {r2.ohms} omów\nnapięcie prądu: {r2.voltage} V\n'
      f'natężenie prądu: {r2.current} A')
print("______________________________________________")
r2.voltage = 45
print(f'układ elektryczny - stan końcowy:\noporność: {r2.ohms} omów\nnapięcie prądu: {r2.voltage} V\n'
      f'natężenie prądu: {r2.current} A')


