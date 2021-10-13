# -*- coding: utf-8 -*-
import time

stu_info_list = []
stu_info = {}


def insert():
    stu_name = input("请输入个人姓名：")
    stu_info['name'] = stu_name

    stu_age = int(input("请输入个人年龄（18-25）："))
    while stu_age not in range(18, 26):
        stu_age = int(input("请输入个人年龄（18-25）："))
    stu_info['age'] = stu_age

    stu_mobile = input("请输入个人电话号码：")
    while stu_mobile.__len__() != 11:
        stu_mobile = input("输入的电话号码位数不是11位！，请重新输入：")
    stu_info['mobile'] = stu_mobile

    stu_info['register_time'] = time.strftime("%Y:%m:%d %H:%M:%S", time.localtime())

    stu_info['update_time'] = time.strftime("%Y:%m:%d %H:%M:%S", time.localtime())

    stu_info_list.append(stu_info)
    print(stu_info_list)

    return stu_info_list


def delete():
    delete_name = input("请输入您要删除个人的姓名：")
    for item in stu_info_list:
        for value in item.values():
            if delete_name == value:
                stu_info_list.remove(item)
                print("个人信息删除成功")
    print(stu_info_list)
    return stu_info_list


def update():
    update_name = input("请输入您要修改个人的姓名：")
    for item in stu_info_list:
        for value in item.values():
            if update_name == value:
                item['name'] = input("请输入更新后的姓名：")

                update_age = int(input('请输入更新后的年龄（18-25）：'))
                while update_age not in range(18, 26):
                    update_age = int(input("请输入更新后的年龄（18-25）："))
                item['age'] = update_age

                update_mobile = input("请输入更新后的手机号码：")
                while update_mobile.__len__() != 11:
                    update_mobile = input("输入更新后的电话号码位数不是11位！，请重新输入：")
                item['mobile'] = update_mobile

                item['update_time'] = time.strftime("%Y:%m:%d %H:%M:%S", time.localtime())

    print(stu_info_list)
    return stu_info_list


def select():
    select_name = input("请输入您要查找个人信息的姓名：")
    for item in stu_info_list:
        for value in item.values():
            if select_name == value:
                print("学生姓名：{0}，学生年龄：{1}，学生电话：{2}".format(item.get('name'), item.get('age'), item.get('mobile')))
    return stu_info_list


def select_all():
    for item in stu_info_list:
        print("学生姓名：{0}，学生年龄：{1}，学生电话：{2}".format(item.get('name'), item.get('age'), item.get('mobile')))
    return stu_info_list
