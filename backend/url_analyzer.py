import re
import socket
from urllib.parse import urlparse
from datetime import datetime


def parse_domain(url):
    parsed_url = urlparse(url)
    return parsed_url.netloc


def check_is_ip(domain):
    return bool(re.match(r"^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?\b){4}$", domain))


def get_whois_data(url):
    return {
        "valid": "Valid",
        "activeDuration": "10 years"
    }


def calculate_url_length(url):
    return len(url)


def check_special_char(url, char):
    return 1 if char in url else 0


def check_redirect(url):
    return 1 if '--' in url else 0


def domain_length(domain):
    return len(domain)


def count_subdomains(domain):
    return len(domain.split('.')) - 2


def fetch_page_rank(url):
    return "N/A"  # Placeholder: Replace with actual API integration if available


def get_url_attr(url):
    domain = parse_domain(url)
    return {
        "Domain": domain,
        "Ranking": fetch_page_rank(url),
        "isIp": check_is_ip(domain),
        "valid": get_whois_data(url)['valid'],
        "activeDuration": get_whois_data(url)['activeDuration'],
        "urlLen": calculate_url_length(url),
        "is@": check_special_char(url, '@'),
        "isredirect": check_redirect(url),
        "haveDash": check_special_char(domain, '-'),
        "domainLen": domain_length(domain),
        "noOfSubdomain": count_subdomains(domain)
    }
