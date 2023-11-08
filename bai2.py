def tinh_harmonic(n):
    if n == 1:
        return 1
    else:
        return 1/n + tinh_harmonic(n - 1)

# Nhập giá trị n từ người dùng
n = int(input("Nhập giá trị n: "))

# Gọi hàm để tính số harmonic H(n)
harmonic = tinh_harmonic(n)

print(f"Số harmonic H({n}) là: {harmonic}")
