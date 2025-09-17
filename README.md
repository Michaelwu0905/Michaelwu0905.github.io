## 基于 Flask + SQLite 的极简博客

### 项目简介
一个基于 Flask 与 SQLite 的极简博客，支持文章的创建、查看、编辑与删除。前端使用 Bootstrap 5 与 Bootstrap Icons（CDN），模板已做轻量美化，逻辑简洁直观。

### 功能
- **列表页**：按创建时间倒序展示文章
- **详情页**：查看文章内容
- **新建文章**：表单提交创建
- **编辑文章**：表单提交更新
- **删除文章**：POST 提交并提示确认

### 技术栈
- **后端**：Flask (Python)
- **数据库**：SQLite（本地 `database.db`）
- **前端**：Bootstrap 5（CDN）、Bootstrap Icons（CDN）

### 目录结构
```text
app.py                # Flask 入口与路由
init_db.py            # 初始化数据库（建表并插入示例数据）
db.sql                # 数据库 schema
database.db           # 运行时生成的 SQLite 数据库文件
templates/            # Jinja2 模板（base/index/post/new/edit/about）
static/css, static/js # 前端静态文件
```

### 快速开始
- 环境要求：Python 3.8+

1) 创建并激活虚拟环境（推荐）
```powershell
python -m venv .venv
. .\.venv\Scripts\Activate.ps1
```

2) 安装依赖
```powershell
pip install flask
```

3) 初始化数据库（生成并填充 `database.db`）
```powershell
python init_db.py
```

4) 运行开发服务器
```powershell
$env:FLASK_APP="app.py"
$env:FLASK_DEBUG="1"
flask run
```

5) 访问
- 首页：`http://127.0.0.1:5000/`

### 常用路由
- 首页（列表）：`/`
- 关于页：`/about`
- 查看文章：`/posts/<post_id>`
- 新建文章：`/posts/new`（GET/POST）
- 编辑文章：`/post/<post_id>/edit`（GET/POST）
- 删除文章：`/post/<post_id>/delete`（POST）

### 开发与配置
- `SECRET_KEY` 位于 `app.py`，请在生产环境替换为安全随机值。
- 页面样式在 `templates/` 与 `static/`，可在 `static/css/style.css` 自定义主题配色。
- 模板使用 Jinja2，业务逻辑尽量放在视图函数中，模板负责展示。

### 部署建议
- 本项目为 Flask 服务端应用，可部署到支持 Python Web 的平台（如 Render、Railway、Fly.io、云服务器等）。
- 若使用 WSGI（如 gunicorn），启动命令可指向 `app:app`。
- SQLite 适合轻量使用；生产环境可切换为云数据库并调整连接方式。


