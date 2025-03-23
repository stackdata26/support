# -*- coding: utf-8 -*-
"""Show in Map - DV

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/14nOMVVHnkKOyOLCeUwXKWv9eR6ZLgwqV
"""

import pandas as pd
from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
df = pd.read_csv('/content/drive/MyDrive/dataset/Vizualile/Police_Department_Incidents_-_Previous_Year__2016_.csv')
print(df.head())

!pip install folium pandas

import folium
import pandas as pd

# Tạo bản đồ trung tâm tại San Francisco
m = folium.Map(location=[37.77, -122.42], zoom_start=10)

# Lọc dữ liệu để lấy 100 vụ việc đầu tiên
df_filtered = df[['Y', 'X', 'Category']].dropna().head(1000)

# Thêm các điểm vào bản đồ
for index, row in df_filtered.iterrows():
    folium.Marker(
        location=[row['Y'], row['X']],
        popup=row['Category'],  # Hiển thị loại tội phạm khi bấm vào điểm
        icon=folium.Icon(color="red", icon="info-sign")
    ).add_to(m)

# Hiển thị bản đồ
m

import matplotlib.pyplot as plt
import seaborn as sns

# Chuyển đổi cột ngày thành định dạng datetime
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

# Tạo thêm cột 'Month' và 'Year' để phân tích theo thời gian
df["Month"] = df["Date"].dt.month
df["Year"] = df["Date"].dt.year

# Đếm số vụ việc theo ngày trong tuần
day_counts = df["DayOfWeek"].value_counts()

# Đếm số vụ việc theo khu vực cảnh sát
district_counts = df["PdDistrict"].value_counts()

# Đếm số vụ việc theo tháng trong năm
month_counts = df["Month"].value_counts().sort_index()

# Đếm số vụ việc theo giờ
df["Hour"] = pd.to_datetime(df["Time"], format="%H:%M", errors="coerce").dt.hour
hour_counts = df["Hour"].value_counts().sort_index()

# Vẽ biểu đồ
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Biểu đồ tội phạm theo ngày trong tuần
sns.barplot(x=day_counts.index, y=day_counts.values, ax=axes[0, 0], palette="Blues_d")
axes[0, 0].set_title("Số lượng tội phạm theo ngày trong tuần")
axes[0, 0].set_xlabel("Ngày")
axes[0, 0].set_ylabel("Số vụ")

# Biểu đồ tội phạm theo khu vực cảnh sát
sns.barplot(x=district_counts.index, y=district_counts.values, ax=axes[0, 1], palette="Reds_d")
axes[0, 1].set_title("Số lượng tội phạm theo khu vực cảnh sát")
axes[0, 1].set_xlabel("Khu vực")
axes[0, 1].set_ylabel("Số vụ")
axes[0, 1].tick_params(axis='x', rotation=90)

# Biểu đồ tội phạm theo tháng trong năm
sns.lineplot(x=month_counts.index, y=month_counts.values, ax=axes[1, 0], marker="o", color="green")
axes[1, 0].set_title("Xu hướng tội phạm theo tháng")
axes[1, 0].set_xlabel("Tháng")
axes[1, 0].set_ylabel("Số vụ")

# Biểu đồ tội phạm theo giờ trong ngày
sns.lineplot(x=hour_counts.index, y=hour_counts.values, ax=axes[1, 1], marker="o", color="purple")
axes[1, 1].set_title("Xu hướng tội phạm theo giờ trong ngày")
axes[1, 1].set_xlabel("Giờ")
axes[1, 1].set_ylabel("Số vụ")

plt.tight_layout()
plt.show()