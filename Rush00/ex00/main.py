tasks = []

def main_menu():
    print("\n====== Smart Farm Task Organizer ======")
    print("1. เพิ่มงานในฟาร์ม")
    print("2. แสดงรายการงานทั้งหมด")
    print("3. ลบงาน")
    print("4. สรุปจำนวนงานในแต่ละประเภท")
    print("5. ค้นหางานตามคำค้น")
    print("6. แสดงงานตามวันที่")
    print("7. ออกจากโปรแกรม")

def main():
    while True:
        main_menu()
        choice = input("เลือกเมนู (1-7): ")
        if choice == '1':
            Select_option_1()
        elif choice == '2':
            Select_option_2()
        elif choice == '3':
            Select_option_3()
        elif choice == '4':
            Select_option_4()
        elif choice == '5':
            Select_option_5()
        elif choice == '6':
            Select_option_6()
        elif choice == '7':
            print("ขอบคุณที่ใช้โปรแกรม Smart Farm!")
            break
        else:
            print("ตัวเลือกไม่ถูกต้อง กรุณาลองใหม่")

def Select_option_1():
    task_name = input("ป้อนชื่องาน: ")
    task_date = input("ป้อนวันที่ (dd/mm/yyyy): ")
    task_type = input("ประเภทงาน (พืชผัก/ปศุสัตว์/อื่นๆ): ")
    tasks.append({"name": task_name, "date": task_date, "type": task_type})
    print("เพิ่มงานสำเร็จ")

def Select_option_2():
    if not tasks:
        print("ยังไม่มีงานในรายการ")
        return
    print("รายการงานทั้งหมด:")
    for i, task in enumerate(tasks):
        print(f"{i + 1}. {task['date']} - {task['name']} ({task['type']})")

def Select_option_3():
    if not tasks:
        print("ยังไม่มีงานในรายการ")
        return
    Select_option_2()
    try:
        task_number_to_delete = int(input("ลำดับของงานที่ต้องการลบ: ")) - 1
        if 0 <= task_number_to_delete < len(tasks):
            deleted_task = tasks.pop(task_number_to_delete)
            print(f"ลบงาน: {deleted_task['name']} เรียบร้อยแล้ว")
        else:
            print("ไม่พบงานตามลำดับที่ระบุ")
    except ValueError:
        print("กรุณาป้อนตัวเลขสำหรับลำดับงาน")

def Select_option_4():
    if not tasks:
        print("ยังไม่มีงานในรายการ")
        return
    task_summary = {}
    for task in tasks:
        task_type = task['type']
        task_summary[task_type] = task_summary.get(task_type, 0) + 1
    print("\nสรุปจำนวนงานแต่ละประเภท:")
    for task_type, count in task_summary.items():
        print(f"{task_type}: {count} งาน")

def Select_option_5():
    keyword = input("ป้อนคำค้นหางาน: ").lower()
    results = [task for task in tasks if keyword in task["name"].lower()]
    if results:
        print(f"\nพบ {len(results)} งานที่ตรงกับ '{keyword}':")
        for task in results:
            print(f"- {task['date']} - {task['name']} ({task['type']})")
    else:
        print("ไม่พบงานที่ค้นหา")

def Select_option_6():
    date = input("ป้อนวันที่ (dd/mm/yyyy): ")
    results = [task for task in tasks if task["date"] == date]
    if results:
        print(f"\nงานในวันที่ {date}:")
        for task in results:
            print(f"- {task['name']} ({task['type']})")
    else:
        print("ไม่มีงานในวันที่นี้")

if __name__ == "__main__":
    main()