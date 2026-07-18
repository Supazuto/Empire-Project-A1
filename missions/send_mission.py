# =====================================================
#  missions/send_mission.py — คนรับผิดชอบ: ______________________
#  หน้าที่: (OPTIONAL) ส่งลูกน้องไปเสี่ยงตายทำภารกิจ
# =====================================================

def send_mission(person):
#   - power ของ person >= 7 -> บวกเงินรางวัล 300000 เข้าเงินของ person
#     แล้ว return {"status": True, "reward": 300000}
#   - ไม่ถึงเกณฑ์ -> return {"status": False, "reward": 0}
#   (การลบคนที่ตาย main.py จัดการเอง)
    # TODO: เขียนโค้ดตรงนี้
    person_power = person["power"]
    person_money = person["money"]
    if person_power >= 7 :
        person_money += 300000
        person["money"] = person_money
        return True, "reward : 300,000"
    else:
        return False, "reward : 0"


# ทดสอบเฉพาะไฟล์ตัวเอง: พิมพ์  python -m missions.send_mission
if __name__ == "__main__":
    strong = {"name": "Tony", "power": 9, "money": 1000}
    weak = {"name": "Bob", "power": 2, "money": 1000}

    print(send_mission(strong))   # ต้องได้ status True, reward 300000
    print(strong)                 # เงินต้องกลายเป็น 301000
    print(send_mission(weak))     # ต้องได้ status False
