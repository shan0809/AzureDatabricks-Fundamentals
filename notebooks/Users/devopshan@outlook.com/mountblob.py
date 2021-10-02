# Databricks notebook source
containername = "azuredbcontainer"
storagename = "azuredbob1289"
mountpoint = "/mnt/custommount"
sas = "=="
try:
  
  dbutils.fs.mount( source = "wasbs://" + containername + "@" + storagename + ".blob.core.windows.net",
                mount_point = mountpoint,
                 extra_configs = {"fs.azure.account.key." + storagename + '.blob.core.windows.net': sas}
  )
except Exception as e:
  print("already mounted, please unmount using dbutils.fs.unmount")

# COMMAND ----------

display(dbutils.fs.mounts())

# COMMAND ----------

"hello"

# COMMAND ----------

SmallDatasetTravel.csv

# COMMAND ----------

# MAGIC %fs  ls dbfs:/cluster-logs/0925-100442-stand344/

# COMMAND ----------

# MAGIC %fs ls dbfs:/cluster-logs/0925-100442-stand344/driver/

# COMMAND ----------

# MAGIC %fs ls dbfs:/cluster-logs/0925-100442-stand344/init_scripts/0925-100442-stand344_10_139_64_4/

# COMMAND ----------

# MAGIC %fs head dbfs:/cluster-logs/0925-100442-stand344/init_scripts/0925-100442-stand344_10_139_64_4/20210929_191156_00_spark-monitoring.sh.stderr.log

# COMMAND ----------



# COMMAND ----------

"hello world"

# COMMAND ----------

