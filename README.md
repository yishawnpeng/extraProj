# extraProj
一個在Ubuntu利用Python Flask架構並且在Docker Container運行的網頁C/C++編譯器

A web C/C++ compiler that uses the Python Flask architecture in Ubuntu system and runs on Docker container

# 背景介紹和製作目的 Introduction and Purpose

我是中原大學資訊工程學系和研究所4+1年於2021/9畢業的彭義翔，在找工作的閒暇時間，多方學習以前求學少接觸但之後可能會用到也常見的專業。

我要幫忙母校資工系重新架構C/C++的編譯器，因為以前沿用多年的方式因為原授課教授要退休，之後是我的指導教授來開班，故在畢業之後主動要求參與設計最原始的架構。

原授課教授使用的方法是自行開發Java JDK版本的桌面程式，因版本老舊而維護不易(還有為了避免學生惡意破壞額外加了大量手段)，我們要使用學校內網和容器(Container)的機制重新設計架構，以達到不容易破壞(學校內網、皆於容器上運行)、查找問題容易(利用Log)的目的。

# 面對對象和其他設定

我預設有一定資工基礎，

# 成果展示

成果簡單內部展示

![HI示範](https://user-images.githubusercontent.com/29775017/137617775-c5eb0e9a-bf05-48c6-9659-329943534310.JPG)

成果簡單外部展示

![HI示範外部](https://user-images.githubusercontent.com/29775017/137617786-19545e5c-9fc9-4dd9-8650-fdb007f5ff2f.JPG)

可以看到本地IP 0.0.0.0，port 5618 有簡單的展示，外部連線方式可利用ifconfig先確認此Ubuntu IP 即可直接訪問，

為了避免開發途中有別人意外連近來或是已經確定只給特定IP看到，[可利用ssh設定修改連線設定](https://seanhung365.pixnet.net/blog/post/212779848-ubuntu-%E5%AE%89%E8%A3%9D%E5%92%8C%E5%95%9F%E7%94%A8-ssh-%E7%99%BB%E5%85%A5)。

為了展示方便，其他成果統一以內部展示。

