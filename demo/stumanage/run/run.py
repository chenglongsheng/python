from CRUD import CRUD


def run():
    while True:
        print("=" * 40)
        print("学生信息管理-函数版")
        print("1、增加insert-个人信息")
        print("2、删除delete-个人信息")
        print("3、修改update-个人信息")
        print("4、查询select-个人信息")
        print("5、显示所有学生信息")
        print("6、退出系统")
        print("=" * 40 + '\n')
        order = int(input("请输入您要操作的功能序号："))
        if order == 1:
            CRUD.insert()
        elif order == 2:
            CRUD.delete()
        elif order == 3:
            CRUD.update()
        elif order == 4:
            CRUD.select()
        elif order == 5:
            CRUD.select_all()
        elif order == 6:
            break
