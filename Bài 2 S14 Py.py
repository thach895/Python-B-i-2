def add_reward_points(current_points, points_earned):
    total = current_points + points_earned
    print("Đã cộng thêm", points_earned, "điểm.")
    return total


total_points = 100

total_points = add_reward_points(total_points, 50)

print("Tổng điểm hiện tại của khách hàng:", total_points)