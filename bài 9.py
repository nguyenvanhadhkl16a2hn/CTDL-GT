import random 
def phan_a():
    def factorial(n):
        if n == 0:
            return 1
        smaller_factorial = factorial(n - 1)
        result = n * smaller_factorial
        return result
def phan_b():
    def dem_chuoi(input_string):
        if input_string == "":
            return 0
        else:
            return 1 + dem_chuoi(input_string[1:])

    a = input("nhập chuỗi bạn muốn đếm: ")
    a1 = dem_chuoi(a)
    print(f"Độ dài của chuỗi '{a}' là {a1}.")
def phan_c():
    def swap(my):
        a = list(my)
        n = len(a)

        for i in range(n - 1, 0, -1):
            j = random.randint(0, i)
            a[i], a[j] = a[j], a[i]
        input_string = ''.join(a)
        print(input_string)
    my = input("nhập chuỗi bạn muốn đảo: ")
    swap(my)
if __name__ == '__main__':
    print("phần a: ")
    phan_a()
    print("phần_b: ")
    phan_b()
    print("phần c: ")
    phan_c()