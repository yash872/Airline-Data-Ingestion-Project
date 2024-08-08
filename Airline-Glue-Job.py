import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
import re

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Script generated for node airport-dim
airportdim_node1723095212438 = glueContext.create_dynamic_frame.from_catalog(database="airline-db", table_name="dev_airlines_airports_dim", redshift_tmp_dir="s3://temp-yb/airport-dim/", transformation_ctx="airportdim_node1723095212438")

# Script generated for node daily-flights-data
dailyflightsdata_node1723094880792 = glueContext.create_dynamic_frame.from_catalog(database="airline-db", table_name="daily_flights_data", transformation_ctx="dailyflightsdata_node1723094880792")

# Script generated for node Filter (depdelay >= 60)
Filterdepdelay60_node1723094924236 = Filter.apply(frame=dailyflightsdata_node1723094880792, f=lambda row: (row["depdelay"] >= 60), transformation_ctx="Filterdepdelay60_node1723094924236")

# Script generated for node departure Join
Filterdepdelay60_node1723094924236DF = Filterdepdelay60_node1723094924236.toDF()
airportdim_node1723095212438DF = airportdim_node1723095212438.toDF()
departureJoin_node1723095400148 = DynamicFrame.fromDF(Filterdepdelay60_node1723094924236DF.join(airportdim_node1723095212438DF, (Filterdepdelay60_node1723094924236DF['originairportid'] == airportdim_node1723095212438DF['airport_id']), "left"), glueContext, "departureJoin_node1723095400148")

# Script generated for node modify dep columns
modifydepcolumns_node1723095483475 = ApplyMapping.apply(frame=departureJoin_node1723095400148, mappings=[("depdelay", "long", "dep_delay", "bigint"), ("arrdelay", "long", "arr_delay", "bigint"), ("destairportid", "long", "destairportid", "long"), ("carrier", "string", "carrier", "string"), ("city", "string", "dep_city", "string"), ("name", "string", "dep_airport", "string"), ("state", "string", "dep_state", "string")], transformation_ctx="modifydepcolumns_node1723095483475")

# Script generated for node arrival Join
modifydepcolumns_node1723095483475DF = modifydepcolumns_node1723095483475.toDF()
airportdim_node1723095212438DF = airportdim_node1723095212438.toDF()
arrivalJoin_node1723095770004 = DynamicFrame.fromDF(modifydepcolumns_node1723095483475DF.join(airportdim_node1723095212438DF, (modifydepcolumns_node1723095483475DF['destairportid'] == airportdim_node1723095212438DF['airport_id']), "left"), glueContext, "arrivalJoin_node1723095770004")

# Script generated for node modify arr columns
modifyarrcolumns_node1723095844934 = ApplyMapping.apply(frame=arrivalJoin_node1723095770004, mappings=[("dep_delay", "bigint", "dep_delay", "long"), ("arr_delay", "bigint", "arr_delay", "long"), ("destairportid", "long", "destairportid", "long"), ("carrier", "string", "carrier", "string"), ("dep_city", "string", "dep_city", "string"), ("dep_airport", "string", "dep_airport", "string"), ("dep_state", "string", "dep_state", "string"), ("airport_id", "long", "airport_id", "long"), ("city", "string", "arr_city", "string"), ("name", "string", "arr_airport", "string"), ("state", "string", "arr_state", "string")], transformation_ctx="modifyarrcolumns_node1723095844934")

# Script generated for node Redshift Target Table
RedshiftTargetTable_node1723096041201 = glueContext.write_dynamic_frame.from_catalog(frame=modifyarrcolumns_node1723095844934, database="airline-db", table_name="dev_airlines_daily_flights_fact", redshift_tmp_dir="s3://temp-yb/flight-facts/",additional_options={"aws_iam_role": "arn:aws:iam::010526265053:role/service-role/AmazonRedshift-CommandsAccessRole-20240806T210859"}, transformation_ctx="RedshiftTargetTable_node1723096041201")

job.commit()