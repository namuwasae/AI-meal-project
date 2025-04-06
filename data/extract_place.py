import pandas as pd
import os

# 엑셀 파일 불러오기 (첫 번째 행을 헤더로 사용)
df = pd.read_excel("data/food1.xlsx", engine='openpyxl', header=0)

# 컬럼명 수정
df.columns = ['식품코드', '식품명', '식품기원명', '식품대분류코드', '식품대분류명', '영양성분함량기준량', 
              '에너지', '수분', '단백질', '지방', '회분', '탄수화물', '당류', '식이섬유',
              '칼슘', '철', '인', '칼륨', '나트륨', '비타민A', '레티놀', '베타카로틴',
              '티아민', '리보플라빈', '니아신', '비타민C', '비타민D', '콜레스테롤',
              '포화지방산', '트랜스지방산', '출처명', '식품중량', '데이터생성방법코드',
              '데이터생성방법명', '데이터생성일자', '데이터기준일자']

# 실제 데이터 행만 선택 (첫 번째 행 제외)
df = df.iloc[1:]

# data/grouped 디렉토리 생성
os.makedirs("data/grouped", exist_ok=True)

# 고유한 식품기원명 목록 추출
unique_origins = df['식품기원명'].unique()
print("\n=== 고유한 식품기원명 목록 ===")
print(unique_origins)

# 각 식품기원명별로 데이터 필터링하여 저장
for origin in unique_origins:
    # 해당 식품기원명을 가진 데이터만 필터링
    df_filtered = df[df['식품기원명'] == origin]
    
    # 파일명에서 사용할 수 없는 특수문자 처리
    safe_origin = origin.replace('(', '_').replace(')', '_').replace(' ', '_')
    
    # 결과를 새로운 엑셀 파일로 저장
    output_filename = f"data/grouped/grouped_{safe_origin}.xlsx"
    df_filtered.to_excel(output_filename, index=False)
    print(f"\n{origin} 데이터 저장 완료: {len(df_filtered)}개 행이 저장됨 -> {output_filename}")

print("\n모든 처리가 완료되었습니다.")