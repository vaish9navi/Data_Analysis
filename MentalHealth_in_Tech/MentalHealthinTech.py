import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

dbfile = "C:/Users/priiv/OneDrive/Desktop/Data_Analysis/MentalHealth_in_Tech/mental_health.sqlite"
conn = sqlite3.connect(dbfile)

tables = pd.read_sql("SELECT * FROM sqlite_master \
WHERE TYPE = 'table'; ", con=conn)
# print(tables)

answer = pd.read_sql_query("SELECT * FROM Answer", con=conn)
# print(answer.head())
question = pd.read_sql_query("SELECT * FROM Question", con=conn)
# print(question.head())
survey = pd.read_sql_query("SELECT * FROM Survey", con=conn)
# print(survey.head())

# print(answer.info())
# print(question.info())
# print(survey.info())