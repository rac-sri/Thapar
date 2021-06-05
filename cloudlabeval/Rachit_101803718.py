
# Problem: Design an algorithm that takes minimum time for finding all common words/strings from two files. It should read input from input1.txt and input2.txt files. Input can be text files of any length. You are not allowed to use inbuilt functions for the same.

# Download input files from the given links:

# https://drive.google.com/file/d/1M04fIFn_kj4SwRy1NrYOs0_ijYu019AW/view?usp=sharing

# https://drive.google.com/file/d/1nyAqf-bpkGZv76C1__dDajzJR7j796Tu/view?usp=sharing




import sys
from operator import add
from pyspark.sql import SparkSession
import re

spark = SparkSession.builder.appName("Searching Occurences").getOrCreate()

l = spark.read.text("input1.txt").rdd.map(lambda r: r[0])
ll = l.map(lambda r: re.sub("[^a-zA-Z0-9 ]", "", r))

l1 = spark.read.text("input2.txt").rdd.map(lambda r: r[0])
ll1 = l1.map(lambda r: re.sub("[^a-zA-Z0-9 ]", "", r))

w = ll.flatMap(lambda x: x.split(' ')).map(lambda x: x.lower())
w_c = w.filter(lambda x: x!='').distinct()

w1 = ll1.flatMap(lambda x: x.split(' ')).map(lambda x: x.lower())
w_c1 = w1.filter(lambda x: x!='').distinct()

res = w_c.intersection(w_c1)

print(res.collect())
