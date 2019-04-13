import pandas as pd
import xlrd
import numpy as np
ctx = "../data/"
filename=ctx +"CCTV_in_Seoul.csv"
df_cctv = pd.read_csv(filename,encoding='utf-8')#dataframe tpye==df라고 개명

print(df_cctv.head())

"""
  2013년도 이전  2014년  2015년  2016년
0  강남구  3238       1292    430    584    932
1  강동구  1010        379     99    155    377
2  강북구   831        369    120    138    204
3  강서구   911        388    258    184     81
4  관악구  2109        846    260    390    613
"""
df_cctv_idx = seoul_cctv.columns
print(df_cctv_idx)
''' Index(['기관명', '소계', '2013년도 이전', '2014년', '2015년', '2016년'], 
            dtype='object')
'''
df_cctv.rename(columns={df_cctv.columns[0] : '구별'}, inplace=True)
# inplace=True 는 실제 변수의 내용
print(df_cctv.head())
'''    구별    소계  2013년도 이전  2014년  2015년  2016년
0  강남구  3238       1292    430    584    932
1  강동구  1010        379     99    155    377
2  강북구   831        369    120    138    204
3  강서구   911        388    258    184     81
4  관악구  2109        846    260 
'''
df_pop = pd.read_excel(ctx + "population_in_Seoul.xls",
                            encoding='UTF-8',
                            header = 2,
                            usecols='B,D,G,J,N' )
'''
FutureWarning: the 'parse_cols' keyword is deprecated, use 'usecols' instead
'''
print(df_pop.head())

'''
   자치구           계        계.1       계.2   65세이상고령자
0   합계  10197604.0  9926968.0  270636.0  1321458.0
1  종로구    162820.0   153589.0    9231.0    25425.0
2   중구    133240.0   124312.0    8928.0    20764.0
3  용산구    244203.0   229456.0   14747.0    36231.0
4  성동구    311244.0   303380.0    7864.0    39997.0
'''
seoul_pop.rename(columns={df_pop.columns[0]: '구별',
                          df_pop.columns[1]: '인구수',
                          df_pop.columns[2]: '한국인',
                          df_pop.columns[3]: '외국인',
                          df_pop.columns[4]: '고령자'}, inplace=True)

print(df_pop.head())
'''
    구별         인구수        한국인       외국인        고령자
0   합계  10197604.0  9926968.0  270636.0  1321458.0
1  종로구    162820.0   153589.0    9231.0    25425.0
2   중구    133240.0   124312.0    8928.0    20764.0
3  용산구    244203.0   229456.0   14747.0    36231.0
4  성동구    311244.0   303380.0    7864.0    39997.0
'''


df_cctv.sort_values(by='소계', ascending=True).head(5)#sort_values 오른차 순
df_pop.drop([0],inplace=True)
df_pop['구별'].unique()
df_pop['구별'].isnull()
df_pop.drop([26],inplace=True)
print(df_pop)


df_pop['외국인비율'] = df_pop['외국인'] / df_pop['인구수'] * 100
df_pop['고령자비율'] = df_pop['고령자'] / df_pop['인구수'] * 100
df_cctv.drop(['2013년도 이전','2014년','2015년','2016년'],1,inplace=True)
#cctv와 인구를 합치다
df_cctv.pop=df.merge(df_cctv,df_pop,on='구별')
#상관관계
cor1=np.corrcoef(data_result['고령자비율'],data_result['소계'])
cor2=np.corrcoef(data_result['고령자비율'],data_result['소계'])
print(df_cctv_pop)

df_cctv_pop.to_csv()
