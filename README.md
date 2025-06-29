# 🦾 Miracle Robot Control Platform

本项目是一个基于 ROS 和 Qt/Poco 的机器人控制平台，支持通过网页前端控制机械臂、手指、腰部、颈部等模块，支持 CAN 总线通讯与文件上传执行功能。

---

## 📌 功能概览

- ✅ Web 前端控制界面（Qt + HTML）
- ✅ ROS 集成支持机械臂/手指控制
- ✅ 支持多种 joint 模式与数据同步
- ✅ 支持文件列表读取、上传与远程执行
- ✅ CAN 总线发送命令（ros_can 控制）
- ✅ CORS HTTP 静态资源服务器

---

## 🛠 项目结构

```bash
code/web_controller/
├── cors_http_server.py          # Python 静态文件服务（带 CORS）
├── pagehandler.h/.cpp           # 处理 HTTP 请求逻辑
├── web_server.h/.cpp            # 基于 Poco 的 HTTP 服务封装
├── fileuploadhandler.h/.cpp     # 文件上传接口
├── can_utils.h/.cpp             # CAN 总线通信封装
├── jointstate.h                 # 关节状态结构体封装
├── www/                         # 网页资源目录（index.html 等）
└── CMakeLists.txt               # 构建配置
code/ros_ws/
- ✅ rosbridge等相关依赖
