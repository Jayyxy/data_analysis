import pandas as pd 

# 결측치
# : 데이터에 값이 없는 것/누락된 것. 데이터 분석시 처리해야 할 대상 


# 결측치 종류
# 1) N/A
# 2) Null
# 3) NaN

# 결측치 처리 전략 
# 1) 제거하기
# 2) 대체하기

'''
(1) 결측치 탐색하기 : isna()


'''
df = pd.read_csv('data_analysis/20251117/data/seoul_park.csv')
df 

df.isna()

df.isna().sum()


'''
(2)-1 결측치 처리 전략 : 채우기 


'''

print(df.isna().sum()) # 데이터프레임의 모든 컬럼에 대해 결측값의 개수를 반환 
df['청소년'] = df['청소년'].fillna(int(df['청소년'].mean()))


'''
(2)-2 결측치 처리 전략 : 삭제하기 dropna()

- 결측치가 포함된 행을 삭제 

==============================================
df.dropna(subset=["컬럼 이름"], ignore_index= )


- 
==============================================


==============================================
df.dropna(how= )

- how = "any" : 하나라도 있으면 삭제 
- how = "all" : 모든값이 결측이면 삭제 

==============================================


==============================================
df.dropna(thresh= )

- 남아 있어야 하는 비결측치 개수 
- how 매개변수와 달리 개수로 디테일하게 제거 
- 
==============================================

* how와 thresh는 같이 사용 불가

'''


print(df.shape)

df.dropna(subset=['청소년'], ignore_index= True, inplace=True) # 행을 삭제 

print(df.isna().sum())
print(df.shape) # 행을 확인 : 5개의 행 삭제됨 

'''
(3) 데이터 병합하기 

- 데이터 셋은 여러 개로 분산되어 있는 경우가 종종 있음 

ex) 2016년 1월 매출, 2016년 2월 매출 / 고객 데이터 , 구매 데이터


'''


'''
(3)-1 concat()
 : 여러 데이터셋끼리 이어붙여서 하나로 병합

==============================================
pd.concat([데이터프레임(리스트)], axis= , join= , ignore_index=)
==============================================

* axis = 
- 어느 방향으로 합칠것인지 정하는 기준 (0 : 세로방향 , 1 : 가로방향)

* join = 
- 합칠 때의 기준 설정 (inner : 공통된 컬림 끼리만(나머지는 무시), outer : 모든 컬럼을 고려해서)

* ignore_index = 
- 합치고 나서 인덱스를 유지할지, 새로 부여할지 결정 
- True : 새로운 인덱스 부여, False : 원본 데이터프레임의 인덱스를 유지 (Default)

'''


# ==============================================
# Example. 데이터 병합하기 
# ==============================================

# Q1.
df1 = pd.read_csv('data_analysis/20251117/data/seoul_park04.csv')
df2 = pd.read_csv('data_analysis/20251117/data/seoul_park_april.csv')

# 데이터 확인이 우선 
print(df1.head())
print(df2.head())


# df1와 df2를 세로로 결합하며, 겹치는 컬럼끼리 합칠거고, 합친 후 인덱스 초기화 
df_union = pd.concat([df1,df2], axis=0 ,join='inner' , ignore_index= True)

df_union

# 결합 후 데이터 확인  
print(df_union.head())
print(df_union.shape)
print(df_union.columns)

'''
(3)-2 merge()
 : 특정 컬럼을 기준으로 합치기 

- concat과 달리 가로로 병합만 가능 

==============================================
pd.merge(df1, df2, on= , how=) 
==============================================

* df1, df2 : 리스트 형태가 아닌 두개의 프레임으로만 설정 

* on = 
: 기준이 되는 컬럼 이름 ( 병합 기준 컬럼 )

* how = 
: 각 행을 합칠 때의 방식 ( 4가지 )
( inner : 교집합 , outer : 합집합, left : df1에 있는 모든 데이터를 기준 , right : df2에 있는 모든 데이터를 기준 )



'''

df_mm = pd.read_csv('data_analysis/20251117/data/misemunji.csv')

print(df1.head())
print(df_mm.head())

# how = 'left'를 이용하여 입장객 데이터를 중심으로 분석하기 위해 (부가적으로 미세먼지 데이터를 가져옴)
#  - df_mm 에는 폐쇄된 기간의 미세먼지 정보도 존재 (해당 기간은 의미 X )
#  - Inner를 쓰는 경우 미세먼지가 측정되지 않는 날, 미세먼지 정보가 없는 입장객만 있는 날의 데이터는 사라짐 (미세먼지는 부가적인 정보)
#  - 데이터 결합은 분석 목적에 따라 달라짐 , 변수의 중요도에 따라 
merged_df = pd.merge(df1,df_mm, on='날짜', how= 'left')



