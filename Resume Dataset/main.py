import PyPDF2

# 打开PDF文件
with open('inputs/archive/data/data/ACCOUNTANT/10554236.pdf', 'rb') as f:
    # 创建一个PDF解析器对象
    pdf_reader = PyPDF2.PdfReader(f)

    # 遍历PDF中的所有页面
    for page in range(len(pdf_reader.pages)):
        # 获取当前页面对象
        pdf_page = pdf_reader.pages[page]

        # 从页面对象中提取文本
        text = pdf_page.extract_text()

        # 打印文本
        print(text)
