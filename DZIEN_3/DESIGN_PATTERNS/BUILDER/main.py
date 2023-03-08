from builder import Builder
from director import Director
from concretebuilder1 import ConcreteBuilder

director = Director()
builder = ConcreteBuilder()
director.builder = builder

print("produkt podstawowy:")
director.build_minimal_version_product()
builder.product.list_parts()
print("\n__________________________________________")
print("produkt pełny: ")
director.build_full_version_product()
builder.product.list_parts()
print("\n__________________________________________")
print("produkt - wersja limitowana: ")
builder.produce_part_a()
builder.produce_part_c()
builder.product.list_parts()
