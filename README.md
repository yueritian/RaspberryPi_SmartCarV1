# RaspberryPi_SmartCarV1
基于树莓派制作智能小车（H5页面操作移动+实时显示摄像头内容+各类传感器）

<img src="https://github.com/yueritian/RaspberryPi_SmartCarV1/blob/master/DocImages/model.jpg" width="600" alt="小车模型设计"/>
<img src="https://github.com/yueritian/RaspberryPi_SmartCarV1/blob/master/DocImages/car02.jpg" width="600" alt="小车照片"/>
<img src="https://github.com/yueritian/RaspberryPi_SmartCarV1/blob/master/DocImages/car01.jpg" width="600" alt="小车照片"/>
<img src="https://github.com/yueritian/RaspberryPi_SmartCarV1/blob/master/DocImages/car03.jpg" width="600" alt="小车照片"/>
<img src="https://github.com/yueritian/RaspberryPi_SmartCarV1/blob/master/DocImages/car04.jpg" width="600" alt="小车照片"/>
<img src="https://github.com/yueritian/RaspberryPi_SmartCarV1/blob/master/DocImages/car06.jpg" width="600" alt="小车照片"/>
<img src="https://github.com/yueritian/RaspberryPi_SmartCarV1/blob/master/DocImages/car07.jpg" width="600" alt="小车照片"/>

## 软件环境
> * 烧录系统：RASPBIAN STRETCH LITE 2018-04-18 （需要进行一系列配置，如开启SSH、摄像头、中文设置、更改源等）
> * 监控相关：<del>Nginx 1.14 + RTMP Module + Gstreamer + StrobeMediaPlayback</del>  mjpg-streamer182
> * 编写语言：Python 3.6.4
> * 其他使用：Python Flask组件，用于发布小车控制Web服务

## 硬件相关
### 组件
> * 树莓派3代
> * 降压板LM2596S：用于把12v电池组降压到树莓派供电需要的5v（我没有使用电机控制板的5v输出，因为未知原因连接后电机控制板烧了）
> * 电机控制板L298N：用于驱动电机（需要12v供电）
> * 红外避障传感器 * 2
> * 寻迹传感器
> * 超声波传感器
> * 摄像头500w像素（树莓派3代用）
> * 舵机（sg90） * 3
> * LCD1602（5v） + i2c接口
> * 无源蜂鸣器（5v，低电平触发）
> * 光敏传感器
> * RGB七彩灯
> * TT马达 * 2
> * 轮胎 * 2
> * 万向轮
> * 云台 * 3
> * 面包板
> * 两轮智能小车底盘
> * 18650电池组（12v 1800ma）

### 工具
> * 电烙铁（有的传感器的触角需要自行焊接）
> * 万用表（测量是否有短路，保护树莓派）
> * 迷你钻（购买的板子、云台等需要自行DIY）
> * 多头改锥
> * 镊子
> * 剪刀

### 耗材/其他
> * 小铜柱（可多购一些不同高度的）
> * 杜邦线（母母线，公母线，公公线）
> * M3螺丝（可多购一些不同长度的）
> * 电线（别买太细的）
> * 电气胶带（黑胶带）
> * 双面胶
> * 扎带
> * 开关
> * MicroUsb口的Usb线（越短越好）

## 使用介绍
> * 启动 mjpg-streamer
> * 启动 Flask
  
在使用过程中
> * 光感功能：当处于黑暗中，大灯会自动打开
> * 避障警告功能：当遇到障碍物，蜂鸣器会鸣叫，LCD屏幕会闪烁
> * 寻迹提示功能：当遇到黑色标记，蜂鸣器会鸣叫

## 遇到的坑
> * 这个版本的树莓派系统，默认的ssh等配置均需要手动开启，网卡也需要手动ifup
> * 所有软件安装后，建议做一个全系统的备份
> * Gstreamer安装的相关库较多，基本都需要安装
> * Python安装的时候，最好加上--with-ssl参数，否则后续安装组件的时候会报错，另外python最版本都需要自行编译安装
> * 树莓派的gpio针脚有的默认是高电平有的是低电平，在接入无源蜂鸣器的时候需要注意选择，另外需要注意触发的电平电压
> * LCD模块不支持中文（如果需要支持，还是别买这块了），而且需要的控制脚太多，所以买个i2c的转接模块是不错的选择
> * 最后，区别于软件开发，硬件开发需要做好周全准备，注意用电安全！

## 重大更新
> * 2018.6.15 rtmp方式，手机浏览器不支持flash，且使用ijkplayer做原生开发延迟较大，故换成mjpg-streamer方式。

## 敬请期待
> V1版本为临时起意的作品，作者是软件工程师出身，对硬件方面略懂，走了不少弯路，还好有个懂这方面知识的小伙伴 @Clliviaa 协助。
>> V2版本有几个想法，还未确定，想法包括：
>> * 采用乐高作为小车的结构材料
>> * 进一步探索各类传感器，尝试飞行器、水上作业器、双足机器人、多足机器人、双轮平衡车等
>> * 人工智能方面探索，基础的人脸识别、语音识别、人机对话等
