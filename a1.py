# # hàm sắp xếp(sort)
# def selection_sort(arr):
#     for i in range(len(arr)):
#         min_idx = i
#         for j in range(i + 1, len(arr)):
#             if arr[j] < arr[min_idx]:
#                 min_idx = j
#         arr[i], arr[min_idx] = arr[min_idx], arr[i]
# if __name__ == '__main__':
#     arr = [66, 25, 12, 22, 11]
#     print("danh sách ban đàu: ", arr)
#     selection_sort(arr)
#     print("danh sách sau khi sắp xếp: ", arr)

# #sắp xếp chèn
# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         pass
import random
a = input("nhập chuỗi bạn muốn đảo: ")
a = list(a)
n = len(a)

for i in range(n - 1, 0, -1):
    j = random.randint(0, i)
    a[i], a[j] = a[j], a[i]
input_string = ''.join(a)
print(input_string)  # In chuỗi