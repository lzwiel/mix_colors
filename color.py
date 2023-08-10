# 输入两种颜色
color1 = input("请输入第一种颜色：")
color2 = input("请输入第二种颜色：")

# 定义颜色混合规则
def mix_colors(color1, color2):
    if color1 == "红色" and color2 == "蓝色" or color1 == "蓝色" and color2 == "红色":
        return "紫色"
    elif color1 == "红色" and color2 == "黄色" or color1 == "黄色" and color2 == "红色":
        return "橙色"
    elif color1 == "蓝色" and color2 == "黄色" or color1 == "黄色" and color2 == "蓝色":
        return "绿色"
    else:
        return "无法混合"

# 调用颜色混合函数并打印结果
result_color = mix_colors(color1, color2)
print("混合后得到的颜色为：", result_color)
