import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Dữ liệu hàm lượng Natri (mg) trong ngũ cốc
data = [0, 340, 70, 140, 200, 180, 210, 150, 100, 130,
        140, 180, 190, 160, 290, 50, 220, 180, 200, 210]

# Tạo DataFrame
df = pd.DataFrame({'Hàm lượng Natri (mg)': data})

# Tạo biểu đồ hộp
plt.figure(figsize=(8, 6))
ax = sns.boxplot(y='Hàm lượng Natri (mg)', data=df)

# Tính toán các giá trị Q1, Q3, Median (Trung vị) và IQR
Q1 = df['Hàm lượng Natri (mg)'].quantile(0.25)
Q3 = df['Hàm lượng Natri (mg)'].quantile(0.75)
median = df['Hàm lượng Natri (mg)'].median()

# Thêm các đường kẻ và chú thích cho Q1, Q3 và Median
ax.axhline(Q1, color='blue', linestyle='--', label=f'Q1 = {Q1}')
ax.axhline(Q3, color='orange', linestyle='--', label=f'Q3 = {Q3}')
ax.axhline(median, color='green', linestyle='-', label=f'Median = {median}')

# Thêm chú thích vào biểu đồ
plt.title("Biểu đồ hộp cho Hàm lượng Natri trong Ngũ Cốc")
plt.ylabel("Hàm lượng Natri (mg)")
plt.legend()

# Hiển thị biểu đồ
plt.grid(True)
plt.show()

