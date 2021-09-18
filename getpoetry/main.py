from getpoetry.extract_poetry import Extract
from getpoetry.helpers import get_env
from getpoetry.psql.database import write_into_db  # type: ignore
from selenium.webdriver import Chrome  # type: ignore


def main():
    browser = Chrome(
        get_env("chrome_driver_path")
    )  # Download webdriver at https://chromedriver.chromium.org/downloads

    ext = Extract(browser)

    write_into_db(ext.data, "poems")


if __name__ == "__main__":
    main()
