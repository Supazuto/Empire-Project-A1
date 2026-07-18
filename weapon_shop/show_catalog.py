# =====================================================
#  weapon_shop/show_catalog.py — คนรับผิดชอบ: thankyou
#  หน้าที่: แสดงรายการอาวุธทั้งหมดที่มีขาย
# =====================================================
from data import weapons_catalog

def show_catalog():
#   - print อาวุธทุกชิ้นใน weapons_catalog บรรทัดละชิ้น (รหัส, ชื่อ, ราคา, พลังโบนัส)
    for i in weapons_catalog :
        print(f"{i}: {weapons_catalog[i]}")
        
    pass


# ทดสอบเฉพาะไฟล์ตัวเอง: พิมพ์  python -m weapon_shop.show_catalog
if __name__ == "__main__":
    show_catalog()   # ต้องเห็นอาวุธครบ 3 ชิ้น
