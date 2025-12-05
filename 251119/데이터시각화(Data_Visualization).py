
# ================================================================
# 데이터 시각화란 ?
# ================================================================
# : 문자와 숫자로 표현된 데이터를 차트(chart)를 사용하여 표현하는 것

# ================================================================
# 데이터 시각화의 목적
# ================================================================
# 1) 여러 변수간의 차이를 한 눈에 비교 가능
# 2) 분석 결과를 명확히 설명 


'''
(1) matplotlib 데이터 시각화 사용법

패키지 설치 : pip install matplotlib 
라이브러리 불러오기 : import maplotlib.pyplot as plt 

'''

import matplotlib.pyplot as plt

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
(2) 데이터 라벨표시 



'''

# ================================================================
# 선 그래프 생성하기 : plot() 함수 ; 언어 따른 점유율 변화
# ================================================================
# 제목(title)과 라벨(label) 표시
# plt.title("파이썬의 언어 점유율", fontsize= 15)
# plt.xlabel("연도", fontsize= 15) # x 축
# plt.ylabel("점유율", fontsize=15) # y 축


# plt.plot(year, python, label='python')
# plt.plot(year, C, label='c')
# plt.plot(year, java, label='java')
# plt.plot(year, JS, label='js')


# 범례 표시(1)
# plt.legend(["Python","C","JAVA","JS"]) # (x값 실행 순서대로 지정)

#범례 표시(2)
# plt.legend() # legend()만 호출, 별도 label = 값 지정 

'''
(3) figure을 이용한 공간을 나누기  

'''

# ================================================================
# 방법(1) : 여러개의 figure을 나누기 
# ================================================================

# fig1 = plt.figure(1,figsize=(4,3)) # 이 아래서부터 그려지는 구성요소는 figure 1번에 그려진다
# plt.plot(year, python, label='Python')
# plt.title('Figure 1')

# fig2 = plt.figure(2, figsize=(4,3)) # 이 아래서부터 그려지는 구성요소는 figure 2번에 그려진다
# plt.plot(year,java,label='Java')
# plt.title('Figure 2')

# plt.figure(1) # 현재 도화지를 1번 도화지로 활성화(전환)
# plt.plot(year, java, label='JAVA')

# ================================================================
# 방법(2) : 하나의 figure를 여러 공간으로 나누기 
# ================================================================

# 하나의 도화지(figure) 안에서 공간을 여러개로 나누기 : subplots()
# subplot의 단점 : 각 차트 내용이 겹칠수 있음 -> constrained_layout 옵션 사용
# fig, (ax1, ax2) = plt.subplots(1,2, figsize= (10,6)) # 행, 열 (1행 2열 생성)
#fig, (ax1, ax2) = plt.subplots(2,1, constrained_layout=True ) # 행, 열 (1행 2열 생성)


#ax1.plot(year,python) # 왼쪽 공간
#ax2.plot(year,java) # 왼쪽 공간

# subplot에서는 set을 이용해여 라벨을 지정
#ax1.set_title('파이썬 점유율')
#ax2.set_title('자바 점유율')

#ax1.set_xlabel('연도')
#ax1.set_ylabel('점유율')
#ax2.set_xlabel('연도')
#ax2.set_ylabel('점유율')

'''

***** 예제 문제 *************

plt.subplots() 함수를 이용해 1행 3열로 총 세개의 서브플롯을 생성합니다. (레이아웃 조정 옵션 추가)
생성된 서브플롯은 변수 ax1, ax2, ax3에 저장합니다.

서브플롯 ax1
파이썬의 연도별 점유율을 선 그래프로 그립니다.
제목: "파이썬의 점유율"
x축 라벨: "연도"
y축 라벨: "점유율"

서브플롯 ax2
자바의 연도별 점유율을 선 그래프로 그립니다.
제목: "자바의 점유율"
x축 라벨: "연도"

서브 플롯 ax3
C언어의 연도별 점유율을 선 그래프로 그립니다.
제목: "C언어의 점유율"
x축 라벨: "연도"

'''
import matplotlib.pyplot as plt

# 폰트 사용 (사전에 폰트 설치, 순서 유의 )
plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False


# 예시데이터 
year = [2018, 2019, 2020, 2021, 2022, 2023]
python = [5.8, 8.17, 9.31, 11.87, 15.63, 14.51]
C = [13.59, 14.08, 16.72, 14.32, 12.71, 14.73]
java = [15.78, 15.04, 16.73, 11.23, 10.82, 13.23]
JS = [3.49, 2.51, 2.38, 2.44, 2.12, 2.1]


fig, (ax1,ax2,ax3) = plt.subplots(1,3,constrained_layout=True)

ax1.plot(python,year)
ax1.set_title("파이썬 점유율")
ax1.set_xlabel("연도")
ax1.set_xlabel("점유율")

ax2.plot(java,year)
ax2.set_title("자바의 점유율")
ax2.set_xlabel("연도")
ax2.set_xlabel("점유율")

ax3.plot(C,year)
ax3.set_title("C언어의 점유율")
ax3.set_xlabel("연도")
ax3.set_xlabel("점유율")



plt.show() # 실제 화면에 결과 출력



'''
(3) 차트의 추가 옵션 

'''
