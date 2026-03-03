#!/usr/bin/env python3
"""
龙虾养成日记 - 自动更新脚本
每日自动生成日记条目
"""

import json
from datetime import datetime
from pathlib import Path

BASE_DIR = Path("/root/.openclaw/workspace/lobster-diary")
DIARIES_DIR = BASE_DIR / "diaries"
MEMORY_DIR = Path("/root/.openclaw/workspace/memory/daily")

def get_today_tasks():
    """从记忆文件获取今日任务"""
    today = datetime.now().strftime('%Y-%m-%d')
    memory_file = MEMORY_DIR / f"{today}.md"
    
    if memory_file.exists():
        with open(memory_file, 'r', encoding='utf-8') as f:
            return f.read()
    return ""

def create_daily_diary():
    """创建今日日记"""
    today = datetime.now().strftime('%Y-%m-%d')
    filename = f"{today}-diary.md"
    filepath = DIARIES_DIR / filename
    
    # 检查是否已存在
    if filepath.exists():
        print(f"⚠️ 今日日记已存在：{filename}")
        return
    
    # 获取记忆内容
    memory_content = get_today_tasks()
    
    # 生成日记模板
    diary = f"""# Day X - {today}

**日期：** {today}  
**标签：** #日常 #更新

---

## 📊 今日概览

*待补充...*

---

## 🔧 系统变更

*待补充...*

---

## 📝 完成任务

*待补充...*

---

## 🎯 明日计划

*待补充...*

---

*🦞 龙虾养成，持续更新中！*
"""
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(diary)
    
    print(f"✅ 创建今日日记：{filename}")

if __name__ == "__main__":
    create_daily_diary()
    # 重新生成 HTML
    import subprocess
    subprocess.run(['python3', str(BASE_DIR / 'generate.py')])
