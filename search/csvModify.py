import csv

head=160645
print(head)
with open("kkTV_All.csv", "r", newline="",encoding = "UTF-8") as csvfile:
    with open("kkTV_All_OK.csv", "w", newline="", encoding = "UTF-8") as csvfile1:
        fieldnames = ['Mid', 'Platform', 'Title','URL']
        writer = csv.DictWriter(csvfile1, fieldnames=fieldnames)
        writer.writeheader()

        # 讀取 CSV 檔內容，將每一列轉成一個 dictionary
        rows = csv.DictReader(csvfile)

        # 以迴圈輸出指定欄位
        for row in rows:
            print(row['Mid'])
            if int(row['Mid'])>=0:
                newMid=int(row['Mid'])+head
                writer.writerow({'Mid': str(newMid), 'Platform': row['Platform'], 'Title': row['Title'], 'URL': row['URL']})