def tim_max_min_de_quy(arr, n):
    if n == 1:
        return arr[0], arr[0]
    
    max_con_lai, min_con_lai = tim_max_min_de_quy(arr, n - 1)
    hien_tai = arr[n - 1]
    
    max_gia_tri = max(hien_tai, max_con_lai)
    min_gia_tri = min(hien_tai, min_con_lai)
    
    return max_gia_tri, min_gia_tri

# Nhập giá trị n và dãy từ người dùng
n = int(input("Nhập số lượng phần tử n: "))
danh_sach = []
for i in range(n):
    phan_tu = int(input(f"Nhập phần tử thứ {i+1}: "))
    danh_sach.append(phan_tu)

# Sử dụng hàm để tìm giá trị lớn nhất và giá trị nhỏ nhất trong dãy
gia_tri_max, gia_tri_min = tim_max_min_de_quy(danh_sach, n)

print("Giá trị lớn nhất trong dãy là:", gia_tri_max)
print("Giá trị nhỏ nhất trong dãy là:", gia_tri_min)
