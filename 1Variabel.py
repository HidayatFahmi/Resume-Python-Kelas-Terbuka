# assignment nilai pada varibel
a = 55
b = 77
z= a+b; 
print("nilai z adalah", z)

# Type Data
data_integer = 22
data_float = 9.8
nama = "fahmi"
print("data integer :", data_integer,"bertipe : ", type(data_integer))
print("adata_float : ", data_float,"bertipe : ",type(data_float))
print(f"Halo nama saya adalah {nama} saya baru memlai kembali coding denga python")
fahmi_single = True
print(f"apakaah fahmi single ? {fahmi_single}, tipe data dari status adalah {type(fahmi_single)}")

# tipe data bahasa C
from ctypes import c_double, c_char, c_long
data_c_double = c_double(10.45434534)
print(f"tipe data dari data_c_double : {type(data_c_double)}")