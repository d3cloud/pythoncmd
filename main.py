import os

if __name__ == '__main__':
    print("Welcome to CMD Create by Ankit")
    while(True):
        x = input("Enter Command to run : ")
        if(x=="exit"):
            print("Goodbye")
            break
        os.system(x)
