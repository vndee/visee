import re
import os
import json
import yaml
from common.config import AppConf
from crawler.application.scraper import BasicWebDriver

s1 = u'ÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚÝàáâãèéêìíòóôõùúýĂăĐđĨĩŨũƠơƯưẠạẢảẤấẦầẨẩẪẫẬậẮắẰằẲẳẴẵẶặ' \
     u'ẸẹẺẻẼẽẾếỀềỂểỄễỆệỈỉỊịỌọỎỏỐốỒồỔổỖỗỘộỚớỜờỞởỠỡỢợỤụỦủỨứỪừỬửỮữỰựỲỳỴỵỶỷỸỹ'
s0 = u'AAAAEEEIIOOOOUUYaaaaeeeiioooouuyAaDdIiUuOoUuAaAaAaAaAaAaAaAaAaAaAaAaEe' \
     u'EeEeEeEeEeEeEeIiIiOoOoOoOoOoOoOoOoOoOoOoOoUuUuUuUuUuUuUuYyYyYyYy'

config = AppConf


def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)


def write_to_file(filename, obj_to_write):
    file_out = open(filename, mode='w', encoding='utf-8')
    file_out.write(json.dumps(obj_to_write, ensure_ascii=False, indent=4))
    file_out.close()


def remove_accents(input_str):
    s = ''
    for c in input_str:
        if c in s1:
            s += s0[s1.index(c)]
        else:
            s += c
    return s


class CategoriesWebDriver(BasicWebDriver):
    def __init__(self, _list_website, _dir_homepages, executable_path=None, timeout=15, wait=15):
        self.list_website = _list_website
        self.dir_homepages = _dir_homepages
        BasicWebDriver.__init__(
            self, executable_path=executable_path, timeout=timeout, wait=wait
        )

    def get_tiki_categories(self):
        list_categories_tag = self.driver.find_elements_by_class_name('Navigation__Wrapper-s3youc-0')[0]
        list_categories_tag = list_categories_tag.find_elements_by_tag_name('a')
        dict_categories = dict()
        for a_tag in list_categories_tag:
            _links = a_tag.get_attribute('href')
            dict_categories[_links.split('/')[3].replace('-', '_')] = _links
        return dict_categories

    def get_shopee_categories(self):
        dict_categories = dict()
        list_categories_tag = self.driver.find_elements_by_class_name('home-category-list')[0]
        list_categories_tag = list_categories_tag.find_elements_by_tag_name('a')
        for a_tag in list_categories_tag:
            category_name = re.sub(r'\s+', ' ', remove_accents(
                a_tag.find_elements_by_class_name('vvKCN3')[0].get_attribute('innerHTML')
            ).replace('-', '').replace('&amp;', '')).strip().replace(' ', '_').lower()
            dict_categories[category_name] = a_tag.get_attribute('href')
        print(dict_categories)
        return dict_categories

    def get_lazada_categories(self):
        dict_categories = dict()
        list_categories_tag = self.driver.find_elements_by_css_selector('ul.lzd-site-menu-root > ul > li > a')
        for li_tag in list_categories_tag:
            _links = li_tag.get_attribute('href')
            if _links is None:
                continue
            dict_categories[_links.split('/')[3].replace('-', '_')] = _links

        return dict_categories

    def get_sendo_categories(self):
        dict_categories = dict()
        list_categories_tag = self.driver.find_elements_by_class_name('title_140g')
        for h3_tag in list_categories_tag:
            _links = h3_tag.find_element_by_tag_name('a').get_attribute('href')
            if _links is None:
                continue
            dict_categories[_links.split('/')[3].replace('-', '_')] = _links

        return dict_categories

    def get_categories(self):
        for _website in self.list_website:
            self.get_html(_website)
            short_domain = _website.split('/')[2].replace('www.', '')
            file_name_out = os.path.join(self.dir_homepages, short_domain + '.yaml')
            if short_domain == 'tiki.vn':
                dict_categories = self.get_tiki_categories()
            elif short_domain == 'shopee.vn':
                dict_categories = self.get_shopee_categories()
            elif short_domain == 'lazada.vn':
                dict_categories = self.get_lazada_categories()
            elif short_domain == 'sendo.vn':
                dict_categories = self.get_sendo_categories()
            else:
                dict_categories = dict()
            dict_home_rules = yaml.safe_load(open(file_name_out, mode='r', encoding='utf-8'))
            dict_home_rules['categories'] = dict_categories
            file_rules = open(file_name_out, mode='w', encoding='utf-8')
            file_rules.write(yaml.dump(dict_home_rules))


if __name__ == '__main__':
    list_website = [
        'https://tiki.vn/',
        'https://www.lazada.vn/',
        'https://shopee.vn/',
        'https://www.sendo.vn/sitemap/',
    ]
    dir_homepages = 'rules/homepages/'
    wrapper = CategoriesWebDriver(
        list_website,
        dir_homepages,
        executable_path=config.driver_path
    )
    wrapper.get_categories()
