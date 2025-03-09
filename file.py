def my_write():
    file=open('a.txt','w',encoding='utf-8')
    file.write('伟大的美国梦\n')
    file.close()

def my_write_list(file,lst):
    f=open(file,'a',encoding='utf-8')
    f.writelines(lst)
    f.close()

def my_read():
    file = open('a.txt', 'r', encoding='utf-8')
    s=file.read()
    print(s)
    file.close()

def copy(src,new_path):
    file1=open(src,'rb')
    file2=open(new_path,'wb')
    s=file1.read()
    file2.write(s)
    file2.close()
    file1.close()
if __name__ == '__main__':
    my_write()
    # my_read()
    lst=['姓名：\t','年龄：\t','成绩：\n','张三   \t','76  \t','98']
    my_write_list('a.txt',lst)
