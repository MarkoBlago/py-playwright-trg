from .base_page import BasePage

class CareersPage(BasePage):
       
    # region Elements

    def __init__(self, page):
        super().__init__(page)

        self.LifeAtTRG_Button = '[aria-label="#Life at TRG"]'

    # endregion

    # region Actions

    def click_life_at_trg(self):
        self.page.click(self.LifeAtTRG_Button)

    # endregion
