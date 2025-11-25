# Feature Engineering (특성공학)
#  : 모델이 더 좋은 예측을 할 수 있도록 의미 있는 변수(feature)를 만들고 다듬는 과정
#   -> Feature Creation : 기존 feature을 활용하여 새로운 feature를 생성하는 과정
#   -> Feature Selection : 데이터셋에서 가장 중요한 feature만 선택(불필요한 feature 제거)


# 차원의 저주(Curse of Dimensionality)
#   : Feature가 많아 질수록 데이터 공간(벡터 공간)이 기하급수적으로 커지는 현상 

# 차원의 저주 해결방법
#   - 데이터 샘플 수 증가(데이터 행)
#   - Feature Selection : 중요하지 않는 Feature은 제거
#   - Feature Reduction : 기존 Feature을 변환해 차우너 축소


# (1)  Feature Selection
#   : 가장 중요한 feature만 선택 (filter방식)
#     통계적 기준을 사용하여 가장 관련성 높은 상위 K개의 feature 선택 

# =========================================================
# Feature Transformation(1) 스케일링 or 정규화
# =========================================================
#  : 값의 범위를 조정 (수치형 데이터의 크기를 일정한 범위/단위로 맞추는 것)

# 1) Min-Max Scaling 
# 
# 2) Robust Scaling 
#   - 이상치가 많을 때 유용 


# =========================================================
# Feature Transformation(2) 인코딩(Encoding)
# =========================================================
#   : 범주형 데이터를 모델이 이해할 수 있도록 숫자로 변환 


# 1) Label Encoding 
# - Category값을 차례대로 숫자로 각각 매핑

# 2) One-Hot Encoding 
# - 각 category마다 새로운 이진 컬럼을 생성 
# - 대부분의 값이 0 -> 메모리 낭비 



# =========================================================
# Feature Engineering 그외. 결측값 처리, 이상치 처리 
# =========================================================