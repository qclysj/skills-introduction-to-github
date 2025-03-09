import prettytable as pt
def show_ticket(row_num):
    tb=pt.PrettyTable()#创建表
    tb.field_names=['行号','座位1','座位2','座位3','座位4']
    for i in range(1,row_num+1):
        lst=[f'第{i}行','有票','有票','有票','有票']
        tb.add_row(lst)
    print(tb)

def order_ticket(row_num,row,column):
    tb=pt.PrettyTable()
    tb.field_names=['行号','座位1','座位2','座位3','座位4']
    for i in range(1, row_num + 1):
        if int(row)==i:
            lst=[f'第{i}行','有票','有票','有票','有票']
            lst[int(column)]='已售'
            tb.add_row(lst)
        else:
            lst=[f'第{i}行','有票','有票','有票','有票']
            tb.add_row(lst)
    print(tb)

if __name__ == '__main__':
    row_num=6
    show_ticket(row_num)
    choose_num=input('请输入选择的的座位：如4，3表示第四排第三列：')
    row,column=choose_num.split(',')
    order_ticket(row_num,row,column)