import unittest

from url_analyzer import *


class TestURLAnalysis(unittest.TestCase):

    def test_parse_domain(self):
        self.assertEqual(parse_domain("http://example.com"), "example.com")

    def test_domain_names(self):
        domain_names = [
            "example.com",
            "www.example.com",
            "subdomain.example.com",
            "example.co.uk",
            "192.168.1.1.com",  # Looks like an IP, but it's a domain
            "255.com",  # Looks like part of an IP
            "www.12345.com",  # Starts with numbers, but not an IP
            "10.0.com",  # Looks like part of an IP
            "domain.name",  # Uncommon TLD
            "localhost",  # Special hostname
            "user@domain.com",  # Email, not a domain
            "example.com:80",  # Domain with port
            "ftp://192.168.1.1",  # URL with scheme
            "https://example.com/path?query=string"  # Full URL
        ]
        for domain in domain_names:
            with self.subTest(domain=domain):
                self.assertFalse(check_is_ip(domain))

    def test_valid_ips(self):
        valid_ips = [
            "192.168.1.1",
            "255.255.255.255",
            "0.0.0.0",
            "127.0.0.1"
        ]
        for ip in valid_ips:
            with self.subTest(ip=ip):
                self.assertTrue(check_is_ip(ip))

    def test_invalid_ips(self):
        invalid_ips = [
            "192.168.1.256",  # last octet too large
            "256.255.255.255",  # first octet too large
            "192.168.1",  # missing octet
            "192.168.1.1.1",  # too many octets
            "192.168.1.01",  # leading zero
            "192.168.1.1a",  # alphabetic character
            "192.168.1.-1",  # negative number
            "10.0.0.a",  # alphabetic character instead of number
            "10.10.10",  # one octet short
            "1234.123.123.123",  # first octet too long
            "0111.123.123.123",  # leading zero in first octet
            "123.045.067.089",  # octets with leading zeros
            "....",  # just dots
            "1...1",  # missing octets
            "a.b.c.d",  # alphabetic instead of numeric
            "192.168.1.1/24",  # CIDR notation
            "192:168:1:1",  # colons instead of dots
            "192.168.1.1 extra text",  # extra text
            " 192.168.1.1",  # leading space
            "192.168.1.1 "  # trailing space
        ]
        for ip in invalid_ips:
            with self.subTest(ip=ip):
                self.assertFalse(check_is_ip(ip))

    def test_edge_cases(self):
        edge_cases = [
            "0.0.0.0",
            "255.255.255.255",
            "1.1.1.1",
            "254.254.254.254",
            "10.0.0.0",
            "172.16.0.0",
            "192.168.0.0"
        ]
        for ip in edge_cases:
            with self.subTest(ip=ip):
                self.assertTrue(check_is_ip(ip))

    def test_get_whois_data(self):
        self.assertIsInstance(get_whois_data("http://example.com"), dict)

    def test_calculate_url_length(self):
        self.assertEqual(calculate_url_length("http://example.com"), 18)

    def test_check_special_char(self):
        self.assertEqual(check_special_char("http://example.com", '@'), 0)
        self.assertEqual(check_special_char("user@example.com", '@'), 1)

    def test_check_redirect(self):
        self.assertEqual(check_redirect("http://example--site.com"), 1)
        self.assertEqual(check_redirect("http://example.com"), 0)

    def test_domain_length(self):
        self.assertEqual(domain_length("example.com"), 11)

    def test_count_subdomains(self):
        self.assertEqual(count_subdomains("test.example.com"), 1)
        self.assertEqual(count_subdomains("example.com"), 0)

    def test_fetch_page_rank(self):
        self.assertEqual(fetch_page_rank("http://example.com"), "N/A")


if __name__ == '__main__':
    unittest.main()
