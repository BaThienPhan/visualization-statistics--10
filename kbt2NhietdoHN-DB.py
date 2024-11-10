import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Dữ liệu nhiệt độ trung bình của Hà Nội và Điện Biên qua các mốc thời gian
data = {
    'Thời gian': ['Tháng 1', 'Tháng 2', 'Tháng 3', 'Tháng 4', 'Tháng 5', 'Tháng 6', 'Tháng 7'],
    'Hà Nội': [23, 25, 28, 28, 32, 33, 35],
    'Điện Biên': [16, 24, 26, 26, 26, 27, 28]
}

# Chuyển dữ liệu thành DataFrame
df = pd.DataFrame(data)

# Chuyển đổi dữ liệu sang dạng long format để dễ dàng vẽ với seaborn
df_long = df.melt(id_vars=['Thời gian'], value_vars=['Hà Nội', 'Điện Biên'],
                  var_name='Thành phố', value_name='Nhiệt độ trung bình')

# Vẽ biểu đồ nhiệt độ qua các mốc thời gian
plt.figure(figsize=(10, 6))
sns.lineplot(data=df_long, x='Thời gian', y='Nhiệt độ trung bình', hue='Thành phố', marker='o')
plt.title("Nhiệt độ trung bình của Hà Nội và Điện Biên qua các tháng")
plt.xlabel("Thời gian")
plt.ylabel("Nhiệt độ trung bình (°C)")
plt.grid(True)
plt.show()
