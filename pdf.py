import pdfplumber
with pdfplumber.open('24_庞博_乐器在线教学网站系统项目管理报告.pdf') as pdf:
    for i in pdf.pages:
        print(i.extract_text())
        print(f'----------第{i.page_number}页结束')
