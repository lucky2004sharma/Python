def outer():
    print("hello ")
    
    def inner():
        print("world")
        
        def inner_inner():
            print("welcome")
            
        inner_inner()
        
    inner()


outer()
