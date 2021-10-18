# 第一版能做到的事情

1.從外部連線

2.提交程式碼送出即可得到執行結果

![結果](https://user-images.githubusercontent.com/29775017/137636943-69c55953-6eab-4488-a888-caeae0f59ab0.JPG)



## 實作細節

實際需要的程式只有兩個.py和templates 資料夾裡面的entrance.html。

在你想要架設的ubuntu server直接執行python3 server.py即可。

Dockerfile(唯一名稱 開頭D大寫其餘小寫)是外部測試及範例，onStudent.py會被server.py導入進去(import)。

### exec

docker 的指令可以讓你在server.py啟動的時候還是可以在容器裡面做事(另開cmd的概念)

### HTML

.html盡量和原始程式碼分開，這是一種開發習慣同時相對路徑好設定。

.html裡面的{{code}}, {{result}}, {{isSuccess}}的寫法是為了能讓呼叫他的py-flask架構可以從外部讀寫它的內容，蠻好用的。

### Dockerfile

Dockerfile 每次執行(直接執行)都會產生新的image去執行你的指令(我的範例有改變路徑、複製檔案、執行cmd)，範例中就是用安裝好的gcc名稱的image，然後複製我們事先存好的使用者字串做的cpp檔，再編譯並直接執行。

![nweimages](https://user-images.githubusercontent.com/29775017/137636995-b720d390-3277-4cda-8d7e-17626a3b2602.JPG)



### oneStudent

oneStudent是為了不讓多個使用者混淆的函數，利用python 套件subprocess，可模擬我們利用ubuntu cmd操作，還有Peop等方法，但我試過認為這個最簡單好用，可以選擇不回傳有沒有成功的資訊或是shell=True執行permission denied的狀況。

先創建該學號資料夾並複製cpp檔案，再創建Dockerfile寫入剛剛測試成功的資訊，利用剛剛創建的Dockerfile(build指令會自己找同位置的Dockerflie)，再把回傳資料做分割留下需要的就好，最後利用grep找到剛剛創建的image(Dockerfile 創建的容器默認執行成功會關掉，故若有問題需要手動刪除或是利用try關掉一勞永逸)，再把他移除掉 rmi(意義remove image，刪掉container是rm)，最後回到上層資料夾，就可以回傳結果。

![有問題要刪掉CONTAINER](https://user-images.githubusercontent.com/29775017/137636982-f0ad2b86-7cbc-4e74-8236-c5e415afdaee.JPG)


![查詢CONTAINER_id再刪掉](https://user-images.githubusercontent.com/29775017/137636984-643a64fb-e7ac-4c4a-b0dd-48400176387f.JPG)


### server

最重要的server.py因為flask套件所以和基本的py寫法有點不一樣，是利用
```@app.route("/{{使用者輸入的路徑}}",{{模式}})```
(若要使用者寫資料需要有post模式)，來決定要給使用者看的網頁畫面，可以簡單回傳字串或是
```render_template("{{網頁}}",{{html裡面用大括號保留的內容}})```
，若要讀取html的值，需要知道該欄位標籤的id，就可以利用
```tempCode=request.values["code"]```
的方式取

debug模式可以在開發時遇到問題出現類似下圖，不會無動於衷，很好用!

![有錯誤](https://user-images.githubusercontent.com/29775017/137636960-52833d00-0cb3-4da6-89ab-a639b184ef9d.JPG)



```app.config["JSON_AS_ASCII"] = False```可以解決傳遞字串亂碼的問題

最後
```app.run(host="0.0.0.0",port=5000)```
可指定本機執行ip和port就可以讓外部使用者利用{{本機ip:port}}來連線
