def outer():
    print("hello ")
    
    def inner():
        print("world")
        
    inner()


outer()
