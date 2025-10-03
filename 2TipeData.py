data_integer= 99;
data_float = float(data_integer);
data_str =  str(data_integer);
data_bool = bool(data_integer);
print(f"data integer = {data_integer}, bertipe {type(data_integer)}");
print(f"data_float = {data_float}, bertipe = {type(data_float)}");
print(f"data_str = {data_str}, bertipe = {type(data_str)}");
print(f"data_bool = {data_bool}, bertipe = {type(data_bool)}");

# FLOAT 
print("====== Casting Float =======")
data_boolean = True;
data_integer2 = int(data_boolean);
data_str2 = str(data_boolean);
data_float2 = float(data_boolean);
print("data awal = ", data_boolean)
print(f"data integer = {data_integer2}, bertipe = {type(data_integer2)}");
print(f"data string = {data_str2}, bertipe = {type(data_str2)}");
print(f"data float = {data_float2}, bertipe = {type(data_float2)}");

# String
print("========= Casting String ===========");
data_string3 = "fahmi";
# data_integer3 = int(data_string3);
# data_float3 = float(data_string3);
data_boolean3 = bool(data_string3);
print(f"orignal data is {data_string3}, data types is {type(data_string3)}");
# print(f"data_integer = {data_integer3}, bertipe {type(data_integer3)}");
# print(f"data_string = {data_string3}, bertipe {type(data_string3)}");
print(f"data_boolean = {data_boolean3}, bertipe {type(data_boolean3)}");