
# coding: utf-8

# # Custom Report Demo
# 
# This demo shows how to create and query a dataset. The dataset in this case is generated by running an RCSB PDB web service to create a custom report of PDB annotations.
# 
# [PDB custom report](http://www.rcsb.org/pdb/results/reportField.do)
# 
# ## Imports

# In[1]:


from pyspark import SparkConf, SparkContext, SQLContext
from mmtfPyspark.datasets import customReportService
import time


# ## Configure Spark

# In[2]:


conf = SparkConf().setMaster("local[*]")                       .setAppName("secondaryStructureSegmentDemo")
sc = SparkContext(conf = conf)
sqlContext = SQLContext(sc)


# ## Retrieve PDB annotation:
# Binding addinities (Ki, Kd), group name of the ligand (hetId), and the Enzyme Classification number (ecNo)

# In[3]:


ds = customReportService.get_dataset(["Ki","Kd","hetId","ecNo"])


# ## Show the schema of this dataset

# In[4]:


ds.printSchema()


# ## Filtering
# 
# ### Select structures that either have Ki or Kd values(s) and are protein-serine/threonine kinases (EC 2.7.1.*)
# 
# 
# #### A. By using dataset operations

# In[5]:


ds = ds.filter("(Ki IS NOT NULL OR Kd IS NOT NULL) AND ecNo LIKE '2.7.11.%'")

ds.show(10)


# #### B. By creating a temporary query and running SQL

# In[6]:


ds.createOrReplaceTempView("table")

ds = sqlContext.sql("SELECT * from table WHERE (Ki IS NOT NULL OR Kd IS NOT NULL) AND ecNo LIKE '2.7.11.%'")

ds.show(10)


# ## Terminate Spark

# In[7]:


sc.stop()

