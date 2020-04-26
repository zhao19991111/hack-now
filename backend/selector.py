from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# return: list of productIds of this product
CHROMEDRIVER_PATH = '/usr/local/bin/chromedriver'
WINDOW_SIZE = "1920,1080"
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
chrome_options.add_argument('--no-sandbox')


def target_id_scraper(productName, num):
    browser = webdriver.Chrome(
        executable_path=CHROMEDRIVER_PATH, options=chrome_options)
    browser.get("https://www.target.com/s?searchTerm={0}".format(productName))
    try:
        product_id_list = []
        waitItem = WebDriverWait(browser, 50).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "h2.Heading__StyledHeading-sc-1m9kw5a-0.eZNcif.hideAuxtext"))
        )
        links = WebDriverWait(browser, 50).until(
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
        browser.close()


def walmart_id_scraper(productName, num):
    browser = webdriver.Chrome(
        executable_path=CHROMEDRIVER_PATH, options=chrome_options)
    browser.get(
        "https://www.walmart.com/search/?query={0}".format(productName))
    try:
        product_id_list = []
        links = WebDriverWait(browser, 50).until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "a.search-result-productimage.gridview.display-block"))
        )
        for i in range(num):
            product_id_list.append(
                links[i].get_attribute("href").split("/")[-1].split("?")[0])
        return product_id_list
    finally:
        browser.close()


def cvs_id_scraper(productName, num):
    browser = webdriver.Chrome(
        executable_path=CHROMEDRIVER_PATH, options=chrome_options)
    browser.get(
        "https://www.cvs.com/search/?searchTerm={0}".format(productName))
    try:
        product_id_list = []
        links = WebDriverWait(browser, 50).until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "a.css-4rbku5.css-18t94o4.css-1dbjc4n.r-14lw9ot.r-1lz4bg0.r-rs99b7.r-s211iu.r-1loqt21.r-1pi2tsx.r-1udh08x.r-19yat4t.r-1j3t67a.r-1otgn73.r-13qz1uu")
            )
        )
        for i in range(num):
            product_id_list.append(links[i].get_attribute(
                "href").split("/")[-1].split("-")[-1])
        return product_id_list
    finally:
        browser.close()

# return: a dictionary of this object


def brickseek_scraper(productId, _zip, retailer):
    browser = webdriver.Chrome(
        executable_path=CHROMEDRIVER_PATH, options=chrome_options)
    browser.get("http://brickseek.com/{0}-inventory-checker/?sku={1}-{2}-{3}".format(
        retailer,
        productId[0:3], productId[3:5], productId[5:9]))
    zipcode = browser.find_element(
        By.CSS_SELECTOR, "#inventory-checker-form-zip")
    zipcode.send_keys(_zip)
    try:
        image = browser.find_element(
            By.CSS_SELECTOR, ".item-overview__image-wrap img"
        )
        imageUrl = image.get_attribute("src")
    except:
        return {}
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
        browser.implicitly_wait(20)
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
<<<<<<< HEAD
            "product_id": productId,
=======
<<<<<<< HEAD
            "product_id": productId,
=======
            "productId": productId,
>>>>>>> d4c609e3a8ad44b3650aa04aa127d947c92ba39f
>>>>>>> 1150cbc0e27a6673ab301542d1857a42a31ddaeb
            "imageUrl": imageUrl,
            "address": addr_list,
            "availability": available_list,
            "distance": distance_list,
            "price": price_list,
            "zipcode": str(_zip)
        }
    except:
        return {}
    finally:
        browser.close()


def searchWithIds(productName, number, _zip, retailer):
    search_result = []
    product_id_list = []
    if retailer == "walmart":
        product_id_list = walmart_id_scraper(productName, number)
    elif retailer == "target":
        product_id_list = target_id_scraper(productName, number)
    elif retailer == "cvs":
        product_id_list = cvs_id_scraper(productName, number)
    for productId in product_id_list:
        print("Search with id: {0}".format(productId))
        search_result.append(brickseek_scraper(productId, _zip, retailer))
    return search_result


# print(brickseek_scraper("063000577", "90024", "target"))
# print(target_id_scraper("milk", 4))
# print(walmart_id_scraper("biscuit", 4))
# print(cvs_id_scraper("biscuit", 4))
print(searchWithIds("biscuit", 5, "90024", "cvs"))
