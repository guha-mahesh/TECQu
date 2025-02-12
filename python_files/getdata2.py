from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


username = "Aaronthehedge32"
url = f"https://www.duolingo.com/profile/{username}"


driver.get(url)


driver.implicitly_wait(5)

try:

    streak_element = None
    streak_elements = driver.find_elements(By.CSS_SELECTOR, "h4.-TMd4") 

    for elem in streak_elements:
        if elem.text.isdigit():  
            streak_element = elem
            break

    if streak_element:
        print("Streak:", streak_element.text.strip())
    else:
        print("Streak not found")
except Exception as e:
    print("Error:", e)


driver.quit()
