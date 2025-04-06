# AI 메뉴 조합 프로젝트

## 폴더 구조
- data/
  - raw/: 원본 데이터 파일
    - grouped/: 그룹화된 원본 데이터
  - processed/: 정제된 데이터 파일
    - main_menu/: 메인메뉴 관련 데이터
    - etc/: 기타 정제된 데이터

- scripts/: 데이터 처리 스크립트
  - extract_main_menu.py: 메인메뉴 데이터 추출
  - extract_non_main_menu.py: 메인메뉴 제외 데이터 추출
  - process_food_data.py: 식품 데이터 처리
  
## 데이터 설명
1. 메인메뉴 데이터 (main_menu.xlsx)
   - 총 221개의 메인메뉴
   - 조리방법별로 분류됨 (구이, 조림, 찜 등)

2. 비메인메뉴 데이터 (non_main_menu.xlsx)
   - 총 568개의 메뉴
   - 국/탕류, 밥류, 나물류 등 포함
