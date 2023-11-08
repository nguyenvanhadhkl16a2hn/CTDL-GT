def dem_so_lan_xuat_hien(arr, x):
    if len(arr) == 0:
        return 0
    elif arr[0] == x:
        return 1 + dem_so_lan_xuat_hien(arr[1:], x)
    else:
        return dem_so_lan_xuat_hien(arr[1:], x)

# Hàm kiểm tra chức năng của hàm dem_so_lan_xuat_hien
def test_dem_so_lan_xuat_hien():
    arr = input("Nhập danh sách các số, cách nhau bằng dấu cách: ").split()
    arr = [int(item) for item in arr]
    x = int(input("Nhập số cần đếm: "))
    
    count = dem_so_lan_xuat_hien(arr, x)
    print(f"Số lần xuất hiện của số {x} trong danh sách là {count}")

if __name__ == "__main__":
    test_dem_so_lan_xuat_hien()
