# moyu
基于青龙面板钉钉机器人推送摸鱼日历

>接口来源于微信公众号：摸鱼人日历

## * 第一步：青龙面板添加依赖项  
在依赖管理中python3中添加 requests

## * 第二步：添加环境变量  

| 参数 | 说明 |
| ---- | ---- |
| access_token | 钉钉机器人access_token |
| secret | 钉钉机器人secret |

## * 第三步：新建py文件  
在脚本管理处新建一个moyu.py文件，把这里的moyu.py文件内容复制进去  
若要在推送中附加其他内容参考[钉钉官方文档](https://open.dingtalk.com/document/robots/custom-robot-access)修改data中的内容

## * 第四部：创建定时任务
```
# 命令
task moyu.py
```
设定好运行时间 
```
# 周一至周五9点运行
0 9 * * 1-5
```
  
### 最终效果图如下：  
![image](https://github.com/fghuluu/moyu/assets/69468148/5e0ff50c-d165-437e-818d-26a5c99a8fa6)

  
## 申明  
本项目仅做学习交流, 禁止用于各种非法途径  
项目中的所有内容均源于互联网, 仅限于小范围内学习参考, 如有侵权请第一时间联系 本项目作者 进行删除
