import pandas as pd
from tabulate import tabulate


# Dirty Data 
# : 수집된 원천 데이터는 불완전하거나 부정확한 경우가 많음


# Dirty Data 종류
# 1) 결측치
# 2) 오류 데이터
# 3) 사용불가 데이터
# 4) 이상치 

'''
(1) 데이터 정렬하기 : sort_values()

========================================
df.sort_values("기준 컬럼", ascending  = )
========================================

* ascending 이 true면 오르차순 false면 내림차순 


'''

df = pd.read_csv('data_analysis/20251117/data/seoul_park04.csv')
df 

print(tabulate(df.sort_values("총입장객수"), headers='keys', tablefmt='fancy_outline'))
print(tabulate(df.sort_values("총입장객수", ascending= False), headers='keys', tablefmt='fancy_outline'))

'''
(2) 인덱스 재지정하기 : reset_index()

========================================
df.reset_index(drop= )
========================================

* drop이 True면 기존 인덱스 컬럼 삭제

'''
print(df.reset_index()) # index 재정렬 
print(df.reset_index(drop=True)) # index 열 제거 


df_reset_index = df.sort_values("총입장객수").reset_index(drop=True)
df_reset_index.reset_index()





'''
(3) 데이터 정렬하기 : reset_index()

========================================
df.reset_index(drop= )
========================================

* drop이 True면 기존 인덱스 컬럼 삭제

'''

# ! 데이터 정제는 원본에 반영 X -> 변수를 통해 직접 덮어쓰기 


'''
(3) 데이터 정렬하기 : reset_index()

========================================
df.reset_index(drop= )
========================================

* drop이 True면 기존 인덱스 컬럼 삭제

'''