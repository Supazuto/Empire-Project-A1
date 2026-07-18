# =====================================================
#  weapon_shop/equip_item.py — คนรับผิดชอบ: ______________________
#  หน้าที่: ซื้อและสวมใส่อาวุธให้ลูกน้อง (เช็คเงื่อนไข 2 อย่างก่อน)
# =====================================================

def equip_item(person, weapon):
#   - เช็คเงิน: เงินของ person ไม่พอราคา weapon -> ซื้อไม่ได้
#   - เช็คอาวุธ: person มีอาวุธอยู่แล้ว (equipment ไม่ใช่ "ไม่มี") -> ใส่เพิ่มไม่ได้
#   - ผ่านทั้งคู่ -> หักเงิน, เปลี่ยน equipment เป็นชื่ออาวุธ, บวก bonus เข้า power
#   - return {"status": True/False, "message": ข้อความบอกผล}
    # TODO: เขียนโค้ดตรงนี้
    person_money = int(person["money"])
    weapon_price = int(weapon["price"])
    person_power = person["power"]
    equipment = person["equipment"]
    if person_money < weapon_price :
        if equipment != "ไม่มี" :
            return {"status" : False , "message" : "มีอาวุธอยู่แล้ว"}

    else:
        person_money -= weapon_price
        person_power += weapon["bonus"]
        person["power"] = person_power
        person["money"] = person_money
        person["equipment"] = weapon["name"]
        return {"status" : "True" , "message" : "ทำรายการสำเร็จ"}
    return {"status" : "False" , "message" : "เงินไม่พอ"}




# ทดสอบเฉพาะไฟล์ตัวเอง: พิมพ์  python -m weapon_shop.equip_item
if __name__ == "__main__":
    vito = {"name": "Vito", "money": 60000, "power": 5, "equipment": "ไม่มี"}
    gun = {"name": "ปืนพก 9mm", "price": 50000, "bonus": 5}

    print(equip_item(vito, gun))   # ต้องได้ status True
    print(vito)                    # เงินเหลือ 10000, power เป็น 10, equipment เป็นปืน
    print(equip_item(vito, gun))   # ครั้งที่สองต้องได้ "มีอาวุธอยู่แล้ว"
