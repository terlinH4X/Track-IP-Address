# Track IP Address

This program helps to track the location of IP addresses. It can be helpful for both security purposes or just for general knowledge. When you enter an IP address into the program, it will use an API to find the location of the IP address and provide that information as output.

![Author: TERLIN](https://img.shields.io/badge/Author-TERLIN-blue)
![Developed with: Python](https://img.shields.io/badge/Developed%20with-Python-orange)

---

## Prerequisites

Before using the code, you need to ensure that you have the following packages installed:

- `requests`
- `colorama`

---

## Usage

- git clone [https://github.com/KES-TRA/Track-IP-Address.git]("https://github.com/KES-TRA/Track-IP-Address.git")
- `cd Track-IP-Addres`
- `pip install -r requirements.txt`
- `python main.py`

---

## Result

```json
{
 "ip": "8.8.8.8",
 "city": "Mountain View",
 "region": "California",
 "region_code": "CA",
 "country": "US",
 "country_name": "United States",
 "continent_code": "NA",
 "in_eu": false,
 "postal": "94035",
 "latitude": 37.386,
 "longitude": -122.0838,
 "timezone": "America/Los_Angeles",
 "utc_offset": "-0700",
 "country_calling_code": "+1",
 "currency": "USD",
 "languages": "en-US,es-US,haw,fr",
 "asn": "AS15169",
 "org": "Google LLC",
 "postal_confidence": 100,
 "hostname": "dns.google",
 "anycast": true,
 "security": {
  "is_proxy": false,
  "proxy_type": null,
  "is_crawler": false,
  "crawler_name": null,
  "crawler_type": null,
  "is_tor": false,
  "threat_level": "low",
  "threat_types": null
 }
} 
```
