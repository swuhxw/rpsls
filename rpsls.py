#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ�������
���ڣ�2020��4��10��
"""
import random

def name_to_number(name):#����Ϸ�����Ӧ����ͬ������
	if name=='ʯͷ':
	  return 0
	elif name=='ʷ����':
	     return 1
	elif name=='��':
	     return 2
	elif name=='����':
	     return 3
	elif name=='����':
	     return 4
	else:
		print("Error: No Correct Name")
def number_to_name(number):#������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
	if number in range(0,5):
		if number==0:
		   return "ʯͷ"
		elif number==1:
		   return "ʷ����"
		elif number==2:
		   return "��"
		elif number==3:
		   return "����"
		elif number==4:
		   return "����"
	else:
	       print("Error: No Correct Name")
def rpsls(player_choice):#�û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��
	print("����ѡ��Ϊ��",player_choice)
	player_number=name_to_number(player_choice)
	comp_number=random.randrange(0,5)
	comp_choice=number_to_name(comp_number)
	print("�������ѡ��Ϊ��",comp_choice)
	if player_number-comp_number in range(-4,-2) or range(1,3):
	   print("��Ӯ��")
	elif player_number-comp_number in range(-2,0) or range(3,5):
	     print("����Ӯ��")
	elif player_number-comp_number == 0:
	     print("ƽ��")
	else:
	     print("����")

print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()
rpsls(choice_name)







