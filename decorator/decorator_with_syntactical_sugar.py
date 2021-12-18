# Example of using decorator through `@` symbol

def decorated(func):
    def inner():
        print("I am pretty")
        func()
    return inner

@decorated
def clumsy():
    print("I am now decorated and looking pretty")

if __name__ == "__main__":
    clumsy()
