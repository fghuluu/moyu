# moyu
基于青龙面板钉钉机器人推送摸鱼日历

* 第一步：青龙面板添加依赖项  
在依赖管理中python3中添加 requests

* 第二步：添加环境变量  

| 参数 | 说明 |
| ---- | ---- |
| access_token | 钉钉机器人access_token |
| secret | 钉钉机器人secret |

* 第三步：新建py文件  
在脚本管理处新建一个moyu.py文件，把这里的moyu.py文件内容复制进去

* 第四部：创建定时任务
```
# 命令
task moyu.py
```
设定好运行时间
