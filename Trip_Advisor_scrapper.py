import csv #This package lets us save data to a csv file
from selenium import webdriver #The Selenium package we'll need
import time #This package lets us pause execution for a bit
import sys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
path_to_file = "C:/Users/paulo/Documents/REVIEW_TRIP_ADVISOR/Restaurants_Review.csv"

pages_to_scrape = 999999


# import the webdriver
url = "https://www.tripadvisor.com.br/Restaurant_Review-g303293-d1098021-Reviews-Coco_Bambu_Frutos_do_Mar-Fortaleza_State_of_Ceara.html"
driver = webdriver.Chrome()
driver.get(url)

time.sleep(5) 

driver.find_element_by_xpath('//*[@id="onetrust-accept-btn-handler"]').click()

# open the file to save the review
csvFile = open(path_to_file, 'a', encoding="utf-8")
csvWriter = csv.writer(csvFile)


# change the value inside the range to save the number of reviews we're going to grab
for i in range(0, pages_to_scrape):

    # give the DOM time to load
    time.sleep(5) 


    try:
        driver.find_element_by_xpath("//span[@class='taLnk ulBlueLinks']").click()
    except:
        print("Do Nothing")

    # Now we'll ask Selenium to look for elements in the page and save them to a variable. First lets define a  container that will hold all the reviews on the page. In a moment we'll parse these and save them:
    container = driver.find_elements_by_xpath(".//div[@class='review-container']")
    #print(len(container))



    # Next we'll grab the date of the review:
    
    print(f"Page Number {i}")
  
   # Now we'll look at the reviews in the container and parse them out

    for j in range(len(container)): # A loop defined by the number of reviews

        title = container[j].find_element_by_xpath(".//span[@class='noQuotes']").text
        date = container[j].find_element_by_xpath(".//span[contains(@class, 'ratingDate')]").get_attribute("title")
        rating = container[j].find_element_by_xpath(".//span[contains(@class, 'ui_bubble_rating bubble_')]").get_attribute("class").split("_")[3]
        review = container[j].find_element_by_xpath(".//p[@class='partial_entry']").text.replace("\n", " ")
        
        #Save that data in the csv and then continue to process the next review
        csvWriter.writerow([date, rating, title, review])
        
    # When all the reviews in the container have been processed, change the page and repeat            
    time.sleep(3) 
    try:
        next_button = driver.find_element_by_css_selector("#REVIEWS a.nav.next.ui_button.primary").click()
    except:
        print(f"FINISH AT PAGE NUMBER {i}!!!")
        break

    
#

# When all pages have been processed, quit the driver
driver.close()