#!python

from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
from tqdm import trange, tqdm
import argparse
# import os 
# from pathlib import Path



# path_lib = Path(__file__).parent.absolute()
# drivers_path = os.path.join(path_lib, 'drivers')


 ################ ARGPARSE VERSION (uncomment, run from cmd with flags)
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
    
# print(drivers_path)
# geckodiver = os.path.join(drivers_path, 'geckodriver.exe')
# print(geckodiver)

# id, game_count, order_by = get_args(parser=parser)






# open browser
def choose_browser():
    browser_type = input("Choose your browser type: \nfor Firefox 'f'\nfor Chrome 'c'\nfor Opera 'o'\nfor Edge 'e'\n")
    if browser_type == 'f':
        driver = webdriver.Firefox()
    elif browser_type == 'c':
        driver = webdriver.Chrome()
    elif browser_type == 'o':
        driver = webdriver.Opera()
    elif browser_type == 'e':
        driver = webdriver.Edge('msedgedriver.exe')    
    return driver

def main_loop():
    id = input("Enter your Steam id: ")
    game_count = int(input("Enter number of games will be added to cart. (1-~): "))
    order_by = input("Choose sort type from (Note:order is custom order you created) -> ['order', 'discount', 'price', 'name']: ")

    # steam wishlist link
    STEAM_LINK = f"https://store.steampowered.com/wishlist/id/{id}/#sort={order_by}"
    print(id, game_count, order_by)



    driver = choose_browser()
    driver.get(STEAM_LINK)

    # wait page load
    # driver.implicitly_wait(5)
    time.sleep(2)

    index = 1 #ith game added to cart 

    # games_root = driver.find_element(By.XPATH, '//*[@id="wishlist_ctn"]')
    # games = driver.find_elements_by_class_name('wishlist_row')

    for item in trange(1, game_count + 1):
        time.sleep(1)
        if item >= 15:
            classifier = 2675 + (item - 15) * 180 
            execute = f"window.scrollTo(0,{classifier})"
            driver.execute_script(execute)
            item = 15
            time.sleep(1)
            
        
        
        purchase_text = driver.find_element(By.XPATH, f'/html/body/div[1]/div[7]/div[5]/div/div[2]/div/div[6]/div[{item}]/div[2]/div[1]/div[2]/div').find_element(By.TAG_NAME, 'span').text
        
        # print(purchase_text)
        

        if purchase_text == "View Details":
            button = driver.find_element(By.XPATH, f'/html/body/div[1]/div[7]/div[5]/div/div[2]/div/div[6]/div[{item}]/div[2]/div[1]/div[2]/div/a[1]')
            # go to game page
            button.click()

            age_check_url = driver.current_url
            
            if "agecheck" in age_check_url:
                age_verif = driver.find_element(By.XPATH, '//*[@id="ageYear"]/option[@value="1996"]').click()

                submit = driver.find_element(By.XPATH, '/html/body/div[1]/div[7]/div[5]/div/div[2]/div/div[1]/div[4]/a[1]')
                submit.click()
                                                        
                time.sleep(1)
            time.sleep(2)
            add_button = driver.find_element(By.CLASS_NAME, 'btn_addtocart')
            add_button.click()

            driver.get(STEAM_LINK)

        elif purchase_text == "Add to Cart":
            time.sleep(1)

            add_to_cart_button = driver.find_element(By.XPATH, f'/html/body/div[1]/div[7]/div[5]/div/div[2]/div/div[6]/div[{item}]/div[2]/div[1]/div[2]/div/form/a[1]')
            
            add_to_cart_button.click()
            driver.back()
            # time.sleep(1)
        
        # print(f"{index} item added to cart.")
        index += 1

if __name__ == "__main__":
    while True:
        main_loop()
        confirm_quit = input("press 'q' to quit\npress 'r' to restart\n")
        if confirm_quit == 'q':
            break
        elif confirm_quit == 'r':
            continue