import allure
import pytest
from pages.main_page import MainPage
from data import url
from data import answers_dict


class TestMainPage:
    @allure.title("Проверка ответов на вопросы на главной странице")
    @pytest.mark.parametrize('num, res',
                             [
                                 [0, answers_dict["answer_0"]],
                                 [1, answers_dict["answer_1"]],
                                 [2, answers_dict["answer_2"]],
                                 [3, answers_dict["answer_3"]],
                                 [4, answers_dict["answer_4"]],
                                 [5, answers_dict["answer_5"]],
                                 [6, answers_dict["answer_6"]],
                                 [7, answers_dict["answer_7"]]
                             ])
    def test_answers_on_questions(self, driver, num, res):
        main_page = MainPage(driver)
        main_page.open_page(url["main_page"])
        assert main_page.get_answer_text(num) == res
