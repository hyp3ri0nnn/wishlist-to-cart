#!python

from selenium import webdriver
import time 
from tqdm import trange, tqdm
import argparse



# parser = argparse.ArgumentParser(description="get steam wishlist details.")
# parser.add_argument('--id', help="Enter your Steam id.") 
# parser.add_argument('--count', help="Number of games will added to cart.")
# parser.add_argument('--sort', help="sort types -> ['order', 'discount', 'price', 'name']") 

# # get query parameters
# def get_args(parser):
#     parser = parser
#     args = parser.parse_args()
#     id = args.id
#     game_count = int(args.count)
#     order_by = args.sort

#     return id, game_count, order_by
    


# id, game_count, order_by = get_args(parser=parser)


id = input("Enter your Steam id: ")
game_count = int(input("Enter number of games will be added to cart. (1-~): "))
order_by = input("Choose sort type sort types -> ['order', 'discount', 'price', 'name']")


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



games_root = driver.find_elements_by_xpath('//*[@id="wishlist_ctn"]')
games = driver.find_elements_by_class_name('wishlist_row')

for item in trange(15, game_count + 1):
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

