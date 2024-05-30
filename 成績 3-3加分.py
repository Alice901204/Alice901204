# 初始化變數
total_students = 0
pass_students = 0
total_score = 0

# 循環輸入成績
while True:
    score = input("請輸入學生成績（輸入 -1 表示結束）：")
    
    # 檢查是否輸入 -1 以結束輸入
    if score == "-1":
        break
    
    # 將輸入的字串轉換為整數
    score = int(score)
    
    # 更新計數器和總分
    total_students += 1
    total_score += score
    
    # 判斷及格與否
    if score >= 60:
        pass_students += 1

# 計算不及格人數
fail_students = total_students - pass_students

# 計算平均值
average_score = total_score / total_students if total_students > 0 else 0

# 輸出結果
print("全班人數：", total_students)
print("及格人數：", pass_students)
print("不及格人數：", fail_students)
print("全班平均值：", average_score)