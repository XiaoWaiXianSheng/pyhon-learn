from pyspark import SparkConf, SparkContext
import os

os.environ['PYSPARK_PYTHON'] = "D:/dev/python3.11.6/python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")

sc = SparkContext(conf=conf)

'''针对KV型RDD，自动按照key分组，然后根据你提供的聚合逻辑，完成组内数据（value）的聚合操作'''

'''func: (V, V) -> V
    接受两个传入参数（类型要一致），返回一个返回值，类型要与传入要求一致'''

rdd = sc.parallelize([('男', 99), ('男', 88), ('女', 33), ('女', 66)])

rdd2 = rdd.reduceByKey(lambda a, b: a + b)

print(rdd2.collect())