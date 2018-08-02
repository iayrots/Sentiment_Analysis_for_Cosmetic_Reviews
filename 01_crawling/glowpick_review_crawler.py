from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time
import re

def glowpick_crawler(start_n, end_n):
    # make dataframe
    columns = ['product_name', 'brand_name', 'img_link','point', 'review']
    df = pd.DataFrame(columns=columns)

    # open window
    driver = webdriver.Chrome('/Users/yunah/Downloads/chromedriver')
    for number in range(start_n, end_n):
        driver.get('https://www.glowpick.com/product/' + str(number))

        # 리뷰가 없는 페이지 예외처리
        try:
            table = driver.find_element_by_css_selector('#gp-product-detail > div')
            review = table.find_element_by_css_selector('ul.section-list-wrap.side-bottom \
                                                        > li.section-list-review.side-right \
                                                        > section > ul > li:nth-child(1) > div > p')
            if review is None:
                continue
        except:
            continue

        # crawling data
        table = driver.find_element_by_css_selector('#gp-product-detail > div')
        data = {
            'product_name' : table.find_element_by_css_selector('h1').text,
            'brand_name' : table.find_element_by_css_selector('ul.section-list-wrap.side-top \
                                                                > li.section-list-info.side-right \
                                                                > div > section.section-list-item.product \
                                                                > div.wrap-brand > p').text,
            'img_link' : table.find_element_by_css_selector('img').get_attribute('src'),
            'point' : table.find_element_by_css_selector('p.score').text,
            'review' : table.find_element_by_css_selector('ul.section-list-wrap.side-bottom \
                                                            > li.section-list-review.side-right \
                                                            > section > ul > li:nth-child(1) > div > p').text,
        }
        df.loc[len(df)] = data

    driver.close()

    return df
