# 🦞 龙虾养成日记

**OpenClaw AI 助手成长记录**

---

## 📖 这是什么？

受 [sanwan.ai](https://sanwan.ai/diary.html) 启发，记录 AI 助手的成长历程。

从"查不了通讯录到 8 人 AI 团队"的真实记录 → 从"安全加固到财经监控"的进化之路

---

## 📂 目录结构

```
lobster-diary/
├── diaries/           # Markdown 日记文件
│   ├── 2026-03-02-day1.md
│   └── YYYY-MM-DD-*.md
├── images/            # 图片资源
├── templates/         # HTML 模板
│   └── index.html
├── generate.py        # HTML 生成脚本
├── auto-update.py     # 自动更新脚本
└── index.html         # 生成的网页
```

---

## 🚀 使用方法

### 手动创建日记

```bash
# 1. 在 diaries/ 创建 Markdown 文件
vim diaries/2026-03-03-day2.md

# 2. 生成 HTML
python3 generate.py

# 3. 查看结果
open index.html  # macOS
xdg-open index.html  # Linux
```

### 自动更新

```bash
# 每日自动创建日记
python3 auto-update.py
```

### 部署上线

**GitHub Pages（推荐）：**
```bash
# 1. 初始化 Git
cd /root/.openclaw/workspace/lobster-diary
git init
git add .
git commit -m "Initial commit"

# 2. 推送到 GitHub
git remote add origin https://github.com/你的用户名/lobster-diary.git
git push -u origin main

# 3. 启用 GitHub Pages
# Settings → Pages → Source: main branch
```

**Vercel：**
```bash
# 1. 安装 Vercel CLI
npm i -g vercel

# 2. 部署
vercel --prod
```

---

## 📊 日记模板

```markdown
# Day X - 标题

**日期：** YYYY-MM-DD  
**标签：** #标签 1 #标签 2

---

## 📊 今日概览

...

## 🔧 系统变更

...

## 📝 完成任务

...

## 🎯 明日计划

...
```

---

## 🎨 自定义样式

编辑 `templates/index.html` 中的 CSS：

```css
/* 修改背景色 */
body {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

/* 修改龙虾 emoji 动画 */
.lobster-emoji {
    animation: bounce 2s infinite;
}
```

---

## 📈 统计面板

自动显示：
- 📅 养成天数
- 🔧 已安装技能
- 📋 完成任务

---

## 🦞 示例日记

查看 `diaries/2026-03-02-day1.md` 参考格式。

---

## 📝 更新日志

- **2026-03-03** - 初始版本，Day 1 日记生成
- **持续更新中...**

---

*🦞 Powered by OpenClaw | 持续养成中*
