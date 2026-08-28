def outer(name):
    print(f"hello {name}")
    
    def inner():
        print(f"world {name}")
        
        def inner_inner():
            print(f"welcome {name}  ")
            
        inner_inner()
        
    inner()


outer("mohit")
