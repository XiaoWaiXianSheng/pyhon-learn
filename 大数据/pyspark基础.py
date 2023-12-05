from pyspark import SparkConf, SparkContext

'''创建SparkConf类对象'''
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")


'''基于SparkConf类对象创建SparkContext类对象'''
sc = SparkContext(conf=conf)

'''打开PySpark的运行版本'''
print(sc.version)

sc.stop()