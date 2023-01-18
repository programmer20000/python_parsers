import os

from icrawler.builtin import UrlListCrawler


def Download_image(dir_name='image', file_path=''):
    if os.path.exists(dir_name):
        os.mkdir(dir_name)
    else:
        print('folder already exists')

        links_image = UrlListCrawler(downloader_threads=4, storage={'root_dir': dir_name})
        links_image.crawl(url_list=file_path, file_idx_offset=0)


def main():
    Download_image(file_path='links_image_unic.txt')


if __name__ == '__main__':
    main()
