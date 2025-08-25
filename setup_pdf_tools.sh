#!/bin/bash

echo "🔧 安装PDF生成工具..."

# 检测操作系统
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    echo "检测到Linux系统"
    # Ubuntu/Debian
    if command -v apt-get &> /dev/null; then
        sudo apt-get update
        sudo apt-get install -y wkhtmltopdf
    # CentOS/RHEL
    elif command -v yum &> /dev/null; then
        sudo yum install -y wkhtmltopdf
    fi
elif [[ "$OSTYPE" == "darwin"* ]]; then
    echo "检测到macOS系统"
    if command -v brew &> /dev/null; then
        brew install wkhtmltopdf
    else
        echo "请先安装Homebrew: https://brew.sh/"
        exit 1
    fi
else
    echo "⚠️  请手动安装wkhtmltopdf"
    echo "下载地址: https://wkhtmltopdf.org/downloads.html"
fi

# 安装Python依赖
echo "📦 安装Python依赖..."
pip install markdown pdfkit

echo "✅ 安装完成！"
echo "现在可以运行: python generate_pdf.py"
