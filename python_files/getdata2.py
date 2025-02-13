from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def get_streak(username):
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run without UI
    chrome_options.add_argument("--disable-gpu")  # Required for some environments
    chrome_options.add_argument("--no-sandbox")  # Avoid issues in some systems
    chrome_options.add_argument("--disable-dev-shm-usage")  # Prevent memory issues

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

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
            return streak_element.text.strip()
        else:
            print("Streak not found")
    except Exception as e:
        print("Error:", e)
    finally:
        driver.quit()  # Ensure driver quits even if an error occurs

username = "Aaronthehedge32"
print(get_streak(username))
