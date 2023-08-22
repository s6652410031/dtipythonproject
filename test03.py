#แสดงข้อมูลหลายๆ ประเภทใน print เดียว
#1.ใช้ ,
print("SAU" ,555,123,456,True,10+50)
#2.ใช้ + มีข้อแม้ ข้อมูลที่ไม่ใช่ String ต้องเป็น String
print("SAU "+str(555)+' '+str(123.456)+' '+str(True)+' '+str(10+50))
#3. ใช้ Format
print("SAU {} {} {} {}" .format(555, 123.456, True, 10+50))
print("SAU {2} {3} {1} {0}" .format(555, 123.456, True, 10+50))
#4.ใช้ f-string ***
print( f'SAU {555} {123,456} {True} {10+50}')
#ในกรณี 1 บรรทัดมีหลาย statement คั้นด้วย ;
print("555");print("111");print(False)