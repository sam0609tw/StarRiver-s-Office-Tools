import os
import shutil
from datetime import datetime

# 🔧 修改為你要整理的資料夾
source_folder = r"C:\你的資料夾路徑"

def to_roc_date(timestamp):
    dt = datetime.fromtimestamp(timestamp)
    roc_year = dt.year - 1911
    return f"{roc_year:03d}{dt.strftime('%m%d')}"

for filename in os.listdir(source_folder):
    file_path = os.path.join(source_folder, filename)

    if os.path.isfile(file_path):
        modified_time = os.path.getmtime(file_path)
        folder_name = to_roc_date(modified_time)

        target_folder = os.path.join(source_folder, folder_name)
        os.makedirs(target_folder, exist_ok=True)
        shutil.move(file_path, os.path.join(target_folder, filename))
        print(f"✅ {filename} 已移動至 {folder_name}/")

print("🎉 所有檔案已依民國年月日整理完成。")
input("\n🎉 資料夾更名作業完成，請按 Enter 關閉...")