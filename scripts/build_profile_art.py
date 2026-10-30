"""Build original, self-contained light/dark artwork for the profile.

Visual references: antfu's compact navigation and DenverCoder1's project cards.
All artwork and copy here are original to this profile; no remote assets required.
"""
from html import escape
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "assets"
SANS = "'Noto Sans CJK SC', 'Microsoft YaHei', Arial, sans-serif"
MONO = "'SFMono-Regular', Consolas, 'Liberation Mono', monospace"


def text(x, y, value, size=20, fill="fg", weight=400, font=SANS, spacing=None):
    tracking = f' letter-spacing="{spacing}"' if spacing is not None else ""
    return (f'<text x="{x}" y="{y}" fill="{palette[fill]}" '
            f'font-family="{font}" font-size="{size}" font-weight="{weight}"'
            f'{tracking}>{escape(value)}</text>')


def line(x1, y1, x2, y2, width=1):
    return f'<path d="M{x1} {y1}H{x2}" stroke="{palette["line"]}" stroke-width="{width}"/>' if y1 == y2 else f'<path d="M{x1} {y1}L{x2} {y2}" stroke="{palette["line"]}" stroke-width="{width}"/>'


def rect(x, y, w, h, r=16, fill="panel"):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{palette[fill]}" stroke="{palette["line"]}"/>'


def save(name, width, height, title, description, elements):
    body = '\n'.join(elements)
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
           f'viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">\n'
           f'<title id="title">{escape(title)}</title>\n'
           f'<desc id="desc">{escape(description)}</desc>\n{body}\n</svg>\n')
    (OUT / f'{name}{suffix}.svg').write_text(svg, encoding='utf-8')


def icon(kind):
    paths = {
        'control': '<rect x="10" y="10" width="32" height="32" rx="7"/><path d="M18 2v8m16-8v8M18 42v8m16-8v8M2 18h8m-8 16h8M42 18h8m-8 16h8"/><path d="M19 27l5 5 10-12"/>',
        'vision': '<path d="M2 26s9-16 24-16 24 16 24 16-9 16-24 16S2 26 2 26z"/><circle cx="26" cy="26" r="8"/><path d="M2 11V2h9m30 0h9v9M2 41v9h9m30 0h9v-9"/>',
        'navigation': '<path d="M6 42L20 28l13 8 13-25"/><path d="M33 12l13-1 2 13"/><circle cx="6" cy="42" r="4"/><circle cx="20" cy="28" r="3"/><circle cx="33" cy="36" r="3"/>',
        'tools': '<rect x="2" y="6" width="48" height="36" rx="6"/><path d="M12 18l7 6-7 6m15 0h12M16 48h20m-10-6v6"/>',
    }
    return f'<g transform="translate(510 30)" fill="none" stroke="{palette["muted"]}" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">{paths[kind]}</g>'


