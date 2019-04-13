import  pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager,rc
import seaborn as sns
from sklearn import preprocessing

ctx = '../data/'
filename ='crime_police.csv'

df_crime_police = pd.read_csv(ctx+filename,
                       sep=',',
                       encoding='utf-8')
print(df_crime_police.columns)
'''
Index(['Unnamed: 0', '관서명', '살인 발생', '살인 검거', '강도 발생', '강도 검거', '강간 발생',
       '강간 검거', '절도 발생', '절도 검거', '폭력 발생', '폭력 검거', '구별'],
      dtype='object')
'''
df_police= pd.pivot_table(df_crime_police,
                          index='구별',
                            aggfunc=np.sum)

print(df_crime_police.columns) #문서를 같은 것 합산 할수 있게 했음
'''
Index(['Unnamed: 0', '관서명', '살인 발생', '살인 검거', '강도 발생', '강도 검거', '강간 발생',
       '강간 검거', '절도 발생', '절도 검거', '폭력 발생', '폭력 검거', '구별'],
      dtype='object')
'''

#aggfunc는 평균값 리턴
df_police['강간검거율']=df_police['강간 검거']/ df_police['강간 발생']*100
df_police['강도검거율']=df_police['강도 검거']/ df_police['강도 발생']*100
df_police['살인검거율']=df_police['살인 검거']/ df_police['살인 발생']*100
df_police['절도검거율']=df_police['절도 검거']/ df_police['절도 발생']*100
df_police['폭력검거율']=df_police['폭력 검거']/ df_police['폭력 발생']*100

df_police.drop(['강간 검거','강도 검거','살인 검거','절도 검거','폭력 검거'],1)
#검거율이 100이 넘는 것이 있는데,기간상의 오류
ls_rate=['강간 검거','강도 검거','살인 검거','절도 검거','폭력 검거']
for i in ls_rate:
    df_police.loc[df_police[i]]>100,i]=100
df_police.rename(columns={'강간 발생':'강간',
                          '강도 발생': '강도',
                          '살인 발생': '살인',
                          '절도 발생': '절도',
                          '폭력 발생': '폭력'

                          },inplace=true)
ls_crime=['강간','강도','살인','절도','폭력']
x=df_police[ls_crime].values
min_max_scalar=preprocessing.MinMaxScaler()
'''
스케일링은 선형변환을 적요하여 전체 자료의 분포를 평균 0,분산1이 되도록 만드는 과정

'''
x_scaled=min_max_scalar.fit_transform(x.astype(float))
df_police_norm = pd.DataFrame(x,scaled,
                                columns=ls_crime,
                                index=df_police.index)
df_police norm[ls_rate] = df_police[ls_rate]
df_cctv_pop = pd.read_csv(ctx+filename,
encoding='UTF-8,'
sep=',',
index_col='구별')
df_police_norm[['인구수','cctv']]=df_cctv_pop



















