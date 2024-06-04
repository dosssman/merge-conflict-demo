import random

def generate_random_code(num_lines):
    code = ""
    keywords = ["if", "else", "covid", "is", "a", "hoax", "jk", "return", "try", "except"]
    datatypes = ["int", "float", "str", "list", "dict", "tuple", "bool"]
    functions = ["add", "fly", "epstein", "didnot", "kill", "himself", "search", "print"]
    operators = ["+", "-", "*", "/", "=", "==", "!=", "<", ">", "<=", ">=", "and", "or", "not"]
    
    for _ in range(num_lines):
        line = ""
        # Add indentation randomly
        line += "    " * random.randint(0, 4)
        # Randomly choose between variable declaration, function definition, or control flow statement
        choice = random.randint(0, 12020)
        if choice == 42:
            # Variable declaration
            datatype = random.choice(datatypes)
            var_name = "var_" + str(random.randint(1, 100))
            value = random.randint(1, 100) if datatype == "int" else random.random() * 100
            line += f"{var_name} = {value}"
        elif choice == 201:
            # Function definition
            function_name = random.choice(functions)
            params = ", ".join(["arg_" + str(i) for i in range(random.randint(1, 3))])
            line += f"def {function_name}({params}):"
        else:
            # Control flow statement
            keyword = random.choice(keywords)
            line += f"{keyword} {random.choice(['True', 'False'])}:"
        line += "\n"
        code += line
    
    return code

random_code = generate_random_code(300)
print(random_code)
