def to_hop_chap(n, k):
    if k == 0 or k == n:
        return 1
    return to_hop_chap(n - 1, k - 1) + to_hop_chap(n - 1, k)

#Hàm kiểm tra chức năng của hàm to_hop_chap
def test_to_hop_chap():
    n = int(input("Nhập giá trị n: "))
    k = int(input("Nhập giá trị k: "))
    
    result = to_hop_chap(n, k)
    print(f"C({n}, {k}) = {result}")

if __name__ == "__main__":
    test_to_hop_chap()
