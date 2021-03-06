# extraProj
一個在Ubuntu利用Python Flask架構並且在Docker Container運行的網頁C/C++編譯器

A web C/C++ compiler that uses the Python Flask architecture in Ubuntu system and runs on Docker container

# 背景介紹和製作目的 Introduction and Purpose

我是2021年9月中原大學資訊工程學系和研究所4+1年畢業的彭義翔，在尋找工作的閒暇時間，多方學習以前求學少接觸但用途廣泛且常見的專業。

程式設計課程是資工系課程中重要的一部分，雖然系上已經有一個使用多年的C/C++編譯器供學生進行練習，但因為因為原授課教授準備光榮退休，而接下此教學重責的是我的指導教授，所以我在畢業之後主動爭取參與並設計最原始的架構，以期望能夠將所學回饋給母校，更借此挑戰自我。

原先使用的方法是自行開發Java JDK版本的桌面程式，因版本老舊，還有為了避免學生惡意破壞而額外增加大量防護，導致維護困難，因此我們希望使用學校內網和容器(Container)的機制重新設計架構，以達到不容易破壞(學校內網、皆於容器上運行)、查找問題容易(利用Log)的目的。

故我們的整體框架選擇利用Python的Flask套件架設網站，以便於管理不同的html和學生登入機制，同時，網頁提交時只會讀入字串以回傳至伺服器，再利用已經設定好的容器執行編譯和回傳結果(編譯錯誤或是執行結果)。

# 面對對象和其他設定 

預設對象是有一定資工基礎

以下是使用版本

![pythonversion](https://user-images.githubusercontent.com/29775017/137619269-c692cc7f-8a8c-402b-9ebd-06bde6db670d.JPG)

![dockeversion](https://user-images.githubusercontent.com/29775017/137619272-9ec1ba13-4fa0-4d43-86b6-b61c19a2377d.JPG)

python套件有os, flask, subprocess

```pip3 insatll os```其餘類推

若沒有管理套件pip3，則可先upgrade和update再執行以下指令:

```apt-get install python-pip```

要架設的ubuntu下載好Docker之後(網路很多Docker教學這是[其一](https://ithelp.ithome.com.tw/articles/10199339))

使用的[image](https://hub.docker.com/_/gcc?tab=description)是官方提供，或是在cmd裡面輸入即可下載

```docker pull gcc```


# 成果展示

成果簡單內部展示

![HI示範](https://user-images.githubusercontent.com/29775017/137617775-c5eb0e9a-bf05-48c6-9659-329943534310.JPG)

成果簡單外部展示

![HI示範外部](https://user-images.githubusercontent.com/29775017/137617786-19545e5c-9fc9-4dd9-8650-fdb007f5ff2f.JPG)

可以看到本地IP 0.0.0.0，port 5618 有簡單的展示，外部連線方式可利用ifconfig先確認此Ubuntu IP 即可直接訪問，

為了避免開發途中有別人意外連進來或是已經確定只給特定IP看到，[可利用ssh設定修改連線設定](https://seanhung365.pixnet.net/blog/post/212779848-ubuntu-%E5%AE%89%E8%A3%9D%E5%92%8C%E5%95%9F%E7%94%A8-ssh-%E7%99%BB%E5%85%A5)。

為了展示方便，其他成果統一以內部展示。

