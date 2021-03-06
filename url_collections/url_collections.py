"""
Program:
    Collection of url functions
Author:
    haw
Version:
    0.2
Note:
    Version 0.2 change _image_request parameter: header
    Not compatible with previous Version 0.1.X
"""

import os, re
import html, collections, hashlib
import time, datetime, random

import requests


def extract_images(input_file, duplicates=False, extension=True):
    """
    Extract each image url from input_file.

    duplicates:
        False - Return a list of urls with no duplicates
        True - Return a list of urls with duplicates
    extension:
        False - Extract urls that start with http / https only
        True - Extract urls that start with http / https and ends with image extension

    Image Extension:
        jpg, jpeg, png
    Return:
        A list of urls
    Error:
        FileNotFoundError - Raised if input_file can't be read properly
    """

    # Image url regular expression
    if extension:
        URL_REGEX = r'((http)(s)?(\S)*(\.jpg|\.jpeg|\.png))'
    else:
        URL_REGEX = r'((http)(s)?(\S)*)'
    url_regex = re.compile(URL_REGEX, re.IGNORECASE)

    # Extract urls
    try:
        with open(input_file, mode='rt', encoding='utf-8') as file:
            content = file.read()
            content = html.unescape(content)
            urls = url_regex.findall(content)
    except FileNotFoundError as err:
        print('Read file error {}: {}'.format(err.errno, err.strerror))
        raise

    # Return duplicate urls
    if duplicates:
        urls_list = []
        for url in urls:
            urls_list.append(url[0])
        return urls_list

    # Avoid storing duplicate urls
    urls_dict = collections.OrderedDict()
    for url in urls:
        hash_val = hashlib.sha256(url[0].encode()).hexdigest()
        hash_val = hash_val[:10]
        urls_dict[hash_val] = url[0]

    # Return list
    return list(urls_dict.values())



def download_image(url, target_path, header=None):
    """
    Download image from urls to destination

    Parameters:
        file_path - File storing destination
    Error:
        FileNotFoundError - File path not found
        urlError - Raised if image request failed
    """
    # Request for image file
    print('Header: {}'.format(header))
    for _ in range(5):
        try:
            print('Request URL: {}'.format(url))
            img_request = _image_request(url, header)
            break
        except RuntimeError:
            time.sleep(1)
    else:
        raise ReferenceError('Request for image {} failed'.format(url))

    # Write image to file_path
    _image_write(img_request, target_path)
    print('Download {} success'.format(target_path))



def download_images(urls, target_directory, header=None):
    """
    Download images and save into directory

    Parameters:
        urls - iterable
    Error:
        FileNotFoundError - File path not found
    Reutrn:
        List of error messages that occur during image download
    """
    errors = []

    for index, url in enumerate(urls):
        for _ in range(10):
            try:
                img_request = _image_request(url, header)
            except RuntimeError:
                time.sleep(1)
            else:
                filename = datetime.datetime.now().strftime('%Y%m%dT%H%M%SMS%f')
                _image_write(img_request, os.path.join(target_directory, filename))
                print('Download index {:>3} - URL {} success'.format(index, url))
                break
        else:
            print('Download index {:>3} - URL {} exceed attempt limit'.format(index, url))
            errors.append('Index {:>3} exceed request attempt limit: {}'.format(index, url))
        time.sleep(random.uniform(1, 2.5))

    return errors



def _image_request(url, header=None):
    """
    Request for image from url

    Return:
        Requested object
    Error:
        RuntimeError - Raised if failed to request for image
    """
    # Request for image
    if header:
        print('Run with header')
        image_request = requests.get(url, headers=header)
    else:
        print('Run without header')
        image_request = requests.get(url)

    # Check status code
    if image_request.status_code == 200:
        return image_request
    else:
        print('Respond Code: {}'.format(image_request.status_code))
        raise RuntimeError('Request for image failed')



def _image_write(image, file_path):
    """
    Save image to destination

    Parameter:
        image - Request object
    Error:
        FileNotFoundError - File path not found
    """
    try:
        with open(file_path, mode='wb') as file:
            for chunk in image:
                file.write(chunk)
    except FileNotFoundError as err:
        print('Write file error {}: {}'.format(err.errno, err.strerror))
        raise



class urlError(Exception):
    """
    Raise when error occurs during the use of url_collections module
    """
    pass


if __name__ == '__main__':
    # Test extract_images
    urls = extract_images('test.csv')
    print(urls)

    # Test download_image
    download_image('https://r.hswstatic.com/w_907/gif/tesla-cat.jpg', 'test_cat.jpg')

    # Test download_image with user-agent
    download_image('https://r.hswstatic.com/w_907/gif/tesla-cat.jpg', 'test_cat2.jpg', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')

    # Test download_images
    download_images(urls, 'Test_Dir', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')
