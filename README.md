<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/header-dark.svg" />
  <img src="./assets/header.svg" width="100%" alt="czself — RoboMaster robot control and algorithms" />
</picture>

完成 **RM2026 步兵机器人整车电控**，目前负责 **步兵改哨兵算法开发**。<br>
关注机器人控制、视觉联调、建图定位与导航集成。

<a href="https://github.com/totrytakeoff/RM2026/tree/basic_framework">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="./assets/highlights-dark.svg" />
    <img src="./assets/highlights.svg" width="100%" alt="RoboMaster 1v1 步兵对抗赛全国二等奖；RM2026 步兵整车电控实现：底盘、云台、发射与遥控通信。" />
  </picture>
</a>

**[主项目](#主项目)　·　[机器人技术栈](#机器人技术栈)　·　[联调与验证](#联调与验证)　·　[更多项目](#更多项目)**

## 主项目

### [RM2026 · 步兵整车电控 ↗](https://github.com/totrytakeoff/RM2026/tree/basic_framework)

**YZ Control / STM32F407** — 在战队协作项目中完成步兵整车电控实现与联调，贯通遥控输入、机构控制、传感反馈和电机执行。

| 模块 | 实现与源码 |
| :--- | :--- |
| **底盘** | 运动学、坐标变换、云台跟随、小陀螺与轮速分配 · [源码](https://github.com/totrytakeoff/RM2026/tree/refactor/infantry-freertos/applications/infantry/chassis) |
| **云台** | Yaw / Pitch、IMU 反馈、角度 / 速度切换、软硬限位 · [源码](https://github.com/totrytakeoff/RM2026/tree/refactor/infantry-freertos/applications/infantry/gimbal) |
| **发射** | 摩擦轮与拨弹协同、单发 / 连发、扳机边沿与状态管理 · [源码](https://github.com/totrytakeoff/RM2026/tree/refactor/infantry-freertos/applications/infantry/shoot) |
| **通信** | 遥控状态归一化、模式映射、CAN / UART 与掉线处理 · [源码](https://github.com/totrytakeoff/RM2026/tree/refactor/infantry-freertos/applications/infantry/command) |

[赛季控制基线](https://github.com/totrytakeoff/RM2026/tree/basic_framework) · [当前框架分支](https://github.com/totrytakeoff/RM2026/tree/refactor/infantry-freertos) · [整车应用源码](https://github.com/totrytakeoff/RM2026/tree/refactor/infantry-freertos/applications/infantry)

<details>
<summary><b>展开控制链路与 FreeRTOS 设计</b> · 任务分工 / 状态所有权 / 工程验证</summary>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/control-loop-dark.svg" />
  <img src="./assets/control-loop.svg" width="100%" alt="步兵控制链路：遥控输入到机器人行为，再到 PID 与 CAN 电机执行；编码器和 IMU 反馈进入闭环。" />
</picture>

当前框架分支进一步梳理整车控制的任务边界与数据所有权：

- **任务职责**：姿态解算、整车控制、电机执行和健康监测分工；控制任务发布完整命令，电机任务独占 PID 状态与 CAN 输出。
- **状态一致性**：姿态快照与电机命令邮箱处理跨任务共享状态，命令租约限制过期输出。
- **故障处理**：输入有效性、设备在线状态、任务健康和独立看门狗共同参与输出管理。
- **验证入口**：主机逻辑测试覆盖输入适配、运动学、云台限位、扳机状态及 PID reset，配套板级回归和链接审计。

[控制所有权设计](https://github.com/totrytakeoff/RM2026/blob/refactor/infantry-freertos/docs/migration/control_ownership_milestone.md) · [任务实现](https://github.com/totrytakeoff/RM2026/blob/refactor/infantry-freertos/firmware/infantry_f407/freertos/infantry_tasks.c) · [主机测试](https://github.com/totrytakeoff/RM2026/tree/refactor/infantry-freertos/tests/host)

这里展示的是后续框架重构分支；该分支的实板回归状态以仓库验收记录为准。

</details>

## 机器人技术栈

项目实践覆盖 **下位机电控 → ROS 系统集成 → 感知与导航**。

<table width="100%">
  <tr>
    <td width="50%" valign="top">
      <h3>电控与运动控制</h3>
      <p><code>C / C++</code> <code>STM32</code> <code>FreeRTOS</code></p>
      <p>F407 / F103、HAL、CAN / UART、SPI / I²C；外设驱动、中断、DMA 与任务组织。</p>
      <p>PID、底盘运动学、Yaw / Pitch、编码器与 BMI088 / IMU；姿态解算、闭环调参、限位和模式切换。</p>
    </td>
    <td width="50%" valign="top">
      <h3>ROS 与视觉感知</h3>
      <p><code>ROS Noetic</code> <code>Python</code> <code>OpenCV</code></p>
      <p>rospy、TF、Topic、Actionlib、cv_bridge；节点接口、坐标变换与源帧时间戳关联。</p>
      <p>Ultralytics YOLO、RGB-D、PaddleOCR；推理接入、目标检测、ROI 裁剪、深度定位与识别可视化。</p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3>建图、定位与导航</h3>
      <p><code>GMapping</code> <code>AMCL</code> <code>move_base</code></p>
      <p>二维 SLAM、map_server、LaserScan 与里程计；地图管理、初始位姿和定位参数联调。</p>
      <p>Navfn、costmap_2d、ForwardPathFollower；全局规划、局部路径跟随、footprint 检查、激光 / 深度避障与多点任务。</p>
    </td>
    <td width="50%" valign="top">
      <h3>仿真、调试与工程工具</h3>
      <p><code>Gazebo</code> <code>RViz</code> <code>rosbag</code></p>
      <p>Gazebo Classic 传感器接入、地图与路径可视化；VOFA+ 遥测、GDB / OpenOCD 烧录与故障定位。</p>
      <p>Linux、Git、CMake、PlatformIO、Docker；构建环境、运行数据记录与复盘。</p>
    </td>
  </tr>
</table>

## 联调与验证

**视觉配合运动，导航串联任务，调试追到具体信号与状态。**<br>
视觉与导航实践来自 [ROS / Gazebo 智慧社区巡检](https://github.com/czself/ros)，电控调试记录来自 [云台项目](https://github.com/czself/gimbal)。

<details>
<summary><b>视觉与运动配合</b> · 图像接入 / 深度与 TF / 识别到行为</summary>

- **相机 → ROS → 推理**：通过 <code>cv_bridge</code> 对接图像与 OpenCV / YOLO，检查源帧、时间戳、类别、置信度和输出频率。
- **检测 → 空间位置**：结合 <code>CameraInfo</code>、深度图和同源帧 TF，把观测关联到机器人 / 地图坐标，处理深度缺失、重复观测与结果过期。
- **识别 → 任务行为**：交通灯检测接入通行条件，人物检测接入位置关联与统计；车牌使用 ROI 裁剪、PaddleOCR 和多帧结果核对。
- **到点 → 稳定取图**：联调位置、航向、拍照时机和画面范围，保留原图、标注图、识别结果及源帧信息。

[视觉节点源码](https://github.com/czself/ros/blob/main/scripts/yolo_inspector.py) · [任务与取图联调](https://github.com/czself/ros/blob/main/scripts/route_executor.py) · [高清 OCR 接入记录](https://github.com/czself/ros/blob/main/docs/agent_context/tasks/task008/ocr_hd_20260928.md)

</details>

<details>
<summary><b>建图、定位与导航联调</b> · 规划执行 / 障碍接入 / 多点任务</summary>

- **定位链路**：配置 GMapping 与 AMCL，核对地图、里程计、激光输入和 map / odom / base 坐标链。
- **规划执行**：对接 Navfn 与自定义 <code>ForwardPathFollower</code>，联调代价地图、footprint、速度限制和末端位置 / 航向对齐。
- **避障任务**：接入 LaserScan / PointCloud2 障碍信息，以 <code>move_base</code> Action 串联目标点、返回起点、超时处理与进度检查。
- **验证复盘**：记录路径、位姿、速度命令、任务日志和识别结果，分析到点偏差、定位误差、停滞及任务失败原因。

[导航配置](https://github.com/czself/ros/tree/main/navigation) · [局部路径跟随器](https://github.com/czself/ros/tree/main/ros_packages/forward_path_follower) · [完整任务统计](https://github.com/czself/ros/blob/main/docs/agent_context/tasks/task009/docs20_20260929/REPORT.md)

</details>

<details>
<summary><b>云台电控调试</b> · CAN / 姿态反馈 / PID / VOFA+</summary>

**STM32F407 / BMI088 / GM6020**

- **命令与反馈映射**：沿 CAN 报文 ID、物理电机 ID、反馈数组与输出索引逐层追踪，定位通信正常但电机不动作的问题。
- **姿态与控制状态**：记录陀螺仪零偏、Yaw 漂移、积分累积和稳态误差之间的关联。
- **可观测性**：结合总线错误计数、收发计数和 VOFA+ 遥测，保留“现象 → 原因 → 修复”的调试过程。

[查看调试日志](https://github.com/czself/gimbal/blob/main/DEBUG_LOG.md)

</details>

## 更多项目

| 项目 | 方向 |
| :--- | :--- |
| [**STM32 双轨教程**](https://github.com/czself/stm_regis_hal) | 寄存器 / HAL、外设通信与 FreeRTOS，配套中文讲解 |
| [**ROS 智慧社区机器人**](https://github.com/czself/ros) | Gazebo 建图、导航、十点巡检与视觉识别 |
| [**YZ Control 战队官网**](https://github.com/czself/robot_web_team) | Next.js / React / TypeScript，战队展示与队员门户 |
| [**TinyVim 终端 IDE**](https://github.com/czself/TinyVim-IDE) | Rust，编译运行、文件浏览与 AI 编辑预览 |

[浏览全部仓库 ↗](https://github.com/czself?tab=repositories)
