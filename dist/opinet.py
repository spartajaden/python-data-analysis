from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By          
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup as bs
import pandas as pd
import time as tt

# 윈도우에서는 기본 옵션만으로 완벽하게 돌아갑니다.
options = Options()
options.add_argument("--window-size=1920,1080") 

driver = webdriver.Chrome(options=options)

driver.get('https://www.opinet.co.kr/user/main/mainUser.do')
print("오피넷 메인 접속 완료.")

# 팝업창 제거 및 이동
try:
    driver.execute_script("""
        var popups = document.querySelectorAll('.m_pop, [id^="pop"], .popup');
        popups.forEach(function(el) { el.style.display = 'none'; });
    """)
    area_menu = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#gnb > ul > li:nth-child(1) > ul > li:nth-child(1) > a"))
    )
    driver.execute_script("arguments[0].click();", area_menu)
    print("▶ 지역별 검색 페이지 이동 완료")
except Exception:
    driver.get('https://www.opinet.co.kr/searRgSelect.do')

# iframe 진입
try:
    WebDriverWait(driver, 7).until(EC.frame_to_be_available_and_switch_to_it((By.ID, "main_iframe")))
    print("🎯 iframe 내부 진입 성공!")
except Exception:
    tt.sleep(1.5) 
    driver.switch_to.frame(driver.find_element(By.ID, "main_iframe"))

# 부산광역시 선택
try:
    sido_element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#SIDO_NM0")))
    Select(sido_element).select_by_visible_text("부산광역시")
    print('✅ 부산광역시 변경 선택 완료!')
    tt.sleep(1.5) 
except Exception as e:
    print("❌ 드롭다운 선택 실패:", e)

# 파싱
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#body1 > tr")))
soup = bs(driver.page_source, 'html.parser')
contents = soup.select('#body1 > tr')

temp = [c.select_one('a').text.strip() for c in contents if c.select_one('a')]
print(f"\n찾은 주유소 개수: {len(temp)}개")
print(temp)

driver.quit()