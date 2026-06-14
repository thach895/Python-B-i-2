player_records = [
    ("Levi", 120, 2500),
    ("SofM", 150),
    ("Optimus", 100, "N/A")
]


def calculate_bonus(matches, mmr):
    """
    Tính thưởng RP
    Bonus RP = (Matches * 10) + (MMR * 0.5)
    """
    return (matches * 10) + (mmr * 0.5)


def process_bonus(player_records):
    print("--- BẢNG TÍNH THƯỞNG RP ---")

    for record in player_records:

        print("Đang xử lý:", record)

        try:
            name = record[0]
            matches = record[1]
            mmr = int(record[2])

            bonus = calculate_bonus(matches, mmr)

            print(f"Tuyển thủ {name} nhận được {bonus} RP")

        except IndexError:
            name = record[0]
            print(f"{name}: Lỗi - Hồ sơ bị thiếu thông tin!")
            continue

        except ValueError:
            name = record[0]
            print(f"{name}: Lỗi - Dữ liệu MMR không hợp lệ!")
            continue


process_bonus(player_records)