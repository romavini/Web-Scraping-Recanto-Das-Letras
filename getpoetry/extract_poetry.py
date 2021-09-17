from getpoetry.psql.database import read_db
from getpoetry.helpers import exception_handler, get_env, print_message
from time import sleep
import sys
from datetime import datetime
from random import random
from typing import Dict, List

import pandas as pd


class Extract:
    def __init__(self, browser):
        self.browser = browser

        _, er = self.login()
        if er == 2:
            self.quit("all")

        pages, er = self.get_pages()
        if er == 2 and not pages:
            self.quit("all")

        poems_href, er = self.get_poems_href(pages)
        if er == 2 and not poems_href:
            self.quit("all")

        print_message("Info", f"{len(poems_href)} new poems to add", "s")
        if not poems_href:
            self.quit("all")

        poems_list = self.get_poems_text(poems_href)
        self.quit("browser")
        self.data = pd.DataFrame(poems_list)

    def quit(self, q="browser"):
        if q == "all":
            self.browser.quit()
            sys.exit()
        elif q == "browser":
            self.browser.quit()

    @exception_handler
    def login(self):
        """Login into Recanto das Letras"""
        self.browser.get(
            "https://www.recantodasletras.com.br/escrivaninha/login/login.php?"
        )
        sleep(1 + random())

        page_element_login = self.browser.find_element_by_class_name("login-form-inner")

        user = page_element_login.find_element_by_name("usuario")
        user.click()
        sleep(0.5 + random())
        user.send_keys(get_env("user"))
        sleep(0.5 + random())

        password = page_element_login.find_element_by_name("senha")
        password.click()
        sleep(0.5 + random())
        password.send_keys(get_env("password"))
        sleep(0.5 + random())

        login_button = page_element_login.find_element_by_name("imageField")
        login_button.click()

    @exception_handler
    def get_pages(self) -> List[str]:
        """Return an list of pages with poems."""
        pages = ["https://www.recantodasletras.com.br/escrivaninha/publicacoes/index.php"]
        self.browser.get(pages[0])
        index = self.browser.find_element_by_class_name("index-pagination-descr")
        max_pages = int(index.text.split(" ")[-1].split(":")[0])
        for i in range(2, max_pages + 1):
            pages.append(
                "https://www.recantodasletras.com.br/escrivaninha/"
                f"publicacoes/index.php?pag={i}"
            )

        return pages

    @exception_handler
    def get_poems_href(self, pages: List[str]) -> List[Dict[str, str]]:
        """Return an list of dictionaries with title and href of each poem.

        Keyword arguments:
        pages -- List of pages."""

        db_poems = read_db("poems")
        if db_poems is None:
            db_titles = []
        else:
            db_titles = db_poems["title"].to_list()

        poems = []

        for page in pages:
            self.browser.get(page)
            sleep(1 + random())
            titles = self.browser.find_elements_by_class_name("index-title")[1:]
            categories = self.browser.find_elements_by_class_name("index-category")[1:]
            dates = self.browser.find_elements_by_class_name("index-date")[1:]
            views = self.browser.find_elements_by_class_name("index-views")[1:]

            for title, category, date, view in zip(titles, categories, dates, views):
                p = title.find_element_by_tag_name("a")

                if p.text in db_titles:
                    continue

                poem = {}
                poem["title"] = p.text
                poem["text"] = " "
                poem["href"] = p.get_attribute("href")
                poem["category"] = category.text
                poem["date"] = (
                    datetime.strftime(
                        datetime.strptime(date.text, "%d/%m/%y"), "%Y-%m-%d"
                    )
                    if ":" not in date.text
                    else datetime.strftime(datetime.now(), "%Y/%m/%d")
                )
                poem["views"] = view.text
                poems.append(poem)

        return poems

    @exception_handler
    def get_poem(self, href: str) -> str:
        """Return text of poem"""
        sleep(1 + random())
        self.browser.get(href)
        body = self.browser.find_element_by_class_name("boxtexto")
        divs = body.find_elements_by_tag_name("div")
        return divs[0].text

    def get_poems_text(self, poems_href: List[Dict[str, str]]) -> List[Dict[str, str]]:
        """Return a list of dicts with poems and infos

        Keyword arguments:
        poems_href -- list of dictionaries with infos of poems"""
        poem_list = []

        for poem_dict in poems_href:
            text, er = self.get_poem(poem_dict["href"])
            if er == 2:
                break
            poem_dict["text"] = text
            poem_list.append(poem_dict)

        return poem_list
