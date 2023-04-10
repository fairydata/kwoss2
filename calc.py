# get two integer parameters
# return sum
def plus(x, y):
    x1 = int (x)
    y1 = int(y)
    return x1+y1

# main function
def main():
    check = 11
    
    
    print("Welcome to calcuator")
    while check >= 1:        
        print("0: exit, 1: plus")
        check = int(input())
        if check == 1:
            fn = 2
            sn = 3
            while fn != 0:
                print("First Number")
                x = input()
                if not x.isdigit():
                    print("잘못된 값입니다. 다시 입력해주세요")
                    x = 0
                else:
                    fn = 0
            while sn != 0:
                print("Second Number")
                y = input()
                if not y.isdigit():
                    print("잘못된 값입니다. 다시 입력해주세요")
                    y = 0
                else:
                    sn = 0
            
            print("answer : ", plus(x,y))
        elif check > 1:
            print("Unsupported")
        else:
            print("Thank you")

if __name__ == "__main__":
    main()