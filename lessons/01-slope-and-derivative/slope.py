"""บทที่ 1: ความชัน อนุพันธ์ และ gradient descent

รัน:  python3 lessons/01-slope-and-derivative/slope.py
ใช้ Python ล้วน ไม่ต้องติดตั้งอะไรเพิ่ม
"""


def slope(f, x, h):
    """ความชันเฉลี่ยของ f ระหว่าง x กับ x+h  (ผลต่างแนวตั้ง / ผลต่างแนวนอน)"""
    return (f(x + h) - f(x)) / h


def gradient_descent(df, x, lr, steps):
    """เดินลงเนินทีละก้าว: x ใหม่ = x เดิม - lr * ความชัน

    df    ฟังก์ชันที่คืนค่าอนุพันธ์ ณ จุด x
    lr    learning rate หรือขนาดก้าว
    คืน list ของ x ทุกก้าว รวมจุดเริ่มต้น
    """
    path = [x]
    for _ in range(steps):
        x = x - lr * df(x)
        path.append(x)
    return path


def section(title):
    print(f"\n=== {title} ===")


if __name__ == "__main__":
    # ---------------------------------------------------------------
    section("1) ความชันของ f(x) = x^2 ที่ x = 3 เมื่อ h เล็กลงเรื่อย ๆ")

    def square(x):
        return x * x

    for h in [1, 0.1, 0.01, 0.001, 0.0001]:
        print(f"h = {h:<7} ความชัน = {slope(square, 3, h):.6f}")
    print("ค่าที่คำนวณด้วยมือ: 2x = 6")

    # ---------------------------------------------------------------
    section("2) h เล็กเกินไป คอมพิวเตอร์คำนวณผิด (ข้อจำกัดของ double)")

    for h in [1e-8, 1e-12, 1e-16, 1e-20]:
        print(f"h = {h:<7} ความชัน = {slope(square, 3, h)}")

    # ---------------------------------------------------------------
    section("3) ตรวจกฎยกกำลัง: อนุพันธ์ของ x^3 คือ 3x^2")

    def cube(x):
        return x**3

    for x in [-2, 0, 1, 5]:
        print(f"x = {x:>2}  วัดด้วยโค้ด = {slope(cube, x, 1e-6):>10.4f}   สูตร 3x^2 = {3 * x * x}")

    # ---------------------------------------------------------------
    section("4) gradient descent หาจุดต่ำสุดของ f(x) = (x - 3)^2")

    def df(x):
        return 2 * (x - 3)  # อนุพันธ์ของ (x-3)^2 = x^2 - 6x + 9

    path = gradient_descent(df, x=0.0, lr=0.1, steps=30)
    for step in [0, 1, 2, 3, 5, 10, 20, 30]:
        x = path[step]
        print(f"ก้าวที่ {step:>2}: x = {x:.5f}   f(x) = {(x - 3) ** 2:.5f}")

    # ---------------------------------------------------------------
    section("5) โมเดลแรกของเรา: y = w * x  เรียนจากข้อมูล (x=2, y=10)")

    # loss(w) = (2w - 10)^2 = 4w^2 - 40w + 100   ดังนั้นอนุพันธ์คือ 8w - 40
    def dloss(w):
        return 8 * w - 40

    path = gradient_descent(dloss, x=0.0, lr=0.05, steps=20)
    for step in [0, 1, 2, 3, 5, 10, 20]:
        w = path[step]
        print(f"ก้าวที่ {step:>2}: w = {w:.5f}   ทำนาย y = {2 * w:.5f}   loss = {(2 * w - 10) ** 2:.5f}")
    print("คำตอบที่ถูกคือ w = 5 เพราะ 5 * 2 = 10")
