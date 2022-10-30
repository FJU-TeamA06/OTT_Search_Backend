# OTT_Search_Backend
使用main.py來搜尋，會返回一個DataFrame格式的結果清單
語法:

    python3 main.py [搜尋字詞]
例子:

    python3 main.py 間諜家家酒
DataFrame格式如下:
-
Title排列:
![](image/Title.png)
Watch的排列跟Title對應
裡面有Platform和Url
![](image/Watch_1.png)
一個Title有多個Platform的情況:
![](image/Watch_2.png)