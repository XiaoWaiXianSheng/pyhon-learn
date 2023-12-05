from pyspark import SparkConf, SparkContext
import os

os.environ['PYSPARK_PYTHON'] = "D:/dev/python3.11.6/python.exe"  # 配置环境变量

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")

sc = SparkContext(conf=conf)

'''准备一个RDD'''
rdd = sc.parallelize([1, 2, 3, 4, 5])

'''通过map方法将全部数据乘以10'''


def func(data):
    return data * 10


rdd2 = rdd.map(func)
rdd3 = rdd.map(lambda x: x * 10)
rdd4 = rdd.map(lambda x: x * 10).map(lambda x: x +5)
# (T) -> U 函数要能接受一个参数，返回一个值
# (T) -> T 传入的参数类型需与返回值类型相同

print(rdd2.collect())
print(rdd3.collect())
print(rdd4.collect())
