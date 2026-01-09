#!/bin/bash
# 创建 GitHub 仓库并推送代码

REPO_NAME="clothesforme"
USERNAME="DDDDDGCSM"
DESCRIPTION="Middle East Clothes Exchange Platform"

echo "🚀 开始部署 ClothesForME 到 GitHub..."
echo ""

# 检查是否已设置 GitHub token
if [ -z "$GITHUB_TOKEN" ]; then
    echo "⚠️  未检测到 GITHUB_TOKEN 环境变量"
    echo "请先设置 GitHub token:"
    echo "  export GITHUB_TOKEN=your_token_here"
    echo ""
    echo "或者手动创建仓库："
    echo "1. 访问 https://github.com/new"
    echo "2. 仓库名称: $REPO_NAME"
    echo "3. 描述: $DESCRIPTION"
    echo "4. 设置为 Public 或 Private"
    echo "5. 不要初始化 README"
    echo ""
    echo "然后运行："
    echo "  git remote add origin https://github.com/$USERNAME/$REPO_NAME.git"
    echo "  git branch -M main"
    echo "  git push -u origin main"
    exit 1
fi

echo "📦 创建 GitHub 仓库..."
curl -X POST \
  -H "Authorization: token $GITHUB_TOKEN" \
  -H "Accept: application/vnd.github.v3+json" \
  https://api.github.com/user/repos \
  -d "{\"name\":\"$REPO_NAME\",\"description\":\"$DESCRIPTION\",\"private\":false}" \
  > /dev/null 2>&1

if [ $? -eq 0 ]; then
    echo "✅ GitHub 仓库创建成功"
else
    echo "⚠️  仓库可能已存在，继续推送..."
fi

echo ""
echo "🔗 添加远程仓库..."
git remote remove origin 2>/dev/null
git remote add origin https://github.com/$USERNAME/$REPO_NAME.git

echo "📤 推送代码到 GitHub..."
git branch -M main
git push -u origin main

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ 部署成功！"
    echo "🌐 仓库地址: https://github.com/$USERNAME/$REPO_NAME"
    echo ""
    echo "📝 下一步："
    echo "1. 访问 https://vercel.com/new"
    echo "2. 导入仓库: $USERNAME/$REPO_NAME"
    echo "3. 点击 Deploy"
else
    echo "❌ 推送失败，请检查网络连接和权限"
fi

