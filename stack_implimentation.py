## stack implementation
stack_dataset = []

class StackClass:
    def push(val):
        stack_dataset.append(val)
        return f"pushed value : {val}"

    def pop():
        if not stack_dataset:
            return f"error: stack is empty"
        return f"popped value : {stack_dataset.pop()}"
    
    def remove(val):
        if not stack_dataset:
            return f"error: stack is empty"
        return f"removed value : {stack_dataset.remove(val)}"\

    def display():
        return f"stack dataset: {stack_dataset}"

def stack_implementation(stack,item):
    try:
        if item == '1.push?':
            val = int(input("enter value to push : "))
            return stack.push(val)
        elif item == '2.pop?':
            return stack.pop()
        elif item == '3.remove?':
            val = int(input("enter value to remove : "))
            return stack.remove(val)
        elif item == '4.display?':
            return stack.display()
    except IndexError:
        print("error: Out of index range!!")
    except ValueError:
        print("error: entered value is not correct!! or enter value is not a integer")
    else:
        print("ooops something you did wrong")
    finally:
        print("Done!!!!")

try:
    print("working with stack!!")
    stack = StackClass()
    while True:
        collection_operation = ["1.push?", "2.pop?", "3.remove?", "4.display?", "5.exit?"]
        for item in collection_operation:
            data = input(f" {item} enter (Yes/no) : ")
            if data.lower() == 'yes' and item == '5.exit?':
                print("cleaning up the resources and exiting the program!!!!")
                stack_dataset.clear()
                print("resources cleaned and good byeee.....")
                exit()
            elif data.lower() == 'yes':
                print(stack_implementation(stack,item))
                print('-'*50)
        else:
            print("ooooops! we have only these many options..")
            ans = input("are you want to continue? (yes/no) : ")
            if ans == 'yes':
                continue
        break

except Exception as e:
    print(f"unknown exception : {e}")







    

