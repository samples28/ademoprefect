#!/usr/bin/env python3
"""
将Markdown模板转换为PDF的脚本
需要安装: pip install markdown pdfkit
注意: 还需要安装wkhtmltopdf系统工具
"""

import markdown
import pdfkit
import os
from datetime import datetime

def markdown_to_pdf(md_file, output_pdf):
    """将Markdown文件转换为PDF"""
    try:
        # 读取Markdown文件
        with open(md_file, 'r', encoding='utf-8') as f:
            md_content = f.read()
        
        # 转换为HTML
        html = markdown.markdown(md_content, extensions=['tables'])
        
        # 添加CSS样式
        html_with_style = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <style>
                body {{
                    font-family: "Microsoft YaHei", Arial, sans-serif;
                    line-height: 1.6;
                    margin: 40px;
                    color: #333;
                }}
                h1, h2, h3 {{
                    color: #2c3e50;
                    border-bottom: 2px solid #3498db;
                    padding-bottom: 10px;
                }}
                table {{
                    border-collapse: collapse;
                    width: 100%;
                    margin: 20px 0;
                }}
                th, td {{
                    border: 1px solid #ddd;
                    padding: 12px;
                    text-align: left;
                }}
                th {{
                    background-color: #f2f2f2;
                    font-weight: bold;
                }}
                .checkbox {{
                    margin: 5px 0;
                }}
            </style>
        </head>
        <body>
        {html}
        </body>
        </html>
        """
        
        # 配置PDF选项
        options = {
            'page-size': 'A4',
            'margin-top': '0.75in',
            'margin-right': '0.75in',
            'margin-bottom': '0.75in',
            'margin-left': '0.75in',
            'encoding': "UTF-8",
            'no-outline': None,
            'enable-local-file-access': None
        }
        
        # 转换为PDF
        pdfkit.from_string(html_with_style, output_pdf, options=options)
        print(f"✅ 成功生成PDF: {output_pdf}")
        
    except Exception as e:
        print(f"❌ 转换失败: {e}")
        print("请确保已安装所需依赖:")
        print("pip install markdown pdfkit")
        print("以及系统工具 wkhtmltopdf")

def main():
    """主函数"""
    # 创建输出目录
    output_dir = "compliance_documents"
    os.makedirs(output_dir, exist_ok=True)
    
    # 转换文件
    files_to_convert = [
        ("tech_update_plan_template.md", "技术更新计划模板.pdf"),
        ("physical_access_review_template.md", "物理访问权限审查模板.pdf")
    ]
    
    for md_file, pdf_name in files_to_convert:
        if os.path.exists(md_file):
            output_path = os.path.join(output_dir, pdf_name)
            markdown_to_pdf(md_file, output_path)
        else:
            print(f"⚠️  文件不存在: {md_file}")
    
    print(f"\n📁 所有PDF文件已保存到: {output_dir}/")

if __name__ == "__main__":
    main()
