# Hàm đệ qui tính tổng các số lẻ từ 1 đến 2n + 1
def tong_so_le_de_quy(n):
    if n == 0:
        return 0
    return 2 * n - 1 + tong_so_le_de_quy(n - 1)

# Hàm sử dụng vòng lặp tính tổng các số lẻ từ 1 đến 2n + 1
def tong_so_le_vong_lap(n):
    total = 0
    for i in range(1, 2 * n + 2, 2):
        total += i
    return total

# Nhập giá trị n từ người dùng
n = int(input("Nhập giá trị n: "))

# Tính tổng số lẻ bằng đệ qui và vòng lặp
tong_de_quy = tong_so_le_de_quy(n)
tong_vong_lap = tong_so_le_vong_lap(n)

print(f"Tổng các số lẻ từ 1 đến 2n + 1 (đệ qui): {tong_de_quy}")
print(f"Tổng các số lẻ từ 1 đến 2n + 1 (vòng lặp): {tong_vong_lap}")
