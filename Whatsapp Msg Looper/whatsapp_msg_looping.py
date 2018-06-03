"""
whatsapp_msg_looper - Takes username, message and no.of tymes msg should be looped
                      and loops the message(conditioned you hv to login to whatsapp web). 
"""
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


def main():
    """
    :return: Null
    """

    # Initialize url and open
    
    url = "https://web.whatsapp.com/"
    
    driver = webdriver.Chrome()

    driver.get(url)

    username = ""

    message = ""

    number = 1

    op = 0

    # Getting user input (option)
    
    while op != 3:

        op = int(input(" \nEnter your option:\n 1.New user\n 2.same user\n 3.Quit\n\n Enter your option : "))

        if op == 1:

            # Getting username, message and no.of tymes msg should be repeated

            username = input(" Enter users name(Full name) : ")

            message = input(" Enter the message to be sent : ")

            number = int(input(" No.of repetitions : "))

            # Selecting user
            
            link = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '//input[@class="jN-F5 copyable-text selectable-text"]')))
            ActionChains(driver).move_to_element(link).perform()
            link.send_keys(username)

            # Clicking on user chat

            link = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '//div[@class="_3j7s9"]')))
            ActionChains(driver).move_to_element(link).perform()
            link.click()
            
            for i in range(number):

                # Selecting and typing message
                
                link = WebDriverWait(driver, 30).until(
                    EC.element_to_be_clickable((By.XPATH, '//div[@class="_2S1VP copyable-text selectable-text"]')))
                ActionChains(driver).move_to_element(link).perform()
                link.send_keys(message)

                time.sleep(1)

                # Sending message
                
                link = WebDriverWait(driver, 30).until(
                    EC.element_to_be_clickable((By.XPATH, '//button[@class="_2lkdt"]')))
                ActionChains(driver).move_to_element(link).perform()
                link.click()

        elif op == 2:

            _op = input(" \nEnter your opt :\n a.New message\n b.Repeat\n c.Quit\n\n Enter your option : ")

            if _op == "a":

                # Getting message and no.of tymes msg should be repeated

                message = input(" Enter the message to be sent : ")

                number = int(input(" No.of repetitions : "))

                for i in range(number):

                    # Selecting and typing message

                    link = WebDriverWait(driver, 30).until(
                        EC.element_to_be_clickable((By.XPATH, '//div[@class="_2S1VP copyable-text selectable-text"]')))
                    ActionChains(driver).move_to_element(link).perform()
                    link.send_keys(message)

                    time.sleep(1)

                    # Sending message
                    
                    link = WebDriverWait(driver, 30).until(
                        EC.element_to_be_clickable((By.XPATH, '//button[@class="_2lkdt"]')))
                    ActionChains(driver).move_to_element(link).perform()
                    link.click()

            elif _op == "b":

                for i in range(number):

                    # Selecting and typing message

                    link = WebDriverWait(driver, 30).until(
                        EC.element_to_be_clickable((By.XPATH, '//div[@class="_2S1VP copyable-text selectable-text"]')))
                    ActionChains(driver).move_to_element(link).perform()
                    link.send_keys(message)

                    time.sleep(1)

                    # Sending message
                    
                    link = WebDriverWait(driver, 30).until(
                        EC.element_to_be_clickable((By.XPATH, '//button[@class="_2lkdt"]')))
                    ActionChains(driver).move_to_element(link).perform()
                    link.click()

            elif _op == "c":
                
                break

            else:

                print(" Invalid input")

        elif op == 3:

            break

        else:

            print(" Invalid input")

if __name__ == "__main__":
    main()
