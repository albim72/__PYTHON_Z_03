from oldresistor import OldResistor


r0 = OldResistor(10.2E2)
print(f"______________ klasa {r0.__class__.__name__} _______________")
print(r0)
print(r0.get_ohms())
r0.set_ohms(5.5E2)
print(r0.get_ohms())
