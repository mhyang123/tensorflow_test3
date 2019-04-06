import pandas as pd
ctx = "../data/"
filename=ctx +"01. CCTV_in_Seoul.csv"
seoul_cctv = pd.read_csv(filename,encoding='utf-8')

print(seoul_cctv.head())

"""
  2013년도 이전  2014년  2015년  2016년
0  강남구  3238       1292    430    584    932
1  강동구  1010        379     99    155    377
2  강북구   831        369    120    138    204
3  강서구   911        388    258    184     81
4  관악구  2109        846    260    390    613
"""
seoul_cctv_idx = seoul_cctv.columns
print(seoul_cctv_idx)
''' Index(['기관명', '소계', '2013년도 이전', '2014년', '2015년', '2016년'], 
            dtype='object')
'''
seoul_cctv.rename(columns={seoul_cctv.columns[0] : '구별'}, inplace=True)
# inplace=True 는 실제 변수의 내용
# print(seoul_cctv.head())
'''    구별    소계  2013년도 이전  2014년  2015년  2016년
0  강남구  3238       1292    430    584    932
1  강동구  1010        379     99    155    377
2  강북구   831        369    120    138    204
3  강서구   911        388    258    184     81
4  관악구  2109        846    260 
'''