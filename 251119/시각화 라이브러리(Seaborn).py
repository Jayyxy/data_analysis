# ===============================================================
# 시각화 라이브러리. Seaborn
# ===============================================================
# 


# 설치 : pip install seaborn
# 불러오기 : import seaborn as sns

# matpolotlib과 같이 사용 

import matplotlib.pyplot as plt
import seaborn as sns

# 폰트 사용 (사전에 폰트 설치, 순서 유의 )
plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False


# 예시데이터 
year = [2018, 2019, 2020, 2021, 2022, 2023]
python = [5.8, 8.17, 9.31, 11.87, 15.63, 14.51]
C = [13.59, 14.08, 16.72, 14.32, 12.71, 14.73]
java = [15.78, 15.04, 16.73, 11.23, 10.82, 13.23]
JS = [3.49, 2.51, 2.38, 2.44, 2.12, 2.1]


'''
(1) seaborn을 이용한 차트 생성
'''
# 라인차트
sns.lineplot(x=year, y=python)

# 범례 표시
# 별도로 legend()를 호출하지 않고 label 매개변수로 범례추가
sns.lineplot(x=year, y=python, label="Python")
sns.lineplot(x=year, y=java, label="Java")

plt.show() 

# 테마 사용하기 
sns.set_style