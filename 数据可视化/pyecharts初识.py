'''导入Line功能构建折线图对象'''
from pyecharts.charts import Line

from pyecharts.options import TitleOpts, ToolboxOpts
from pyecharts.options import LegendOpts, VisualMapOpts

line = Line()

line.add_xaxis(["中国", "英国", "美国"])

line.add_yaxis("GDP", [30, 20, 10])

'''设置全局配置项'''
line.set_global_opts(
    title_opts=TitleOpts(title="GDP展示", pos_left="center", pos_bottom="1%"),
    legend_opts=LegendOpts(is_show=True, ),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True, max_=40, min_=0)

)
line.render()
