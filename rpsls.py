#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：胡新婉
日期：2020年4月10日
"""
import random

def name_to_number(name):#将游戏对象对应到不同的整数
	if name=='石头':
	  return 0
	elif name=='史波克':
	     return 1
	elif name=='布':
	     return 2
	elif name=='蜥蜴':
	     return 3
	elif name=='剪刀':
	     return 4
	else:
		print("Error: No Correct Name")
def number_to_name(number):#将整数 (0, 1, 2, 3, or 4)对应到游戏的不同对象
	if number in range(0,5):
		if number==0:
		   return "石头"
		elif number==1:
		   return "史波克"
		elif number==2:
		   return "布"
		elif number==3:
		   return "蜥蜴"
		elif number==4:
		   return "剪刀"
	else:
	       print("Error: No Correct Name")
def rpsls(player_choice):#用户玩家任意给出一个选择，根据RPSLS游戏规则，在屏幕上输出对应的结果
	print("您的选择为：",player_choice)
	player_number=name_to_number(player_choice)
	comp_number=random.randrange(0,5)
	comp_choice=number_to_name(comp_number)
	print("计算机的选择为：",comp_choice)
	if player_number-comp_number in range(-4,-2) or range(1,3):
	   print("您赢了")
	elif player_number-comp_number in range(-2,0) or range(3,5):
	     print("机器赢了")
	elif player_number-comp_number == 0:
	     print("平局")
	else:
	     print("错误")

print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
choice_name=input()
rpsls(choice_name)







