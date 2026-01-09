# 👗 ClothesForME - 中东衣服交换平台

一个温暖的衣服交换社区，让每件衣服找到新的主人。

## ✨ 功能特性

- 👗 **精选衣服**：每件衣服都有独特的故事
- 💬 **故事分享**：了解每件衣服背后的情感
- 🤝 **交换申请**：简单的申请流程
- 📱 **移动端适配**：完美支持手机访问
- 💬 **WhatsApp 集成**：直接联系交换伙伴
- 🌐 **多语言界面**：支持阿拉伯语和英语

## 🚀 快速部署

### 方法一：自动化部署（推荐）

#### 一键部署（半自动）

```bash
python3 一键部署.py your_github_token
```

自动完成：
- ✅ 推送到 GitHub
- ✅ 提供 Vercel 部署指引

#### 完全自动部署

```bash
python3 完全自动部署.py github_token vercel_token
```

自动完成：
- ✅ 推送到 GitHub
- ✅ 创建 Vercel 项目
- ✅ 触发部署
- ✅ 完全无需手动操作

详细说明请查看：[自动化部署说明.md](自动化部署说明.md)

### 方法二：网页部署

1. 访问: https://vercel.com/new
2. 使用 GitHub 登录
3. 导入仓库: `your-username/clothesforme` 或 `your-username/bookforME`
4. 点击: "Deploy"

详细步骤请查看：[快速部署指南.md](快速部署指南.md)

### 方法三：使用 Vercel CLI

```bash
npm install -g vercel
vercel login
vercel
```

## 📁 项目结构

```
bookforME/
├── app.py                    # Flask 后端应用
├── requirements.txt          # Python 依赖
├── vercel.json              # Vercel 配置
├── 一键部署.py              # 半自动部署脚本
├── 完全自动部署.py          # 全自动部署脚本
├── templates/               # HTML 模板
│   └── index.html          # 主页面
└── static/                 # 静态资源
    ├── css/
    │   └── style.css       # 样式文件
    └── js/                 # JavaScript 文件
```

## 🛠️ 本地开发

### 安装依赖

```bash
pip install -r requirements.txt
```

### 运行应用

```bash
python3 app.py
```

访问: http://localhost:5000

## 📋 技术栈

- **后端**: Flask 3.0.0
- **前端**: HTML, CSS, JavaScript
- **部署**: Vercel
- **语言**: 英语（主要），支持阿拉伯语
- **内容**: 衣服交换（包括服装、睡衣、杂志等）

## 🌐 部署后访问

部署成功后，您将获得一个 Vercel 链接，例如：
```
https://clothesforme.vercel.app 或 https://bookforme.vercel.app
```

## 📝 更新部署

修改代码后，只需运行部署脚本：

```bash
# 使用一键部署
python3 一键部署.py your_token

# 或使用完全自动部署
python3 完全自动部署.py github_token vercel_token
```

Vercel 会自动检测并重新部署（约 1-2 分钟）

## 📚 相关文档

- [自动化部署说明.md](自动化部署说明.md) - 自动化部署详细说明
- [快速部署指南.md](快速部署指南.md) - 网页部署步骤
- [VERCEL_DEPLOY_GUIDE.md](VERCEL_DEPLOY_GUIDE.md) - Vercel 完整指南

## 🎯 下一步

1. 运行自动化部署脚本
2. 测试所有功能
3. 收集用户反馈
4. 持续优化体验

---

**祝您部署顺利！** 🚀
