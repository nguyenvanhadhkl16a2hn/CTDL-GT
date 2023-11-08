def int_pow(x, n):
    if n == 0:
        return 1
    if n < 0:
        x = 1 / x
        n = -n
    if n % 2 == 0:
        half_pow = int_pow(x, n // 2)
        return half_pow * half_pow
    else:
        half_pow = int_pow(x, n // 2)
        return x * half_pow * half_pow

#Hàm kiểm tra chức năng của hàm int_pow
def test_int_pow():
    x = float(input("Nhập giá trị x: "))
    n = int(input("Nhập giá trị mũ n: "))
    
    result = int_pow(x, n)
    print(f"{x}^{n} = {result}")

if __name__ == "__main__":
    test_int_pow()