for dark in (False, True):
    suffix = '-dark' if dark else ''
    palette = ({'bg': '#0d1117', 'panel': '#14191f', 'inset': '#10151b', 'fg': '#f1f3f5', 'muted': '#a0a9b4', 'line': '#323a43'}
               if dark else
               {'bg': '#ffffff', 'panel': '#f8f9fa', 'inset': '#ffffff', 'fg': '#171c22', 'muted': '#5c6773', 'line': '#d8dde3'})

    hero = [rect(1, 1, 1198, 418, 22),
            text(44, 43, 'CZSELF / ROBOTICS ENGINEERING', 14, 'muted', 500, MONO, 1.8),
            text(37, 193, 'czself', 148, 'fg', 800, 'Arial, Helvetica, sans-serif', -7),
            text(46, 240, '电控实现 · 视觉联调 · 建图导航', 25, 'muted'),
            line(738, 80, 738, 240),
            line(44, 282, 1156, 282)]
    for n, label, y in [('01', 'CONTROL', 114), ('02', 'PERCEPTION', 169), ('03', 'NAVIGATION', 224)]:
        hero.extend([text(788, y, n, 15, 'muted', 400, MONO), text(836, y, label, 25, 'fg', 500, MONO, 0.4)])
    for x, label, headline, subtitle in [
        (44, 'BUILT / RM2026', '步兵整车电控', '完整实现与整车联调'),
        (425, 'AWARD / ROBOMASTER', '全国二等奖', '1v1 步兵对抗赛'),
        (816, 'CURRENT FOCUS', '步兵 → 哨兵', '当前负责算法开发')]:
        hero.extend([text(x, 319, label, 13, 'muted', 500, MONO, 1),
                     text(x, 358, headline, 29, 'fg', 700),
                     text(x, 389, subtitle, 19, 'muted')])
    hero.extend([line(392, 312, 392, 390), line(782, 312, 782, 390)])
    save('profile-hero', 1200, 420, 'czself · RoboMaster robotics',
         '完整实现 RM2026 步兵整车电控；RoboMaster 1v1 步兵对抗赛全国二等奖；目前负责步兵改哨兵算法开发。', hero)

    project = [rect(1, 1, 1198, 234, 18),
               text(40, 40, 'SELECTED WORK / YZ CONTROL', 13, 'muted', 500, MONO, 1.4),
               text(36, 112, 'RM2026', 68, 'fg', 700, 'Arial, Helvetica, sans-serif', -2),
               text(40, 153, '步兵机器人 · 整车电控', 26, 'fg', 500),
               text(40, 199, 'STM32F407  /  C & C++  /  CAN', 15, 'muted', 400, MONO)]
    for x, y, label, title in [(650, 25, '01 / CHASSIS', '底盘运动控制'), (920, 25, '02 / GIMBAL', '云台姿态控制'),
                                (650, 127, '03 / SHOOTER', '发射机构协同'), (920, 127, '04 / INPUT', '遥控与通信')]:
        project.extend([rect(x, y, 248, 83, 10, 'inset'), text(x+20, y+27, label, 12, 'muted', 400, MONO, 1), text(x+20, y+61, title, 25, 'fg', 600)])
    save('project-rm2026', 1200, 236, 'RM2026 · 步兵整车电控',
         'YZ Control 战队项目。底盘运动控制、云台姿态控制、发射机构协同及遥控通信。', project)

    cards = [
        ('skill-control', 'control', '01 / CONTROL', '电控与实时系统',
         ['C/C++ · STM32 · FreeRTOS', 'PID · CAN/UART · IMU'],
         ['驱动接入、闭环控制与状态管理', '从外设调试到步兵整车联调']),
        ('skill-vision', 'vision', '02 / PERCEPTION', '视觉与 ROS 联调',
         ['Python · OpenCV · YOLO', 'ROS Noetic · RGB-D · PaddleOCR'],
         ['图像、深度与 TF 坐标对齐', '将识别结果接入机器人行为']),
        ('skill-navigation', 'navigation', '03 / NAVIGATION', '建图定位与导航',
         ['GMapping · AMCL · move_base', 'Navfn · costmap · 路径跟随'],
         ['从地图构建到多点任务执行', '联调规划、避障与末端对齐']),
        ('skill-tools', 'tools', '04 / ENGINEERING', '仿真与工程验证',
         ['Gazebo · RViz · rosbag', 'GDB · OpenOCD · VOFA+'],
         ['运行记录、故障定位与回归', 'Linux · Docker · CMake · PlatformIO'])]
    for name, kind, eyebrow, title, keywords, lines in cards:
        elements = [rect(9, 9, 582, 312, 18),
                    text(36, 49, eyebrow, 13, 'muted', 500, MONO, 1.2), icon(kind),
                    text(34, 115, title, 34, 'fg', 700),
                    text(36, 159, keywords[0], 21, 'fg', 400),
                    text(36, 192, keywords[1], 20, 'muted', 400),
                    line(36, 222, 564, 222),
                    text(36, 261, lines[0], 21, 'muted'),
                    text(36, 293, lines[1], 20, 'muted')]
        save(name, 600, 330, title, '；'.join(keywords+lines), elements)

print('Generated 12 original SVG assets (light/dark).')
