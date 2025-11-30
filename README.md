# Alien Invasion 外星入侵游戏

## 项目简介
这是一个基于 Pygame 开发的经典射击游戏。玩家控制飞船左右移动，发射子弹击落外星舰队，随着关卡提升，游戏速度会不断加快。

**GitHub 仓库链接**：https://github.com/Hor1zen/homework2_alien

---

## 环境要求

- **Python 版本**：3.11.9
- **依赖包**：`pygame==2.6.1`

---

## 安装与运行指南

### 1. 克隆项目到本地
```bash
git clone https://github.com/Hor1zen/homework2_alien.git
cd homework2_alien
```

### 2. 安装依赖
确保已安装 Python 3.11.9，然后执行：
```bash
pip install -r requirements.txt
```

### 3. 启动游戏
在项目根目录下运行主程序：
```bash
python alien_invasion.py
```

---

## 项目结构说明

```
homework2_alien/
├── alien_invasion.py    # 主程序入口
├── settings.py          # 游戏配置类
├── ship.py              # 飞船类
├── bullet.py            # 子弹类
├── alien.py             # 外星人类
├── game_stats.py        # 游戏统计与最高分记录
├── scoreboard.py        # 得分板显示
├── button.py            # 开始按钮
├── requirements.txt     # 依赖包列表
├── images/              # 图像资源目录
│   ├── ship.bmp         # 飞船图片
│   └── alien.bmp        # 外星人图片
└── audio/               # 音效文件目录
    ├── bomb.mp3         # 爆炸音效
    ├── laser2.mp3       # 发射激光音效
    ├── magic5.mp3       # 飞船被击中音效
    ├── correct_answer3.mp3  # 清关音效
    └── blip04.mp3       # 激光不足音效
```

**注意**：游戏需要 `images/` 和 `audio/` 目录下的资源文件才能完整运行

---

## 游戏操作说明

| 按键 | 功能 |
|------|------|
| **← →** | 左右移动飞船 |
| **空格** | 发射子弹（最多3发） |
| **Q** | 退出游戏 |
| **鼠标点击** | 点击"Play"按钮开始游戏 |

- 击落所有外星人即可进入下一关，速度会更快
- 被外星人撞到或外星人触底会损失飞船
- 游戏结束后可点击"Play"重新开始，最高分会自动保存到 `high_score.json`

---

## 功能特性

✅ 完整的游戏循环与碰撞检测  
✅ 动态难度递增系统  
✅ 实时得分与最高分记录（本地持久化）  
✅ 得分动画效果（红色浮动显示）  
✅ 多音效反馈系统  
✅ 生命数量可视化显示

---

## 注意事项

1. **首次运行**：如需在 IDE 中运行，请将工作目录设置为项目根目录
2. **文件路径**：所有资源路径均为相对路径，请勿移动 `images/` 和 `audio/` 目录位置
3. **依赖冲突**：若安装失败，建议使用虚拟环境：
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

---

## 许可证
本项目仅供学习交流使用