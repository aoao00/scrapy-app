

# scrapy-app

这是一个用来爬去APP评论的爬虫，用于产品需求分析，仅供学习使用，非商用。

#安装/Installation

本爬虫使用的是Scrapy爬虫框架，[文档](https://docs.scrapy.org/en/latest/index.html)。

```bash
bash

pip install scrapy

git clone https://github.com/aoao00/scrapy-app.git

cd scrape-app/app

scrapy crawl app -o result.csv
```

这个时候爬虫已经在运行了。

结果会输出在根目录的result.csv文件中。

![数据实例](https://aoao0620-1257522220.cos.ap-shanghai.myqcloud.com/Snipaste_2019-03-22_09-03-15.png?q-sign-algorithm=sha1&q-ak=AKIDO1pg4D6fMi82d7yJXXh37knJ5DxevSpl&q-sign-time=1553219812;1553221612&q-key-time=1553219812;1553221612&q-header-list=&q-url-param-list=&q-signature=e5228a86908856614ccb892fdd877f6582053f87&x-cos-security-token=f284c7a7a4fc13e83715f6374e074f11271f265b10001)

# 注意事项

- 默认爬取1000条评论，可自行在app下appSpider.py下修改，过高可能导致IP被封
- 数据分析仅供学习使用

# 数据分析

```python
    com_score=scrapy.Field()  #评论的评价，通常1为差评、3为中评、5为好评
    com_content=scrapy.Field() #评论的内容
    com_time=scrapy.Field() #评论发布的时间
    com_weight=scrapy.Field() #评论的权重？
    com_likes=scrapy.Field() #评论被点赞的次数
    com_ver=scrapy.Field() #评论针对的版本
```

### 案例分析

#### 问题1：注册流程繁琐

问题分析：出于微信方面安全管理的需求，微信在最新几个版本里对于新账户的注册要求用户需要朋友助力验证，其初衷在于有效遏制微信账号被滥用的情况，但对于普通用户来说无异于是增加了入门难度，对于微信来说，注册是用户转化的第一个门槛，务必要简化其操作难度。

#### 问题2：微信7.0大版本更新后UI界面不适应以及个性化操作缺失

问题分析：大众审美难以统一，众口难调，7.0版本更新后一大改进是UI界面，部分用户反馈，UI界面设计的明度太高，导致聊天太过刺眼，微信提示音不能够自定义，对于某些机型的屏幕不兼容等等情况。

#### 问题3：微信占用内存现象严重，部分功能过多

问题分析：微信近几个版本引入小程序，朋友圈好友动态等多个功能的同时，是程序内存占用的牺牲，然而在用户反馈中可以发现，使用最多的功能实际上只有聊天和朋友圈，更关键的是程序的稳定性，流畅性需求。

### 构建需求池

| 需求分类 |   说明   |                   需求描述                   |                           场景描述                           |
| :------: | :------: | :------------------------------------------: | :----------------------------------------------------------: |
|  体验类  |  UI优化  |           解决注册流程中的指引问题           | 用户在进行注册验证中，对于邀请好友验证等步骤的操作不清楚，影响微信用户的转化 |
|  体验类  | 兼容问题 | 解决聊天界面针对部分屏幕尺寸机型的兼容性问题 | 用户在聊天界面使用输入法时，使得聊天窗口缩小为三行左右，阅读文字不方便 |
|  体验类  |  UI优化  |            解决交互界面过亮的问题            |           用户在使用软件的过程当中，认为界面过亮了           |
|  体验类  | 性能优化 |             解决内存占用大的问题             |         用户在使用一段时间后发现微信占用手机内容巨大         |
|  功能类  | 功能优化 |       解决用户本不能自定义提示音的问题       |       用户在使用过程中发现不能像旧版本一样自定义提示音       |
|  功能类  | 功能优化 |           解决全民K歌分享到朋友圈            |        用户发现在全名K歌的歌曲不能够分享到朋友圈当中         |
|  体验类  | 性能优化 |              解决界面流畅性问题              |       用户感受到使用软件过程当中对于多余功能导致的卡顿       |

