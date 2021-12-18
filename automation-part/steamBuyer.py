

from selenium import webdriver
import time 
import sys
import argparse
from tqdm import tqdm
from tqdm.std import trange


parser = argparse.ArgumentParser(description="get steam details.")
parser.add_argument('--id') 
parser.add_argument('--count')
parser.add_argument('--sort') 

# get query parameters
def get_args(parser):
    parser = parser
    args = parser.parse_args()
    id = args.id
    game_count = int(args.count)
    order_by = args.sort

    return id, game_count, order_by
    


id, game_count, order_by = get_args(parser=parser)
print(id, game_count, order_by)

# steam wishlist link
STEAM_LINK = f"https://store.steampowered.com/wishlist/id/{id}/#sort={order_by}"

# open browser
driver = webdriver.Firefox()
driver.get(STEAM_LINK)

# wait page load
# driver.implicitly_wait(5)
time.sleep(2)

index = 1 #ith game added to cart 

# cookies = driver.get_cookies()
# print(cookies)

games_root = driver.find_elements_by_xpath('//*[@id="wishlist_ctn"]')
games = driver.find_elements_by_class_name('wishlist_row')
# xpath = /html/body/div[1]/div[7]/div[5]/div/div[2]/div/div[6]/div[1]
# xpath 2 = /html/body/div[1]/div[7]/div[5]/div/div[2]/div/div[6]/div[2]
# for item in tqdm(0, game_count):
for item in range(15, game_count + 1):
    time.sleep(2)
    if item >= 15:
        classifier = 2675 + (item - 15) * 180 
        execute = f"window.scrollTo(0,{classifier})"
        driver.execute_script(execute)
        item = 15
        time.sleep(1)
        
    
    
    purchase_text = driver.find_element_by_xpath(f'/html/body/div[1]/div[7]/div[5]/div/div[2]/div/div[6]/div[{item}]/div[2]/div[1]/div[2]/div').find_element_by_tag_name('span').text
    
    # print(purchase_text)
    

    if purchase_text == "View Details":
        button = driver.find_element_by_xpath(f'/html/body/div[1]/div[7]/div[5]/div/div[2]/div/div[6]/div[{item}]/div[2]/div[1]/div[2]/div/a[1]')
        # go to game page
        button.click()

        age_check_url = driver.current_url
        
        if "agecheck" in age_check_url:
            age_verif = driver.find_element_by_xpath('//*[@id="ageYear"]/option[@value="1996"]').click()
            # age_verif.click()
            # age_select = driver.find_element_by_xpath('/html/body/div[1]/div[7]/div[4]/div/div[2]/div/div[1]/div[3]/select[3]/option[100]')
            # age_select.click()
            submit = driver.find_element_by_xpath('/html/body/div[1]/div[7]/div[5]/div/div[2]/div/div[1]/div[4]/a[1]')
            submit.click()
                                                       
            time.sleep(4)

        add_button = driver.find_element_by_class_name('btn_addtocart')
        add_button.click()

        driver.get(STEAM_LINK)

    elif purchase_text == "Add to Cart":
        time.sleep(1)

        add_to_cart_button = driver.find_element_by_xpath(f'/html/body/div[1]/div[7]/div[5]/div/div[2]/div/div[6]/div[{item}]/div[2]/div[1]/div[2]/div/form/a[1]')
        add_to_cart_button.click()
        driver.back()
        time.sleep(2)
    
    print(f"{index} item added to cart.")
    index += 1

#     #Add to Cart and return to wishlist.  
#     elif check == "Add to Cart":
#         gameName = browser.current_url
#         time.sleep(1)
#         btn = browser.find_element_by_xpath(f'/html/body/div[1]/div[7]/div[4]/div/div[2]/div/div[6]/div[{i}]/div[2]/div[1]/div[2]/div/form')
#         btn.click()
#         browser.back()
    

#     #Print the ith game added to cart.     
#     print(f"{i+n} --> Item Added to Cart")
    


# #These sleep() functions to wait load of the page.
# time.sleep(2)
# n= 0 #i-th game added to cart.
# for i in range(1,int(gameCount)+2):
#     time.sleep(2)
    
#     #After the 15th item, page will be scrolled to down. 
#     if i > 15:
#         classifier = 2675 + (i - 15) * 176 
#         execute = f"window.scrollTo(0,{classifier})"
#         browser.execute_script(execute)
#         i = 15
#         n += 1
    
#     # Check the button name. Some games have "View Details" instead of "Add To Cart". 
#     check = browser.find_element_by_xpath(f"/html/body/div[1]/div[7]/div[4]/div/div[2]/div/div[6]/div[{i}]/div[2]/div[1]/div[2]/div").find_element_by_tag_name("span").text
    
#     if check == "View Details":
#         btn = browser.find_element_by_xpath(f"/html/body/div[1]/div[7]/div[4]/div/div[2]/div/div[6]/div[{i}]/div[2]/div[1]/div[2]/div/a[1]")
#         btn.click()
#         time.sleep(1)
#         gameName = browser.current_url

#         #Check the current page url to check if there is "Age Verification".
#         ageCheckUrl = browser.current_url
#         # print(ageCheckUrl)

#         if "agecheck" in ageCheckUrl:
#             ageVer = browser.find_element_by_xpath('//*[@id="ageYear"]')
#             ageVer.click()
#             age = browser.find_element_by_xpath('/html/body/div[1]/div[7]/div[4]/div/div[2]/div/div[1]/div[3]/select[3]/option[100]')
#             age.click()
#             verification = browser.find_element_by_xpath('/html/body/div[1]/div[7]/div[4]/div/div[2]/div/div[1]/div[4]/a[1]')
#             verification.click()
#             # Set the year of Age to 1999 and Continue to item page.
        
#         #Careful for low bandwith internet users. Steam page will load game videos first so set the sleep() function more than others.
#         time.sleep(4)


# #  # # # # ## # # # ## # # ## # # # ## # # ## # # ## # # # ## # 

#         addBtn = browser.find_element_by_class_name('btn_addtocart')
#         gameName = browser.current_url
#         addBtn.click()
#         #Return to wishlist after the adding game to cart.
#         browser.get(steam)