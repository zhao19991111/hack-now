from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# return: list of productIds of this product


def target_sku_scraper(productName, num):
    browser = webdriver.Chrome()
    browser.get("https://www.target.com/s?searchTerm={0}".format(productName))
    try:
        product_id_list = []
        links = WebDriverWait(browser, 100).until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "a.Link-sc-1khjl8b-0.kTulu.h-display-block"))
        )
        itemUrl_list = []
        for i in range(num):
            itemUrl_list.append(links[i].get_attribute("href"))
        for url in itemUrl_list:
            browser.get(url)
            expandBtn = browser.find_element(
                By.CSS_SELECTOR, "button.Button-bwu3xu-0.kFNHSR")
            expandBtn.click()
            specItems = browser.find_elements(
                By.CSS_SELECTOR, "div.Col-favj32-0.fVmltG.h-padding-h-default div"
            )
            for j in range(len(specItems)):
                num = specItems[j].get_attribute("innerText").split(" ")[-1]
                parts = num.split("-")
                if len(parts) == 3:
                    product_id_list.append("".join(parts))
        return product_id_list
    finally:
        browser.quit()

# return: a dictionary of this object


def brickseek_scraper(productId, retailor):
    browser = webdriver.Chrome()
    browser.get("http://brickseek.com/{0}-inventory-checker/?sku={1}-{2}-{3}".format(
        retailor,
        productId[0:3], productId[3:5], productId[5:9]))
    zipcode = browser.find_element(
        By.CSS_SELECTOR, "#inventory-checker-form-zip")
    zipcode.send_keys("90024")
    image = browser.find_element(
        By.CSS_SELECTOR, ".item-overview__image-wrap img"
    )
    imageUrl = image.get_attribute("src")
    button = browser.find_element(
        By.CSS_SELECTOR, "div.grid__item-content button"
    )
    button.submit()
    shop_list = []
    addr_list = []
    available_list = []
    distance_list = []
    dollar_list = []
    cent_list = []
    price_list = []
    try:
        browser.implicitly_wait(100)
        addr_eles = browser.find_elements(By.CLASS_NAME, "address")
        available_eles = browser.find_elements(
            By.CLASS_NAME, "availability-status-indicator__text"
        )
        distance_eles = browser.find_elements(
            By.CLASS_NAME, "address__below"
        )
        dollar_eles = browser.find_elements(
            By.CLASS_NAME, "price-formatted__dollars"
        )
        cent_eles = browser.find_elements(
            By.CLASS_NAME, "price-formatted__cents"
        )
        for ele in addr_eles:
            addr_list.append(ele.get_attribute("innerText"))
        for ele in available_eles:
            available_list.append(ele.get_attribute("innerText"))
        for ele in distance_eles:
            distance_list.append(ele.get_attribute("innerText"))
        for ele in dollar_eles:
            dollar_list.append(ele.get_attribute("innerText"))
        for ele in cent_eles:
            cent_list.append(ele.get_attribute("innerText"))
        for i in range(len(addr_list)):
            addr_list[i] = addr_list[i].split(
                "\n")[0] + addr_list[i].split("\n")[1]
        for i in range(len(available_list)):
            if available_list[i] == "In Stock":
                available_list[i] = True
            else:
                available_list[i] = False
        for i in range(len(distance_list)):
            distance_list[i] = distance_list[i].replace("(", "").split(" ")[0]
        for i in range(len(dollar_list)):
            price_list.append(int(dollar_list[i]) + int(cent_list[i]) / 10)
        return {
            "imageUrl": imageUrl,
            "address": addr_list,
            "availability": available_list,
            "distance": distance_list,
            "price": price_list
        }
    finally:
        browser.quit()


# print(brickseek_scraper("063000577", "target"))
print(target_sku_scraper("milk", 4))
