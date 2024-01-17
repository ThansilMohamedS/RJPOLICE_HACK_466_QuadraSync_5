import whois
import datetime
import requests
from bs4 import BeautifulSoup

def get_domain_info(domain_name):
    try:
        domain_info = whois.whois(domain_name)
        return domain_info
    except whois.parser.PywhoisError:
        return None

def check_ssl_certificate(domain_name):
    try:
        response = requests.get(f'https://{domain_name}')
        return response.ok
    except requests.RequestException:
        return False

def check_generic_content(domain_name):
    try:
        response = requests.get(f'https://{domain_name}')
        soup = BeautifulSoup(response.text, 'html.parser')

        has_head = soup.head is not None
        has_body = soup.body is not None
        has_title = soup.title is not None
        has_meta = soup.find('meta') is not None

        has_navigation = soup.find('nav') is not None or soup.find('header') is not None

        has_content = len(soup.find_all(['p', 'div', 'span', 'article', 'section'])) > 0

        threshold = 3  

        return (has_head + has_body + has_title + has_meta + has_navigation + has_content) >= threshold

    except requests.RequestException:
        pass
    
    return False

def check_website_legitimacy_v6(domain_name):
    domain_info = get_domain_info(domain_name)

    if domain_info is not None:
        creation_date = domain_info.creation_date
        if creation_date is not None:
            if type(creation_date) is list:
                creation_date = creation_date[0]

            current_date = datetime.datetime.now()
            domain_age = (current_date - creation_date).days

            ssl_valid = check_ssl_certificate(domain_name)

            if domain_age > 365 and ssl_valid:
                if check_generic_content(domain_name):
                    return True

    return False

if __name__ == "__main__":
    website_to_check = input("Enter the website URL: ")

    is_legitimate = check_website_legitimacy_v6(website_to_check)

    if is_legitimate:
        print(f"The website {website_to_check} appears to be legitimate.")
    else:
        print(f"The website {website_to_check} may not be legitimate.")
