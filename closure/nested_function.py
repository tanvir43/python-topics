# Nested function is function which defined inside scope
# of another function

def enclosed_func(message):
    
    def nested_func():
        print(f"The message from enclosed funtion is {message}")
    return nested_func()

if __name__ == "__main__":
    enclosed_func("OK")