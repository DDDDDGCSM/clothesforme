#!/usr/bin/env python3
"""
BookForME 一键自动化部署脚本
参考 smartval-simple 的部署方式
"""
import subprocess
import os
import sys
from datetime import datetime

# 项目配置
DIR = "/Users/a58/cursor/归档/OK 调研/bookforME"
USER = "DDDDDGCSM"
REPO = "bookforME"
GITHUB_URL = f"https://github.com/{USER}/{REPO}.git"

# GitHub Token（从环境变量或参数获取）
GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN') or (
    sys.argv[1] if len(sys.argv) > 1 and sys.argv[1].startswith('ghp_') else None
)

def git(args):
    """执行 Git 命令"""
    r = subprocess.run(['/usr/bin/git'] + args, cwd=DIR, capture_output=True, text=True, check=False)
    return r.stdout.strip(), r.stderr.strip(), r.returncode

def print_header():
    """打印标题"""
    print("╔═══════════════════════════════════════════════════════════════╗")
    print("║         🚀 BookForME 一键自动化部署 🚀                       ║")
    print("╚═══════════════════════════════════════════════════════════════╝")
    print()

def check_environment():
    """检查环境"""
    print("📋 步骤 1/5: 检查环境...")
    print("=" * 60)
    
    if not os.path.exists(f"{DIR}/app.py"):
        print(f"❌ 错误：找不到 app.py，请确认目录正确")
        print(f"   当前目录: {DIR}")
        sys.exit(1)
    
    if not os.path.exists(f"{DIR}/vercel.json"):
        print(f"❌ 错误：找不到 vercel.json")
        sys.exit(1)
    
    print("✅ 环境检查通过")
    print()

def setup_git():
    """配置 Git"""
    print("📋 步骤 2/5: 配置 Git...")
    print("=" * 60)
    
    # 检查是否已初始化
    if not os.path.exists(f"{DIR}/.git"):
        git(['init'])
        print("✅ Git 已初始化")
    
    git(['branch', '-M', 'main'])
    print("✅ Git 分支已设置为 main")
    print()

def push_to_github():
    """推送到 GitHub"""
    print("📋 步骤 3/5: 推送到 GitHub...")
    print("=" * 60)
    
    # 添加文件
    git(['add', '.'])
    stdout, _, _ = git(['status', '--short'])
    count = len([l for l in stdout.split('\n') if l.strip()])
    print(f"✅ 已添加 {count} 个文件")
    
    # 提交
    msg = f"Deploy: BookForME - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    _, stderr, code = git(['commit', '-m', msg])
    if code == 0:
        stdout, _, _ = git(['log', '-1', '--pretty=format:%h'])
        print(f"✅ 已提交 (ID: {stdout})")
    elif 'nothing to commit' not in stderr.lower():
        print(f"⚠️  提交失败: {stderr[:100]}")
    
    # 配置远程仓库
    stdout, _, code = git(['remote', 'get-url', 'origin'])
    if code != 0 or not stdout:
        if GITHUB_TOKEN:
            url = f"https://{GITHUB_TOKEN}@github.com/{USER}/{REPO}.git"
        else:
            url = GITHUB_URL
        git(['remote', 'add', 'origin', url])
        print(f"✅ 远程仓库已配置: {GITHUB_URL}")
    else:
        if GITHUB_TOKEN and GITHUB_TOKEN not in stdout:
            url = f"https://{GITHUB_TOKEN}@github.com/{USER}/{REPO}.git"
            git(['remote', 'set-url', 'origin', url])
            print(f"✅ 远程仓库已更新（带认证）")
        else:
            print(f"✅ 远程仓库: {stdout}")
    
    # 推送
    print("\n🚀 正在推送到 GitHub...")
    stdout, stderr, code = git(['push', '-u', 'origin', 'main'])
    
    if code == 0:
        print("✅ 推送成功！")
        print(f"   GitHub: {GITHUB_URL}")
    else:
        err = stderr[:300] if stderr else stdout[:300]
        print(f"⚠️  推送失败")
        if "repository not found" in err.lower():
            print("💡 GitHub 仓库可能还未创建")
            print("   请访问: https://github.com/new")
            print(f"   创建仓库: {REPO}")
            return False
        elif "authentication" in err.lower() or "permission" in err.lower():
            print("💡 需要 GitHub 认证")
            if not GITHUB_TOKEN:
                print("   使用方法:")
                print("   export GITHUB_TOKEN=your_token")
                print("   python3 一键部署.py")
                print("   或: python3 一键部署.py your_token")
            return False
        else:
            print(f"   错误: {err}")
            return False
    
    print()
    return True

def deploy_to_vercel():
    """部署到 Vercel（提供指引）"""
    print("📋 步骤 4/5: 部署到 Vercel...")
    print("=" * 60)
    print()
    print("🌐 请在浏览器中完成 Vercel 部署：")
    print()
    print("   1. 访问: https://vercel.com/new")
    print("   2. 使用 GitHub 登录（如果还没登录）")
    print("   3. 点击 'Import Git Repository'")
    print(f"   4. 搜索或选择: {REPO} 或 {USER}/{REPO}")
    print("   5. 点击 'Import'")
    print("   6. 保持所有默认设置（Vercel 会自动检测 Flask）")
    print("   7. 点击 'Deploy'")
    print("   8. 等待 1-2 分钟")
    print("   9. 看到 '🎉 Congratulations!' 表示成功")
    print()
    
    # 尝试自动打开浏览器
    try:
        import webbrowser
        response = input("是否自动打开 Vercel 部署页面？(y/n): ").strip().lower()
        if response == 'y' or response == 'yes':
            webbrowser.open("https://vercel.com/new")
            print("✅ 已打开浏览器")
    except:
        pass
    
    print()

def show_summary():
    """显示总结"""
    print("📋 步骤 5/5: 部署总结")
    print("=" * 60)
    print()
    print("╔═══════════════════════════════════════════════════════════════╗")
    print("║              ✅ 部署准备完成！                                 ║")
    print("╚═══════════════════════════════════════════════════════════════╝")
    print()
    print(f"📦 GitHub 仓库: {GITHUB_URL}")
    print("✅ 代码已推送")
    print("🚀 等待 Vercel 部署...")
    print()
    print("💡 提示：")
    print("  - Vercel 部署通常需要 1-2 分钟")
    print("  - 部署完成后会自动生成访问链接")
    print("  - 每次推送代码都会自动重新部署")
    print("  - 部署链接格式: https://bookforme.vercel.app")
    print()
    print("📚 相关文档：")
    print("  - 快速部署指南.md")
    print("  - VERCEL_DEPLOY_GUIDE.md")
    print()

def main():
    """主函数"""
    print_header()
    
    try:
        check_environment()
        setup_git()
        
        if push_to_github():
            deploy_to_vercel()
            show_summary()
        else:
            print("\n⚠️  GitHub 推送失败，请解决后重新运行")
            print("   或手动访问 Vercel 进行部署")
    
    except KeyboardInterrupt:
        print("\n\n⚠️  部署已取消")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ 发生错误: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()

