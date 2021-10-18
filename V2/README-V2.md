# 第二版能做到的事情

1. 回傳complie錯誤 
2. 使用JavaScript行號幫助使用者檢查
3. 改變docker容器運行邏輯，減少硬碟讀寫

1.![1633590809353](https://user-images.githubusercontent.com/29775017/137730856-2be83f15-e065-4f42-ab59-b88fa54c23aa.jpeg)

2.
![行數](https://user-images.githubusercontent.com/29775017/137731243-1614b819-dcb2-4e6b-b94a-d0ecf8d5a845.JPG)

## 實作細節

之前檢查```docker images```的時候，發現Dockerfile每次創建images之後再刪掉大概是1.23G的空間(gcc為底的image)，會造成大量硬碟空間寫入，對硬碟壽命不好，故使用參數```docker ...其餘省略 -v {{主機目錄}}:{{docker conatiner 目錄}} ...其餘省略``` 的方式在啟動容器時候即掛載資料夾，就可以讓容器編譯，並用```> {{不同地方輸出不同黨名}}.txt```將結果輸出(不論是編譯成功的執行結果或是有錯誤都是存在裡面)。

同時昨天提到的py執行cmd方法 Popen是為了讓外部等待，確定結果跑完再繼續，同時之後要設定run time error也可以有修改空間。

最後讀檔案再輸出就可以。




