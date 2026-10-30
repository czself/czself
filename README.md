<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/header-dark.svg" />
  <img src="./assets/header.svg" width="100%" alt="czself — Embedded systems, robotics and developer tools" />
</picture>

以嵌入式与机器人为主线，记录从底层外设、系统集成到开发工具的实践。

**嵌入式** · STM32 / HAL / FreeRTOS　 **机器人** · ROS / Gazebo　 **工具开发** · Rust / Python

## 精选项目

| 项目 | 做什么 | 主要技术 |
| :--- | :--- | :--- |
| **[STM32 全栈修炼手册](https://github.com/czself/stm_regis_hal)** | 寄存器与 HAL 双轨对照，覆盖外设、通信与 FreeRTOS；代码配套中文讲解。 | `C` `STM32` `PlatformIO` |
| **[智慧社区机器人](https://github.com/czself/ros)** | 在 Gazebo 仿真中串联建图、导航、十点巡检与视觉识别，保留任务日志和验证记录。 | `Python` `ROS Noetic` `Gazebo` |
| **[TinyVim](https://github.com/czself/TinyVim-IDE)** | 面向 C/C++ 与 Python 的轻量终端 IDE，集成编译运行、文件浏览与 AI 编辑预览。 | `Rust` `TUI` `CLI` |
| **[YZ Control 战队官网](https://github.com/czself/robot_web_team)** | 战队展示与队员门户，包含招新、资料管理及角色权限。 | `TypeScript` `Next.js` `React` |

## 技术与实践

- **从底层理解系统**：用寄存器与 HAL 对照梳理外设行为，再推进到任务调度与多模块协作。
- **让系统跑起来**：把导航、感知和任务执行连接起来，记录仿真条件、结果与尚待解决的问题。
- **让项目易于继续**：把源码、使用说明、测试入口和验证记录一起整理到仓库。

更多实践：**[F22 飞控教学与比赛工程](https://github.com/czself/fly)** — 教学资料与比赛开发分开维护，比赛工程仍在开发，实机飞行验证尚未完成。

---

[浏览全部仓库 →](https://github.com/czself?tab=repositories)
