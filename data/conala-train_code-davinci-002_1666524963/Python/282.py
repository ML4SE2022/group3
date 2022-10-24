import threading

def function1():
    print("Hello")
    print("World")

def function2():
    print("Goodbye")
    print("World")

if __name__ == "__main__":
    threading.Thread(target = function1).start()
    threading.Thread(target = function2).start()