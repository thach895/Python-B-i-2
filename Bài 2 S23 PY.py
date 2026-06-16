import math
import os
from datetime import datetime

raw_files = [
    {
        "filename": "pod_ep1.mp3",
        "size_bytes": 4500,
        "duration_sec": 180,
        "upload_at": "2026-06-10"
    },
    {
        "filename": "movie_trailer.mp4",
        "size_bytes": 105000,
        "duration_sec": 145,
        "upload_at": "2026-06-31"
    },
    {
        "filename": "clip_short.mp4",
        "size_bytes": 8200,
        "duration_sec": 15,
        "upload_at": "2026-05-15"
    }
]


def calculate_disk_blocks(size_bytes, block_size=4096):
    return math.ceil(size_bytes / block_size)


def safe_create_dir(path):
    os.makedirs(path, exist_ok=True)


def parse_and_inspect_date(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        return None


def get_media_category(filename):
    if filename.lower().endswith(".mp3"):
        return "audio"
    return "video"


print("======== HỆ THỐNG QUẢN LÝ LƯU TRỮ RIKKEI MEDIA ======")

safe_create_dir("media_vault")

print("[SYSTEM] Kiểm tra hạ tầng lưu trữ... Hoàn tất.")
print("-" * 75)

success_count = 0

for media_file in raw_files:

    print(f"[TỆP TIN: {media_file['filename']}]")

    upload_date = parse_and_inspect_date(
        media_file["upload_at"]
    )

    if upload_date is None:
        print(
            f" + Trạng thái phân loại: 🔴 THẤT BẠI "
            f"(Lỗi: Định dạng ngày upload "
            f"'{media_file['upload_at']}' không tồn tại)"
        )
        print()
        continue

    disk_blocks = calculate_disk_blocks(
        media_file["size_bytes"]
    )

    category = get_media_category(
        media_file["filename"]
    )

    safe_create_dir(
        f"media_vault/{category}"
    )

    print(
        f" + Dung lượng thực tế: "
        f"{media_file['size_bytes']:,} Bytes"
    )

    print(
        f" + Số khối phân vùng "
        f"(4KB Block): {disk_blocks} Blocks"
    )

    print(
        f" + Trạng thái phân loại: "
        f"🟢 HỢP LỆ "
        f"(Lưu trữ vào thư mục '{category}')"
    )

    print()

    success_count += 1

print("=" * 56)

print(
    f"TIẾN ĐỘ QUÉT: Hoàn thành xử lý "
    f"{success_count}/{len(raw_files)} "
    f"tệp tin thành công. Hệ thống ổn định."
)