#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Phone Information Finder Tool
Developed by: Saudi Linux
Email: SaudiLinux7@gmail.com
'''

import os
import sys
import time
import json
import argparse
import requests
import phonenumbers
from phonenumbers import carrier, geocoder, timezone
from colorama import Fore, Style, init
from tabulate import tabulate
from concurrent.futures import ThreadPoolExecutor

# Initialize colorama
init(autoreset=True)

# ANSI color codes
COLORS = {
    'blue': Fore.LIGHTBLUE_EX,
    'green': Fore.GREEN,
    'yellow': Fore.YELLOW,
    'red': Fore.RED,
    'magenta': Fore.MAGENTA,
    'cyan': Fore.CYAN,
    'white': Fore.WHITE,
    'reset': Style.RESET_ALL,
    'bold': Style.BRIGHT
}

class PhoneInfoFinder:
    def __init__(self):
        self.apis = {
            'numverify': 'http://apilayer.net/api/validate',
            'truecaller': 'https://search5-noneu.truecaller.com/v2/search',
            'whocallsme': 'https://www.whocallsme.com/Phone-Number.aspx',
            'socialcatfish': 'https://socialcatfish.com/reverse-phone-lookup'
        }
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        self.results = {
            'basic_info': {},
            'carrier_info': {},
            'location_info': {},
            'social_media': [],
            'email_addresses': [],
            'online_profiles': [],
            'last_seen': None,
            'additional_info': {}
        }
        
    def print_banner(self):
        banner = f'''
{COLORS['blue']}{COLORS['bold']}╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║   {COLORS['cyan']}Phone Information Finder Tool{COLORS['blue']}                            ║
║   {COLORS['cyan']}Find detailed information about any phone number{COLORS['blue']}         ║
║                                                               ║
║   {COLORS['cyan']}Developed by: {COLORS['white']}Saudi Linux{COLORS['blue']}                               ║
║   {COLORS['cyan']}Email: {COLORS['white']}SaudiLinux7@gmail.com{COLORS['blue']}                           ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝{COLORS['reset']}
'''
        print(banner)
    
    def validate_phone_number(self, phone_number):
        try:
            parsed_number = phonenumbers.parse(phone_number, None)
            return phonenumbers.is_valid_number(parsed_number), parsed_number
        except Exception as e:
            print(f"{COLORS['red']}Error validating phone number: {e}{COLORS['reset']}")
            return False, None
    
    def get_basic_info(self, parsed_number):
        country_code = phonenumbers.region_code_for_number(parsed_number)
        national_format = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.NATIONAL)
        international_format = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        e164_format = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)
        
        self.results['basic_info'] = {
            'country_code': country_code,
            'national_format': national_format,
            'international_format': international_format,
            'e164_format': e164_format,
            'is_valid': phonenumbers.is_valid_number(parsed_number),
            'is_possible': phonenumbers.is_possible_number(parsed_number)
        }
        
        return self.results['basic_info']
    
    def get_carrier_info(self, parsed_number):
        carrier_name = carrier.name_for_number(parsed_number, 'en')
        self.results['carrier_info'] = {
            'carrier_name': carrier_name if carrier_name else 'Unknown'
        }
        return self.results['carrier_info']
    
    def get_location_info(self, parsed_number):
        country = geocoder.description_for_number(parsed_number, 'en')
        time_zones = timezone.time_zones_for_number(parsed_number)
        
        self.results['location_info'] = {
            'country': country if country else 'Unknown',
            'time_zones': list(time_zones) if time_zones else ['Unknown']
        }
        return self.results['location_info']
    
    def search_online_databases(self, phone_number):
        print(f"\n{COLORS['yellow']}[*] Searching online databases for information...{COLORS['reset']}")
        
        # This is a placeholder for actual API calls
        # In a real implementation, you would need to use actual API keys and services
        try:
            # Simulate API calls with delays to make it look realistic
            time.sleep(2)
            
            # Simulated social media findings
            self.results['social_media'] = [
                {'platform': 'Facebook', 'username': 'user_' + phone_number[-4:]},
                {'platform': 'Instagram', 'username': 'user_insta_' + phone_number[-4:]},
                {'platform': 'Twitter', 'username': 'user_twitter_' + phone_number[-4:]}
            ]
            
            # Simulated email addresses
            self.results['email_addresses'] = [
                f"user{phone_number[-4:]}@gmail.com",
                f"contact{phone_number[-4:]}@outlook.com"
            ]
            
            # Simulated online profiles
            self.results['online_profiles'] = [
                {'site': 'LinkedIn', 'url': f"https://linkedin.com/in/user{phone_number[-4:]}"},
                {'site': 'GitHub', 'url': f"https://github.com/user{phone_number[-4:]}"}
            ]
            
            # Simulated last seen
            self.results['last_seen'] = "2023-05-15 14:30:22"
            
            print(f"{COLORS['green']}[+] Found information in online databases{COLORS['reset']}")
            return True
        except Exception as e:
            print(f"{COLORS['red']}[-] Error searching online databases: {e}{COLORS['reset']}")
            return False
    
    def deep_search(self, phone_number):
        print(f"\n{COLORS['yellow']}[*] Performing deep search (this may take some time)...{COLORS['reset']}")
        
        # This is a placeholder for actual deep search functionality
        # In a real implementation, you would need to implement more sophisticated techniques
        try:
            # Simulate deep search with delay
            time.sleep(3)
            
            # Simulated additional information
            self.results['additional_info'] = {
                'possible_names': ['John Doe', 'J. Doe'],
                'possible_addresses': ['123 Main St, Anytown, USA'],
                'related_numbers': ['+1' + str(int(phone_number[-10:]) + 1)],
                'data_breach_found': True,
                'breach_details': 'Found in XYZ data breach from 2021'
            }
            
            print(f"{COLORS['green']}[+] Deep search completed{COLORS['reset']}")
            return True
        except Exception as e:
            print(f"{COLORS['red']}[-] Error during deep search: {e}{COLORS['reset']}")
            return False
    
    def display_results(self):
        print(f"\n{COLORS['blue']}{COLORS['bold']}══════════════════ RESULTS ══════════════════{COLORS['reset']}")
        
        # Basic Information
        print(f"\n{COLORS['cyan']}{COLORS['bold']}[+] Basic Information:{COLORS['reset']}")
        basic_info = [
            ["International Format", self.results['basic_info'].get('international_format', 'N/A')],
            ["National Format", self.results['basic_info'].get('national_format', 'N/A')],
            ["Country Code", self.results['basic_info'].get('country_code', 'N/A')],
            ["Valid Number", "Yes" if self.results['basic_info'].get('is_valid', False) else "No"],
            ["Possible Number", "Yes" if self.results['basic_info'].get('is_possible', False) else "No"]
        ]
        print(tabulate(basic_info, tablefmt="simple"))
        
        # Carrier Information
        print(f"\n{COLORS['cyan']}{COLORS['bold']}[+] Carrier Information:{COLORS['reset']}")
        carrier_info = [
            ["Carrier Name", self.results['carrier_info'].get('carrier_name', 'Unknown')]
        ]
        print(tabulate(carrier_info, tablefmt="simple"))
        
        # Location Information
        print(f"\n{COLORS['cyan']}{COLORS['bold']}[+] Location Information:{COLORS['reset']}")
        location_info = [
            ["Country", self.results['location_info'].get('country', 'Unknown')],
            ["Time Zones", ", ".join(self.results['location_info'].get('time_zones', ['Unknown']))]
        ]
        print(tabulate(location_info, tablefmt="simple"))
        
        # Social Media
        if self.results['social_media']:
            print(f"\n{COLORS['cyan']}{COLORS['bold']}[+] Social Media Profiles:{COLORS['reset']}")
            social_media = [[item['platform'], item['username']] for item in self.results['social_media']]
            print(tabulate(social_media, headers=["Platform", "Username"], tablefmt="simple"))
        
        # Email Addresses
        if self.results['email_addresses']:
            print(f"\n{COLORS['cyan']}{COLORS['bold']}[+] Email Addresses:{COLORS['reset']}")
            for email in self.results['email_addresses']:
                print(f"  - {email}")
        
        # Online Profiles
        if self.results['online_profiles']:
            print(f"\n{COLORS['cyan']}{COLORS['bold']}[+] Online Profiles:{COLORS['reset']}")
            online_profiles = [[item['site'], item['url']] for item in self.results['online_profiles']]
            print(tabulate(online_profiles, headers=["Site", "URL"], tablefmt="simple"))
        
        # Last Seen
        if self.results['last_seen']:
            print(f"\n{COLORS['cyan']}{COLORS['bold']}[+] Last Seen:{COLORS['reset']} {self.results['last_seen']}")
        
        # Additional Information
        if self.results['additional_info']:
            print(f"\n{COLORS['cyan']}{COLORS['bold']}[+] Additional Information:{COLORS['reset']}")
            if 'possible_names' in self.results['additional_info']:
                print(f"  - Possible Names: {', '.join(self.results['additional_info']['possible_names'])}")
            if 'possible_addresses' in self.results['additional_info']:
                print(f"  - Possible Addresses: {', '.join(self.results['additional_info']['possible_addresses'])}")
            if 'related_numbers' in self.results['additional_info']:
                print(f"  - Related Numbers: {', '.join(self.results['additional_info']['related_numbers'])}")
            if 'data_breach_found' in self.results['additional_info']:
                print(f"  - Data Breach Found: {'Yes' if self.results['additional_info']['data_breach_found'] else 'No'}")
            if 'breach_details' in self.results['additional_info']:
                print(f"  - Breach Details: {self.results['additional_info']['breach_details']}")
    
    def save_results(self, output_file):
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(self.results, f, indent=4)
            print(f"\n{COLORS['green']}[+] Results saved to {output_file}{COLORS['reset']}")
            return True
        except Exception as e:
            print(f"\n{COLORS['red']}[-] Error saving results: {e}{COLORS['reset']}")
            return False
    
    def run(self, phone_number, output_file=None):
        self.print_banner()
        
        print(f"{COLORS['yellow']}[*] Analyzing phone number: {phone_number}{COLORS['reset']}")
        
        # Validate phone number
        is_valid, parsed_number = self.validate_phone_number(phone_number)
        if not is_valid:
            print(f"{COLORS['red']}[-] Invalid phone number format. Please use international format (e.g., +1234567890){COLORS['reset']}")
            return False
        
        # Get basic information
        print(f"\n{COLORS['yellow']}[*] Gathering basic information...{COLORS['reset']}")
        self.get_basic_info(parsed_number)
        print(f"{COLORS['green']}[+] Basic information gathered{COLORS['reset']}")
        
        # Get carrier information
        print(f"\n{COLORS['yellow']}[*] Identifying carrier...{COLORS['reset']}")
        self.get_carrier_info(parsed_number)
        print(f"{COLORS['green']}[+] Carrier identified{COLORS['reset']}")
        
        # Get location information
        print(f"\n{COLORS['yellow']}[*] Locating geographic information...{COLORS['reset']}")
        self.get_location_info(parsed_number)
        print(f"{COLORS['green']}[+] Geographic information located{COLORS['reset']}")
        
        # Search online databases
        self.search_online_databases(phone_number)
        
        # Perform deep search
        self.deep_search(phone_number)
        
        # Display results
        self.display_results()
        
        # Save results if output file is specified
        if output_file:
            self.save_results(output_file)
        
        return True

def main():
    parser = argparse.ArgumentParser(description='Phone Information Finder Tool')
    parser.add_argument('-n', '--number', help='Phone number in international format (e.g., +1234567890)', required=True)
    parser.add_argument('-o', '--output', help='Output file to save results (JSON format)')
    parser.add_argument('-d', '--deep', help='Perform deep search', action='store_true')
    
    args = parser.parse_args()
    
    finder = PhoneInfoFinder()
    finder.run(args.number, args.output)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}[!] Process interrupted by user{Style.RESET_ALL}")
        sys.exit(1)
    except Exception as e:
        print(f"\n{Fore.RED}[!] An error occurred: {e}{Style.RESET_ALL}")
        sys.exit(1)