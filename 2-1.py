print("758_lk")#这里的print自带换行符
temp = input("猜我想的是什么数字：")
#变量无需声明直接赋值,=代表赋值,==用于判断
#input、print、int等是python的内置函数，称为bif
#bif=built-in function
#input返回的变量是字符串，int->整数型
guess = int(temp)
if guess == 8:#这里是冒号![idle会因此自动缩进]
    print("你猜对了")
    print("猜对无奖")
else:#这里也是冒号!
    print("猜错了")
    #python中用缩进表示if或循环等范围
print("游戏结束，不玩啦")
