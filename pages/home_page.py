from .base_page import BasePage

class HomePage(BasePage):

    # region Elements

    def __init__(self, page):
        super().__init__(page)
        
        self.WhoWeAre_Dropdown = "text=Who we are"
        self.Careers_Option = "text=Careers"
        self.LifeAtTRG_Button = '[aria-label="#Life at TRG"]'

    # endregion

    # region Actions

    def hover_who_we_are(self):
        self.page.hover(self.WhoWeAre_Dropdown)

    def click_careers(self):
        self.page.click(self.Careers_Option)

    # endregion
