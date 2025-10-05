from .base_page import BasePage
import json
import requests


class TRGPage(BasePage):

    # region Elements
    def __init__(self, page):
        super().__init__(page)

        self.core_values_first_headline_text = "text=Whatever it takes!"
        self.core_value_second_headline_text = "text=We work together."
        self.core_value_third_headline_text = "text=We make an impact."
        self.core_value_fourth_headline_text = "text=Passion is our fuel."

        self.first_core_value_description_text = 'p:has-text("We are always on the go.")'
        self.second_core_value_description_text = 'p:has-text("One for all and all for one")'
        self.third_core_value_description_text = 'p:has-text("We foster innovation and always")'
        self.fourth_core_value_description_text = 'p:has-text("We work with passion")'

        self.first_img = self.page.locator("xpath=//img[@sizes='243px']").nth(0)
        self.second_img = self.page.locator("xpath=//img[@sizes='243px']").nth(1)
        self.third_img = self.page.locator("xpath=//img[@sizes='243px']").nth(2)
        self.fourth_img = self.page.locator("xpath=//img[@sizes='243px']").nth(3)

    # endregion

    # region Actions

    def scroll_to_core_values(self):
        self.page.locator(self.core_values_first_headline_text).scroll_into_view_if_needed()

    def get_first_core_value_text(self):
        return self.page.text_content(self.first_core_value_description_text)
    
    def get_second_core_value_text(self):
        return self.page.text_content(self.second_core_value_description_text)
    
    def get_third_core_value_text(self):
        return self.page.text_content(self.third_core_value_description_text)
    
    def get_fourth_core_value_text(self):
        return self.page.text_content(self.fourth_core_value_description_text)
    
    def get_first_headline_text(self):
        return self.page.text_content(self.core_values_first_headline_text)
    
    def get_second_headline_text(self):
        return self.page.text_content(self.core_value_second_headline_text)
    
    def get_third_headline_text(self):
        return self.page.text_content(self.core_value_third_headline_text)
    
    def get_fourth_headline_text(self):
        return self.page.text_content(self.core_value_fourth_headline_text)
    

    def save_text_to_JSON(self):
        text1 = self.get_first_headline_text() + " " + self.get_first_core_value_text()
        text2 = self.get_second_headline_text() + " " + self.get_second_core_value_text()
        text3 = self.get_third_headline_text() + " " + self.get_third_core_value_text()
        text4 = self.get_fourth_headline_text() + " " + self.get_fourth_core_value_text()

        data = {
            "CoreValue1":text1,
            "CoreValue2":text2,
            "CoreValue3":text3,
            "CoreValue4":text4
        }

        with open("CoreValues.json", "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)


    def count_exclamation_marks_from_JSON(self):
        with open("CoreValues.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        total_Exclamations = 0

        for value in data.values():
            total_Exclamations = total_Exclamations + value.count("!")
            
        print("Number of total exlamation marks is: " + str(total_Exclamations))

    def download_and_name_images(self):
        
        FirstImgSrc = self.first_img.get_attribute("src")
        SecondImgSrc = self.second_img.get_attribute("src")
        ThirdImgSrc = self.third_img.get_attribute("src")
        FourthImgSrc = self.fourth_img.get_attribute("src")

        response = requests.get(FirstImgSrc)
        with open(self.get_first_headline_text()+".jpg", "wb") as firstImage:
            firstImage.write(response.content)

        response = requests.get(SecondImgSrc)
        with open(self.get_second_headline_text()+".jpg", "wb") as secondImage:
            secondImage.write(response.content)

        response = requests.get(ThirdImgSrc)
        with open(self.get_third_headline_text()+".jpg", "wb") as thirdImage:
            thirdImage.write(response.content)

        response = requests.get(FourthImgSrc)
        with open(self.get_fourth_headline_text()+".jpg", "wb") as fourthImage:
            fourthImage.write(response.content)

    # endregion
