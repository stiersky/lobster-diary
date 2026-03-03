#!/usr/bin/env python3
"""
龙虾养成日记生成器
将 Markdown 日记转换为漂亮的 HTML 页面
"""

import os
import re
from datetime import datetime
from pathlib import Path

BASE_DIR = Path("/root/.openclaw/workspace/lobster-diary")
DIARIES_DIR = BASE_DIR / "diaries"
TEMPLATES_DIR = BASE_DIR / "templates"
OUTPUT_FILE = BASE_DIR / "index.html"

def read_template():
    """读取 HTML 模板"""
    with open(TEMPLATES_DIR / "index.html", "r", encoding="utf-8") as f:
        return f.read()

def parse_diary(filepath):
    """解析 Markdown 日记文件"""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # 提取标题
    title_match = re.search(r'^# (.+)$', content, re.MULTILINE)
    title = title_match.group(1) if title_match else "无标题"
    
    # 提取日期
    date_match = re.search(r'\*\*日期：\*\* (.+)$', content, re.MULTILINE)
    date = date_match.group(1) if date_match else filepath.stem
    
    # 提取标签
    tags_match = re.search(r'\*\*标签：\*\* (.+)$', content, re.MULTILINE)
    tags = tags_match.group(1) if tags_match else ""
    
    # 提取正文（第一个 ## 之后）
    body_match = re.search(r'## (.+)$', content, re.MULTILINE | re.DOTALL)
    body = body_match.group(0) if body_match else content
    
    # Markdown 转 HTML（简单转换）
    body_html = markdown_to_html(body)
    
    # 标签 HTML
    tags_html = ""
    if tags:
        for tag in tags.split():
            tag_name = tag.strip('#')
            tag_class = tag_name.lower()
            tags_html += f'<span class="tag {tag_class}">{tag}</span> '
    
    return {
        'title': title,
        'date': date,
        'tags': tags_html,
        'body': body_html,
        'filename': filepath.name
    }

def markdown_to_html(md):
    """简单的 Markdown 转 HTML"""
    html = md
    
    # 标题
    html = re.sub(r'^### (.+)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
    html = re.sub(r'^## (.+)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
    
    # 粗体
    html = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html)
    
    # 列表
    html = re.sub(r'^- (.+)$', r'<li>\1</li>', html, flags=re.MULTILINE)
    html = re.sub(r'(\n<li>.+?</li>\n)+', r'<ul>\1</ul>', html)
    
    # 表格
    html = re.sub(r'^\| (.+?) \|$', r'<tr><td>\1</td></tr>', html, flags=re.MULTILINE)
    html = re.sub(r'(\n<tr>.+?</tr>\n)+', r'<table>\1</table>', html)
    
    # 代码块
    html = re.sub(r'```(.+?)```', r'<pre><code>\1</code></pre>', html, flags=re.DOTALL)
    
    # 换行
    html = html.replace('\n\n', '</p><p>')
    
    return f'<p>{html}</p>'

def generate_html():
    """生成 HTML 页面"""
    template = read_template()
    
    # 读取所有日记
    diaries = []
    if DIARIES_DIR.exists():
        for file in sorted(DIARIES_DIR.glob("*.md"), reverse=True):
            diaries.append(parse_diary(file))
    
    # 生成日记 HTML
    entries_html = ""
    for diary in diaries:
        entries_html += f"""
        <div class="diary-entry">
            <div class="diary-date">{diary['date']}</div>
            <div class="diary-title">{diary['title']}</div>
            <div class="tags">{diary['tags']}</div>
            <div class="diary-content">{diary['body']}</div>
        </div>
        """
    
    # 统计
    skill_count = len(os.listdir("/root/.openclaw/workspace/skills/")) if os.path.exists("/root/.openclaw/workspace/skills/") else 0
    task_count = 15  # 可以根据实际任务数调整
    
    # 替换模板变量
    html = template.replace('{{DIARY_ENTRIES}}', entries_html)
    html = html.replace('{{LAST_UPDATE}}', datetime.now().strftime('%Y-%m-%d %H:%M:%S SGT'))
    html = html.replace('{{SKILL_COUNT}}', str(skill_count))
    html = html.replace('{{TASK_COUNT}}', str(task_count))
    
    # 保存
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(html)
    
    print(f"✅ 生成完成：{OUTPUT_FILE}")
    print(f"📊 日记数量：{len(diaries)}")
    print(f"🔧 技能数量：{skill_count}")
    print(f"📋 任务数量：{task_count}")

if __name__ == "__main__":
    generate_html()
