def tim_phan_tu_lon_nhat_de_quy(S, n):
    # Trường hợp cơ bản: nếu dãy chỉ còn một phần tử, trả về phần tử đó
    if n == 1:
        return S[0]
    
    # Gọi đệ qui để tìm phần tử lớn nhất trong dãy con S[0:n-1]
    max_trong_dai_con = tim_phan_tu_lon_nhat_de_quy(S, n - 1)
    
    # So sánh phần tử lớn nhất trong dãy con với phần tử cuối cùng của dãy
    if max_trong_dai_con > S[n - 1]:
        return max_trong_dai_con
    else:
        return S[n - 1]

# Nhập giá trị n và dãy S từ người dùng
n = int(input("Nhập số lượng phần tử n: "))
S = []
for i in range(n):
    phan_tu = int(input(f"Nhập phần tử thứ {i+1}: "))
    S.append(phan_tu)

# Sử dụng hàm để tìm phần tử lớn nhất trong dãy S
phan_tu_lon_nhat = tim_phan_tu_lon_nhat_de_quy(S, n)
print("Phần tử lớn nhất trong dãy S là:", phan_tu_lon_nhat)
