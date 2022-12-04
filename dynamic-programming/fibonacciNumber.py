'''
https://leetcode.com/problems/fibonacci-number/
'''
def main():
    n = int(input("Enter number: "))
    if n <= 1:
        print(1)
        return 0
    f0,f1 = 0,1
    for i in range(1,n):
        fn = f0 + f1
        f0,f1 = f1,fn
    print(fn)
    return 0

if __name__ == '__main__':
    main()
