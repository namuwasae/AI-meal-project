import pandas as pd
import os

# 데이터 읽기
df = pd.read_excel('data/grouped/grouped_산업체급식_재료량_기반_산출_함량_.xlsx')

# '찌개 및 전골류'와 '국 및 탕류'를 하나의 카테고리로 통합
df['식품대분류명'] = df['식품대분류명'].replace({'찌개 및 전골류': '국/찌개류', '국 및 탕류': '국/찌개류'})

# 결과물을 저장할 디렉토리 생성
output_dir = 'categorized_food'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 식품대분류명으로 그룹화하여 각각 새로운 파일 생성
for category in df['식품대분류명'].unique():
    category_df = df[df['식품대분류명'] == category]
    output_filename = f"{output_dir}/{category.replace('/', '_')}_foods.xlsx"
    category_df.to_excel(output_filename, index=False)
    print(f"Created: {output_filename}") 