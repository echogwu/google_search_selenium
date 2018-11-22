from selenium.webdriver.common.by import By
from selenium import webdriver
import time, sys, argparse


def get_google_titles(search_text, sleep_time):
    wb = webdriver.Safari()
    try:
        wb.get("https://www.google.com")
        query = wb.find_element_by_name("q")
        query.send_keys(search_text)
        query.submit()
        time.sleep(sleep_time)
        titles = wb.find_elements_by_xpath('//*[@id="rso"]//a/h3')
        time.sleep(sleep_time)
        for i in range(len(titles)):
            print(f"title {i+1}: {titles[i].text}")
    except:
        print("Uh oh, something went wrong")
    finally:
        wb.close()


if __name__ == "__main__":
    # set default sleep time to 1 second if not set in the command line
    # sleep = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    parser = argparse.ArgumentParser(description='get the titles from the first page of google search on a topic')
    parser.add_argument(
        "--search",
        type=str,
        default="test automation is awesome",
        help="whatever you want to ask google for, defaut value: 'test automation is awesome'",
    )
    parser.add_argument(
        "--sleep",
        type=int,
        default=1,
        help="sleep time between operations in seconds, default value: 1",
    )
    args = vars(parser.parse_args())
    search_text = args["search"]
    sleep_time = args["sleep"]
    get_google_titles(search_text=search_text, sleep_time=sleep_time)
