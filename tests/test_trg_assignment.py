from pages.home_page import HomePage
from pages.careers_page import CareersPage
from pages.lifeAtTRG_page import TRGPage
from utils.utility import Utility


def test_automationTask(page, context):

    #region Task 1
    home = HomePage(page)
    home.navigate("https://www.trgint.com")

    home.hover_who_we_are()
    
    with context.expect_page() as new_page_info:
        home.click_careers()
    new_page = new_page_info.value

    careers = CareersPage(new_page)
    careers.click_life_at_trg()

    trg = TRGPage(new_page)

    trg.scroll_to_core_values()
    trg.save_text_to_JSON()
    trg.count_exclamation_marks_from_JSON()
    trg.download_and_name_images()
    
    #endregion

    #region Task 2

    util = Utility()

    print("Random name generated is: " + util.generate_random_name())

    #endregion