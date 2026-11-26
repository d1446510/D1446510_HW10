# 共同設定
student_id = input("請輸入完整學號：").strip().upper()
tail = student_id[-3:]
a = int(student_id[-3])
b = int(student_id[-2])
c = int(student_id[-1])
s = a + b + c


# 第 2 題：整理兩場電子報活動的個人優惠碼
def collect_codes(raw_codes, saved=None):
    # 若未傳入 saved，建立新的空串列；若有傳入，複製一份避免修改原串列
    result = [] if saved is None else list(saved)

    for code in raw_codes:
        cleaned = code.strip().upper()
        # 略過空字串，且不重複加入
        if cleaned and cleaned not in result:
            result.append(cleaned)

    return result


# 建立初始資料
saved = ["BASE"]
raw_a = [" welcome" + tail + " ", "vip" + tail, "", "WELCOME" + tail, " "]
raw_b = [" new" + tail + " ", " welcome" + tail + " "]

# 依序呼叫函式
activity_a = collect_codes(raw_a, saved=saved)
activity_b = collect_codes(raw_b)

# 印出結果
print(f"學號：{student_id}")
print(f"活動A：{activity_a}")
print(f"活動B：{activity_b}")
print(f"原始saved：{saved}")
print(f"原始raw_a：{raw_a}")
print(f"空資料：{collect_codes([])}")
