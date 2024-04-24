import re
from datetime import datetime
from urllib.parse import urlparse

import whois


def parse_domain(url):
    updated_url = url
    if not (updated_url.startswith('http://') or updated_url.startswith('https://')):
        updated_url = 'http://' + updated_url

    parsed_url = urlparse(updated_url)
    domain = parsed_url.netloc
    if domain.startswith('www.'):
        return domain, domain[4:]

    return domain, domain


def check_is_ip(domain):
    return 1 if bool(re.match(r"^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?\b){4}$", domain)) else 0


def get_whois_details(domain):
    try:
        w = whois.whois(domain)
    except whois.parser.PywhoisError:
        return {'is_valid': 0, 'active_duration': 0}

    def normalize_date(date_field):
        if isinstance(date_field, list):
            date_field = date_field[0]
        return date_field

    registration_date = normalize_date(w.creation_date)
    expiration_date = normalize_date(w.expiration_date)

    is_valid = 1 if expiration_date and expiration_date > datetime.now() else 0

    if registration_date and expiration_date:
        active_duration = (expiration_date - registration_date).total_seconds() / 3600
    else:
        active_duration = 0
    return {'is_valid': is_valid, 'active_duration': active_duration}


def calculate_url_length(url):
    return len(url)


def check_special_char(url, char):
    return 1 if char in url else 0


def check_redirect(url):
    return 1 if '--' in url else 0


def domain_length(domain):
    return len(domain)


def count_subdomains(domain):
    return len(domain.split('.')) - 1


def fetch_page_rank(url):
    return "N/A"  # Placeholder: Replace with actual API integration if available


def get_url_attr(url):
    # ('isIp', 'valid', 'activeDuration', 'urlLen', 'is@', 'isredirect', 'haveDash', 'domainLen',
    #  'nosOfSubdomain')

    fq_domain, domain = parse_domain(url)
    who_is = get_whois_details(domain)
    return (
        check_is_ip(domain),
        who_is['is_valid'],
        who_is['active_duration'],
        calculate_url_length(url),
        check_special_char(url, '@'),
        check_redirect(url),
        check_special_char(url, '-'),
        domain_length(fq_domain),
        count_subdomains(url)
    )
