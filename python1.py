from pyspark.sql import SparkSession

# Initialize Spark Session
spark = SparkSession.builder.appName("StudentMarksJoin").getOrCreate()
sc = spark.sparkContext

# 1. Load the files as RDDs
# student.txt -> student_id, name, city
student_rdd = sc.textFile("student.txt").map(lambda line: line.split(",")) \
                .map(lambda x: (x[0], (x[1], x[2])))

# marks.txt -> student_id, marks
marks_rdd = sc.textFile("marks.txt").map(lambda line: line.split(",")) \
              .map(lambda x: (x[0], int(x[1])))

# 2. Task 1: Perform inner join on student_id [cite: 5]
joined_rdd = student_rdd.join(marks_rdd)

# 3. Task 2: Filter students with marks > 70 [cite: 6]
# Structure after join: (student_id, ((name, city), marks))
filtered_rdd = joined_rdd.filter(lambda x: x[1][1] > 70)

# 4. Task 3: Sort by marks descending [cite: 7]
sorted_rdd = filtered_rdd.sortBy(lambda x: x[1][1], ascending=False)

# 5. Task 4: Save result [cite: 8]
sorted_rdd.saveAsTextFile("student_results_output")

# Print for verification
for record in sorted_rdd.collect():
    print(record)

spark.stop()

