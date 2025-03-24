def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"first" : "Jaziel", "last_name" : "Flores"}
    
    super_list = [
            {"fist" : "Jaziel", "last_name" : "Flores"}, 
            {"fist" : "David", "last_name" : "Rodríguez"}, 
            {"fist" : "Miguel", "last_name" : "Torres"}, 
            {"fist" : "Pepe", "last_name" : "Rodelo"}, 
            {"fist" : "Susana", "last_name" : "ADASA"}, 
            {"fist" : "A perro", "last_name" : "Gracía"}, 
            {"fist" : "XDDDD", "last_name" : "Sanchez"}
    ]

    super_dict = {
        "natural_nums" : [1, 2, 3, 4, 5],
        "integer_nums" : [-1, 1, -2, 2, 0],
        "floating_nums" : [1.23, 4.5, 6.3434]
    }
    
    for key,value in super_dict.items():
        print(key, "-", value)

    return 0
  
if __name__ == '__main__':
  run()
  
