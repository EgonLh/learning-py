# from oop import People

# em_1 = People("P-1","SWE");

# print(em_1)

# from schema import Schema,DataScheme
from schema import *;

data = Schema("A",12,"Data");

data.showInfo();

print("\nAnother Class\n")
# from Schema import DataScheme;

data_1 = DataScheme("Schema_1");

data_1.metaData.showInfo()

print("\nFrom Collection")
data2 = AnotherModule("Data Collection")

data2.showCollection()