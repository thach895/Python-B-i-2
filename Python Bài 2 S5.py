doanh_thu = []

for chi_nhanh in range(1, 4):

    ds_thang = []

    print(f"\n===== Chi nhánh {chi_nhanh} =====")

    for thang in range(1, 4):

        tien = int(input(f"Nhập doanh thu tháng {thang}: "))
        ds_thang.append(tien)

    doanh_thu.append(ds_thang)

for chi_nhanh in range(3):

    for thang in range(3):

        print(
            f"Chi nhánh {chi_nhanh + 1}, "
            f"tháng {thang + 1}: "
            f"{doanh_thu[chi_nhanh][thang]} triệu đồng"
        )