from __future__ import print_function
from sql_data_access import SqlDataAccess
import requests

sql_dal = SqlDataAccess()
print(requests.post('http://track-delay.appspot.com/merge', data=sql_dal.get_all_rows_json()))