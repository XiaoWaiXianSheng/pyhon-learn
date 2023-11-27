import json
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, ToolboxOpts
from pyecharts.options import LegendOpts, VisualMapOpts,LabelOpts

f_us = open("D:/dev/美国.txt", "r", encoding="UTF-8")
us_data = f_us.read()

f_jp = open("D:/dev/日本.txt", "r", encoding="UTF-8")
jp_data = f_jp.read()

f_in = open("D:/dev/印度.txt", "r", encoding="UTF-8")
in_data = f_in.read()

'''删除不合规的数据'''
us_data = us_data.replace("jsonp_1629344292311_69436(", "")
jp_data = jp_data.replace("jsonp_1629350871167_29498(", "")
in_data = in_data.replace("jsonp_1629350745930_63180(", "")

us_data = us_data[:-2]
jp_data = jp_data[:-2]
in_data = in_data[:-2]

#print(us_data)

'''json转python字典'''
us_dict = json.loads(us_data)
jp_dict = json.loads(jp_data)
in_dict = json.loads(in_data)
# print(type(us_dict))
# print(us_dict)

'''获取trend key'''
us_trend_data = us_dict["data"][0]["trend"]
jp_trend_data = jp_dict["data"][0]["trend"]
in_trend_data = in_dict["data"][0]["trend"]
# print(type(trend_data))
# print(trend_data)


'''获取日期数据，用于x轴，取2020年（下标到314结束）'''
us_x_data = us_trend_data["updateDate"][:314]
jp_x_data = jp_trend_data["updateDate"][:314]
in_x_data = in_trend_data["updateDate"][:314]
# print(us_x_data)

'''获取确诊数据，用于y轴，取2020年（下标到314结束）'''
us_y_data = us_trend_data["list"][0]["data"][:314]
jp_y_data = jp_trend_data["list"][0]["data"][:314]
in_y_data = in_trend_data["list"][0]["data"][:314]
# print(us_y_data)

'''生成折线图'''
line = Line()

line.add_xaxis(us_x_data)
line.add_yaxis("美国确诊人数", us_y_data, label_opts=LabelOpts(is_show=False))
line.add_yaxis("日本确诊人数", jp_y_data, label_opts=LabelOpts(is_show=False))
line.add_yaxis("印度确诊人数", in_y_data, label_opts=LabelOpts(is_show=False))

line.set_global_opts(
    title_opts=TitleOpts(title="确诊人数", pos_left="center", pos_bottom="1%"),
    legend_opts=LegendOpts(is_show=True, ),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True, max_=20000000)

)

line.render(path="人数.html")

f_us.close()
f_jp.close()
f_in.close()