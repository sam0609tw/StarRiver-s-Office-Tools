import os

# 🔧 修改為你要處理的路徑
base_folder = r"\\192.168.1.213\scan"

for folder in os.listdir(base_folder):
    folder_path = os.path.join(base_folder, folder)

    # 處理資料夾名稱為純數字
    if os.path.isdir(folder_path) and folder.isdigit():
        # 🛑 排除已是民國7碼格式的資料夾（如 1130703、1140625）
        if len(folder) == 7 and (folder.startswith("113") or folder.startswith("114")):
            print(f"⏭️ 已是正確格式，略過：{folder}")
            continue

        try:
            new_name = None

            # 11xx / 12xx ➜ 加上 113
            if folder.startswith("11") or folder.startswith("12"):
                new_name = "113" + folder
            # 01xx ~ 07xx ➜ 加上 114
            elif folder[:2] in [f"{i:02d}" for i in range(1, 8)]:
                new_name = "114" + folder

            if new_name:
                new_path = os.path.join(base_folder, new_name)

                if not os.path.exists(new_path):
                    os.rename(folder_path, new_path)
                    print(f"✅ {folder} ➜ {new_name}")
                else:
                    print(f"⚠️ 已存在：{new_name}，略過 {folder}")
        except Exception as e:
            print(f"❌ 更名 {folder} 時發生錯誤：{e}")
    else:
        print(f"🔎 略過無效資料夾：{folder}")

input("\n🎉 資料夾更名作業完成，請按 Enter 關閉...")
