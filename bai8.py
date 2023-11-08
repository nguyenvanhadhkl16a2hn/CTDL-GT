def tim_kiem(x, arr):
    for i in range(len(arr)):
        if arr[i] == x:
            return i  # Trả về chỉ mục của phần tử x nếu tìm thấy
    
    return -1  # Trả về -1 nếu không tìm thấy phần tử x

# Nhập giá trị n từ người dùng
n = int(input("Nhập số phần tử trong mảng: "))
mang = []

# Nhập các phần tử của mảng từ người dùng
for i in range(n):
    phan_tu = int(input(f"Nhập phần tử thứ {i + 1}: "))
    mang.append(phan_tu)

# Phần tử cần tìm
x = int(input("Nhập phần tử cần tìm: "))

# Gọi hàm tìm kiếm
ket_qua = tim_kiem(x, mang)

if ket_qua != -1:
    print(f"Phần tử {x} được tìm thấy tại chỉ mục {ket_qua}.")
else:
    print(f"Phần tử {x} không tồn tại trong mảng.")
