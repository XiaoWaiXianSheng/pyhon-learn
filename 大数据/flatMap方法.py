from pyspark import SparkConf, SparkContext
import os

os.environ['PYSPARK_PYTHON'] = "D:/dev/python3.11.6/python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")

sc = SparkContext(conf=conf)
'''对rdd执行map操作，然后进行解除嵌套操作'''

rdd = sc.parallelize(["itheima itcast 666", "itheima itheima itcast", "python itheima"])

rdd2 = rdd.map(lambda x: x.split(" "))
rdd3 = rdd.flatMap(lambda x: x.split(" "))

print(rdd2.collect())
print(rdd3.collect())