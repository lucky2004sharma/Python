def info(name, age):
    print(name)
    print(age)
    print(f"My name is {name} and my age is {age}")
    

info('rahul', 21)    # both are positional arguments

info(name = 'shyam', age = 22)    # both are keywords arguments

info('rahul', age = 23)     # positional --> keywords    work fine

# info(name = 'shyam', 24)    # keyword--> positional      error cause
