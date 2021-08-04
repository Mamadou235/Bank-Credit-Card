import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'Total_Revolving_Bal':1, 'Avg_Open_To_Buy':2, 'Total_Amt_Chng_Q4_Q1':3, 'Total_Trans_Amt':4, 'Total_Trans_Ct':5, 'Total_Ct_Chng_Q4_Q1':6, 'Avg_Utilization_Ratio':7})

print(r.json())
