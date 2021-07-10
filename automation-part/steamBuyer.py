from selenium import webdriver
import time 
import sys


gameCount = sys.argv[3] # Specify how many games will be added to cart. 
orderType = sys.argv[2] # Specify sort type of wishlist. [Custom Order, Price, Discount etc. ]
steamId = sys.argv[1] #Specify the user id. 

# print(steamId,orderType,gameCount)

#Create the link of wishlist of given id.
steam = f"https://store.steampowered.com/wishlist/id/{steamId}/#sort={orderType}"

#Open Broser and go to Steam page.
browser = webdriver.Firefox()
browser.get(steam)

#These sleep() functions to wait load of the page.
time.sleep(2)
n= 0 #i-th game added to cart.
for i in range(1,int(gameCount)+2):
    time.sleep(2)
    
    #After the 15th item, page will be scrolled to down. 
    if i > 15:
        classifier = 2675 + (i - 15) * 176 
        execute = f"window.scrollTo(0,{classifier})"
        browser.execute_script(execute)
        i = 15
        n += 1
    
    # Check the button name. Some games have "View Details" instead of "Add To Cart". 
    check = browser.find_element_by_xpath(f"/html/body/div[1]/div[7]/div[4]/div/div[2]/div/div[6]/div[{i}]/div[2]/div[1]/div[2]/div").find_element_by_tag_name("span").text
    
    if check == "View Details":
        btn = browser.find_element_by_xpath(f"/html/body/div[1]/div[7]/div[4]/div/div[2]/div/div[6]/div[{i}]/div[2]/div[1]/div[2]/div/a[1]")
        btn.click()
        time.sleep(1)
        gameName = browser.current_url

        #Check the current page url to check if there is "Age Verification".
        ageCheckUrl = browser.current_url
        # print(ageCheckUrl)

        if "agecheck" in ageCheckUrl:
            ageVer = browser.find_element_by_xpath('//*[@id="ageYear"]')
            ageVer.click()
            age = browser.find_element_by_xpath('/html/body/div[1]/div[7]/div[4]/div/div[2]/div/div[1]/div[3]/select[3]/option[100]')
            age.click()
            verification = browser.find_element_by_xpath('/html/body/div[1]/div[7]/div[4]/div/div[2]/div/div[1]/div[4]/a[1]')
            verification.click()
            # Set the year of Age to 1999 and Continue to item page.
        
        #Careful for low bandwith internet users. Steam page will load game videos first so set the sleep() function more than others.
        time.sleep(4)
        addBtn = browser.find_element_by_class_name('btn_addtocart')
        gameName = browser.current_url
        addBtn.click()
        #Return to wishlist after the adding game to cart.
        browser.get(steam)
    
    
    #Add to Cart and return to wishlist.  
    elif check == "Add to Cart":
        gameName = browser.current_url
        time.sleep(1)
        btn = browser.find_element_by_xpath(f'/html/body/div[1]/div[7]/div[4]/div/div[2]/div/div[6]/div[{i}]/div[2]/div[1]/div[2]/div/form')
        btn.click()
        browser.back()
    

    #Print the ith game added to cart.     
    print(f"{i+n} --> Item Added to Cart")
    


