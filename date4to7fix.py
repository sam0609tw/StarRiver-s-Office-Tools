import os

base_folder = r"\\192.168.1.213\scan"

for folder in os.listdir(base_folder):
    folder_path = os.path.join(base_folder, folder)

    if os.path.isdir(folder_path) and folder.isdigit():
        try:
            if folder.startswith("113113") or folder.startswith("113114"):
                # 裁切出正確的 7 碼
                fixed_name = folder[3:]  # 移除前面多餘的 113
                fixed_path = os.path.join(base_folder, fixed_name)

                if not os.path.exists(fixed_path):
                    os.rename(folder_path, fixed_path)
                    print(f"🔧 修復資料夾名稱：{folder} ➜ {fixed_name}")
                else:
                    print(f"⚠️ 已存在正確資料夾 {fixed_name}，跳過 {folder}")
        except Exception as e:
            print(f"❌ 修復 {folder} 時錯誤：{e}")

input("\n🛠️ 修復作業完成，請按 Enter 鍵關閉...")
