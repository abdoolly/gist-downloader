from selenium import webdriver
import urllib.request as urlRequest

# URL
url = "https://gist.github.com/mbostock"

# Download To
download_path = "/home/elgenius/gist/"

# file name prefix to save with
filename = "mbostock-"

# download_button_xpath
download_xpath = "//*[@id=\"gist-pjax-container\"]/div[2]/div/div[2]/div[1]/div[3]/a"

# Path To Chrome Driver
path_to_chromedriver = './chromedriver'

#############

driver = webdriver.Chrome(executable_path=path_to_chromedriver)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get(url)

main_collection = driver.find_elements_by_class_name('creator')

links = []
download_links = []

for gist_item in main_collection:
    data_ref = gist_item.find_elements_by_tag_name('a')
    href = data_ref[1].get_attribute('href')
    links.append(href)

# geting the real download links
for link in links:
    driver.get(link)
    download_button = driver.find_element_by_xpath(download_xpath)
    download_zip_link = download_button.get_attribute('href')
    download_links.append(download_zip_link)

driver.quit()

print("downloading...")
# download the gists
for download_link_index in range(0, len(download_links)):
    print("Now Downloading " + str(download_link_index + 1) + " of " + str(len(download_links)))
    print("\n")
    urlRequest.urlretrieve(download_links[download_link_index],
                           download_path + filename + str(download_link_index + 1) + ".zip")
