# Dữ liệu nhiệt độ đã sắp xếp
hanoi_temperatures = sorted([23, 25, 28, 28, 32, 33, 35])
dienbien_temperatures = sorted([16, 24, 26, 26, 26, 27, 28])

# Hàm tính trung vị (Q2)
def calculate_median(data):
    n = len(data)
    if n % 2 == 0:
        return (data[n // 2 - 1] + data[n // 2]) / 2
    else:
        return data[n // 2]

# Hàm tính tứ phân vị Q1 và Q3
def calculate_quartiles(data):
    n = len(data)
    
    # Q2 (Median)
    Q2 = calculate_median(data)
    
    # Q1: Median của nửa dưới (dữ liệu từ 0 đến n//2-1)
    lower_half = data[:n//2]
    Q1 = calculate_median(lower_half)
    
    # Q3: Median của nửa trên (dữ liệu từ n//2 đến hết)
    upper_half = data[(n+1)//2:]  # Đảm bảo không tính phần tử trung tâm nếu n là lẻ
    Q3 = calculate_median(upper_half)
    
    return Q1, Q2, Q3

# Tính các tứ phân vị cho Hà Nội
Q1_hanoi, Q2_hanoi, Q3_hanoi = calculate_quartiles(hanoi_temperatures)

# Tính các tứ phân vị cho Điện Biên
Q1_dienbien, Q2_dienbien, Q3_dienbien = calculate_quartiles(dienbien_temperatures)

import matplotlib.pyplot as plt

# Dữ liệu cho biểu đồ
months = ["Tháng 1", "Tháng 2", "Tháng 3", "Tháng 4", "Tháng 5", "Tháng 6", "Tháng 7"]

# Vẽ biểu đồ nhiệt độ
plt.plot(months, hanoi_temperatures, marker='o', color="blue", label="Hà Nội")
plt.plot(months, dienbien_temperatures, marker='o', color="orange", label="Điện Biên")

# Thêm các đường tứ phân vị cho Hà Nội
plt.axhline(y=Q1_hanoi, color='blue', linestyle='--', label="Q1 Hà Nội (25°C)")
plt.axhline(y=Q3_hanoi, color='blue', linestyle=':', label="Q3 Hà Nội (33°C)")

# Thêm các đường tứ phân vị cho Điện Biên
plt.axhline(y=Q1_dienbien, color='orange', linestyle='--', label="Q1 Điện Biên (24.5°C)")
plt.axhline(y=Q3_dienbien, color='orange', linestyle=':', label="Q3 Điện Biên (27°C)")

# Thiết lập tiêu đề và nhãn trục
plt.title("Nhiệt độ trung bình của Hà Nội và Điện Biên qua các tháng")
plt.xlabel("Thời gian")
plt.ylabel("Nhiệt độ trung bình (°C)")
plt.legend(loc="upper left")
plt.grid(True)

# Hiển thị biểu đồ
plt.show()
