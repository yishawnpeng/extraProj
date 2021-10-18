# 第二版能做到的事情

1. 回傳complie錯誤 
2. 使用JavaScript行號幫助使用者檢查
3. 改變docker容器運行邏輯，減少硬碟讀寫

1.![1633590809353](https://user-images.githubusercontent.com/29775017/137730856-2be83f15-e065-4f42-ab59-b88fa54c23aa.jpeg)

2.
![行數](https://user-images.githubusercontent.com/29775017/137731243-1614b819-dcb2-4e6b-b94a-d0ecf8d5a845.JPG)

## 實作細節

之前檢查```docker images```的時候，發現Dockerfile每次創建images之後再刪掉大概是1.23G的空間(gcc為底的image)，會造成大量硬碟空間寫入，對硬碟壽命不好，故使用參數```docker ...其餘省略 -v {{主機目錄}}:{{docker conatiner 目錄}} ...其餘省略``` 的方式在啟動容器時候即掛載資料夾，就可以讓容器對他讀寫。

同時昨天提到的py執行cmd方法-- Popen是為了讓外部等待，確定結果跑完再繼續，同時之後要設定run time error也可以有修改空間。

最後讀檔案再輸出就可以。

### HTML

套用上別人寫好的css即可，同時設定邊界大小而不是自動。

### server

除了實作細節的docker容器指令不一樣之外，在編譯的時候指令後面多加參數```> {{不同地方輸出不同黨名}}.txt```將結果輸出，即可讀檔把資訊回傳。

