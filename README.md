<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/header-dark.svg" />
  <img src="./assets/header.svg" width="100%" alt="czself — RoboMaster robot control and algorithms" />
</picture>

**完整实现 RoboMaster 步兵机器人整车电控。** 目前负责 **步兵改哨兵的算法开发**，记录控制实现、系统联调与算法开发的工程实践。

<a href="https://github.com/totrytakeoff/RM2026/tree/basic_framework">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="./assets/highlights-dark.svg" />
    <img src="./assets/highlights.svg" width="100%" alt="RoboMaster 1v1 步兵对抗赛全国二等奖；RM2026 步兵整车电控实现：底盘、云台、发射与遥控通信。" />
  </picture>
</a>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/stack-dark.svg" />
  <img src="./assets/stack.svg" width="100%" alt="C/C++, Python, STM32, FreeRTOS, ROS Noetic, Gazebo, OpenCV, YOLO, GMapping, AMCL, move_base, CAN/UART" />
</picture>

## 01 / RM2026：整车电控

在 **YZ Control** 战队协作项目中，完成步兵机器人的整车电控实现与联调。基于 **STM32F407**，把遥控输入、底盘运动、云台控制、发射机构与传感反馈连成完整的控制链路。

[赛季控制基线 ↗](https://github.com/totrytakeoff/RM2026/tree/basic_framework)　[当前框架分支 ↗](https://github.com/totrytakeoff/RM2026/tree/refactor/infantry-freertos)　[整车应用源码 ↗](https://github.com/totrytakeoff/RM2026/tree/refactor/infantry-freertos/applications/infantry)

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/control-loop-dark.svg" />
  <img src="./assets/control-loop.svg" width="100%" alt="步兵控制链路：遥控输入到机器人行为，再到 PID 与 CAN 电机执行；编码器和 IMU 反馈进入闭环。" />
</picture>

| 模块 | 技术要点 | 当前实现 |
| :--- | :--- | :--- |
| **底盘** | 运动学解算、坐标变换、云台跟随、小陀螺与轮速分配 | [chassis/](https://github.com/totrytakeoff/RM2026/tree/refactor/infantry-freertos/applications/infantry/chassis) |
| **云台** | Yaw / Pitch 控制、IMU 反馈、角度与速度状态切换、软硬限位 | [gimbal/](https://github.com/totrytakeoff/RM2026/tree/refactor/infantry-freertos/applications/infantry/gimbal) |
| **发射** | 摩擦轮与拨弹协同、单发 / 连发、扳机边沿与状态管理 | [shoot/](https://github.com/totrytakeoff/RM2026/tree/refactor/infantry-freertos/applications/infantry/shoot) |
| **输入与通信** | 遥控状态归一化、模式映射、CAN / UART 收发与掉线处理 | [command/](https://github.com/totrytakeoff/RM2026/tree/refactor/infantry-freertos/applications/infantry/command) |

<details>
<summary><b>深入看：FreeRTOS 运行时与工程验证</b></summary>

当前框架分支进一步梳理整车控制的任务边界与数据所有权：

- **任务职责**：姿态解算、整车控制、电机执行、健康监测分工；控制任务发布完整命令，电机任务独占 PID 状态与 CAN 输出。
- **状态一致性**：使用姿态快照和电机命令邮箱，处理跨任务共享状态；命令租约限制过期输出。
- **故障处理**：输入有效性、设备在线状态、任务健康和独立看门狗共同参与输出管理。
- **验证入口**：主机逻辑测试覆盖输入适配、运动学、云台限位、扳机状态与 PID reset；配套板级回归和链接审计。

[控制所有权设计](https://github.com/totrytakeoff/RM2026/blob/refactor/infantry-freertos/docs/migration/control_ownership_milestone.md) · [任务实现](https://github.com/totrytakeoff/RM2026/blob/refactor/infantry-freertos/firmware/infantry_f407/freertos/infantry_tasks.c) · [主机测试](https://github.com/totrytakeoff/RM2026/tree/refactor/infantry-freertos/tests/host)

这里展示的是后续框架重构分支；该分支的实板回归状态以仓库验收记录为准。

</details>

## 02 / 我的机器人开发技术栈

从下位机电控到 ROS 上位机，覆盖 **控制、视觉、建图定位、导航与系统联调**。以下技术用于 RM2026 电控、云台实验和 ROS / Gazebo 巡检项目。

| 方向 | 技术栈 | 具体实践 |
| :--- | :--- | :--- |
| **嵌入式与实时系统** | C / C++、STM32F407 / F103、HAL、FreeRTOS、CAN / UART、SPI / I²C | 外设与设备驱动接入、中断与 DMA、任务组织、通信协议解析、设备在线检测。 |
| **机器人运动控制** | PID、底盘运动学、Yaw / Pitch、编码器、BMI088 / IMU、姿态解算 | 底盘跟随与小陀螺、云台角度 / 速度闭环、坐标与单位统一、限位、模式切换及参数联调。 |
| **ROS 系统集成** | ROS 1 Noetic、rospy、TF、Topic、Actionlib、cv_bridge | 节点与消息接口对接、坐标变换、源帧时间戳关联、导航目标下发与执行状态反馈。 |
| **视觉感知** | Python、OpenCV、Ultralytics YOLO、RGB-D、PaddleOCR | 模型推理接入、目标检测、图像裁剪、置信度筛选、深度辅助定位、车牌 OCR 与结果可视化。 |
| **建图与定位** | GMapping、AMCL、map_server、LaserScan、里程计 | 二维 SLAM 建图、地图保存与加载、初始位姿配置、定位参数联调，以及 map / odom / base 坐标链检查。 |
| **导航与避障** | move_base、Navfn、costmap_2d、ForwardPathFollower | 全局路径规划、局部路径跟随、footprint 碰撞检查、激光与深度障碍接入、多点任务与到点航向控制。 |
| **仿真与工程调试** | Gazebo Classic、RViz、rosbag、VOFA+、GDB / OpenOCD | 仿真传感器接入、地图与路径可视化、运行数据记录、总线与控制遥测、烧录及故障定位。 |

**开发环境与构建**：Linux · Git · CMake · PlatformIO · Docker。

## 03 / 视觉联调与导航集成

这些实践主要来自 **[ROS / Gazebo 智慧社区巡检项目](https://github.com/czself/ros)**，涵盖感知结果接入、机器人运动配合与任务验收。

### 视觉与运动配合

- **相机 → ROS → 推理**：通过 `cv_bridge` 对接图像与 OpenCV / YOLO，检查源帧、时间戳、检测类别、置信度和输出频率。
- **检测 → 空间位置**：结合 `CameraInfo`、深度图与同源帧 TF，把图像观测关联到机器人 / 地图坐标，处理深度缺失、重复观测和结果过期。
- **识别 → 任务行为**：将交通灯检测结果接入通行条件；将人物检测接入位置关联与统计；对车牌进行 ROI 裁剪、PaddleOCR 识别和多帧结果核对。
- **到点 → 稳定取图**：联调导航位置、航向、拍照时机与目标画面范围，保留原图、标注图、识别结果及源帧信息。

[视觉节点源码](https://github.com/czself/ros/blob/main/scripts/yolo_inspector.py) · [任务与取图联调](https://github.com/czself/ros/blob/main/scripts/route_executor.py) · [高清 OCR 接入记录](https://github.com/czself/ros/blob/main/docs/agent_context/tasks/task008/ocr_hd_20260928.md)

### 建图、定位与导航联调

- **定位链路**：配置 GMapping 建图与 AMCL 定位，核对地图、里程计、激光输入和 TF 坐标关系。
- **规划与执行**：对接 Navfn 全局规划和自定义 `ForwardPathFollower`，联调局部代价地图、车体 footprint、速度限制、末端位置与航向对齐。
- **避障与任务**：接入 LaserScan / PointCloud2 障碍信息，用 `move_base` Action 串联多目标点、返回起点、超时处理和进度检查。
- **验证与复盘**：记录路径、位姿、速度命令、任务日志与识别结果，分析到点偏差、定位误差、停滞和任务失败原因。

[导航配置](https://github.com/czself/ros/tree/main/navigation) · [局部路径跟随器](https://github.com/czself/ros/tree/main/ros_packages/forward_path_follower) · [完整任务统计](https://github.com/czself/ros/blob/main/docs/agent_context/tasks/task009/docs20_20260929/REPORT.md)

## 04 / 具体问题，具体定位

**[云台控制与调试记录](https://github.com/czself/gimbal)** · STM32F407 / BMI088 / GM6020 / VOFA+

- **电机反馈与命令映射**：沿 CAN 报文 ID、物理电机 ID、反馈数组和输出索引逐层追踪，定位通信正常但电机不动作的问题。
- **姿态与控制器状态**：记录陀螺仪零偏、Yaw 漂移、积分累积和稳态误差之间的关联。
- **可观测性**：结合总线错误计数、收发计数和 VOFA+ 遥测，保留“现象 → 原因 → 修复”的调试过程。

[查看调试日志 ↗](https://github.com/czself/gimbal/blob/main/DEBUG_LOG.md)

## 05 / 更多实践

| 项目 | 技术延伸 |
| :--- | :--- |
| **[STM32 寄存器 / HAL 双轨教程](https://github.com/czself/stm_regis_hal)** | 外设、通信与 FreeRTOS，源码配套中文讲解。 |
| **[ROS 智慧社区机器人](https://github.com/czself/ros)** | Gazebo 仿真中的建图、导航、十点巡检与视觉识别。 |
| **[YZ Control 战队官网](https://github.com/czself/robot_web_team)** | Next.js / React / TypeScript，战队展示与队员门户。 |
| **[TinyVim 终端 IDE](https://github.com/czself/TinyVim-IDE)** | Rust 开发工具，集成编译运行、文件浏览与 AI 编辑预览。 |

---

[主项目 RM2026](https://github.com/totrytakeoff/RM2026/tree/basic_framework) · [云台调试记录](https://github.com/czself/gimbal/blob/main/DEBUG_LOG.md) · [全部仓库](https://github.com/czself?tab=repositories)
