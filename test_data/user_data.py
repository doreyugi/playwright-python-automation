from dataclasses import dataclass

@dataclass
class User:
    username: str
    email: str
    password: str
    DOB_day: str
    DOB_month: str
    DOB_year: str
    first_name: str
    last_name: str
    company: str
    address1: str
    address2: str
    country: str
    state: str
    city: str
    zipcode: str
    mobile_number: str

new_user = User(
    username = "strawberry",
    email = "strawberry@gmail.com",
    password = "strawberry123",
    DOB_day = "5",
    DOB_month = "July",
    DOB_year = "1993",
    first_name = "abc",
    last_name = "def",
    company = "ABC Co.",
    address1 = "362 Celestia",
    address2 = "462 Heavenly Celestia",
    country = "Singapore",
    state = "New York",
    city = "New York",
    zipcode = "70000",
    mobile_number = "70000")

existing_user = User(
    username="banana",
    email="banana@gmail.com",
    password="banana",
    DOB_day="18",
    DOB_month="August",
    DOB_year="1986",
    first_name="ba",
    last_name="na",
    company="fafa",
    address1="235 fafa st",
    address2="365 celestia",
    country="New Zealand",
    state="New York",
    city="New York",
    zipcode="70000",
    mobile_number="70000")