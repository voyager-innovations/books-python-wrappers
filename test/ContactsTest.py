#$Id$#

import requests

from books.model.Contact import Contact
from books.model.Email import Email
from books.model.Address import Address
from books.model.ContactPerson import ContactPerson
from books.service.ZohoBooks import ZohoBooks

zoho_books = ZohoBooks("1202c2fa92ed3b23db3f93c84e21624d", "317312245")
# To get the auth token programmatically, use:
# https://accounts.zoho.com/apiauthtoken/nb/create?SCOPE=ZohoBooks/booksapi&EMAIL_ID=[ZohoID/EmailID]&PASSWORD=[Password]
#
# To get the organization id programmatically, use:
# https://books.zoho.com/api/v3/organizations?authtoken=[AUTHTOKEN]


contact_api = zoho_books.get_contacts_api()

# to get a contact from contacts list
first_contact = contact_api.get_contacts().get_contacts()[0]
print("contact_id = ", first_contact.contact_id)
print("contact_name = ", first_contact.contact_name)
# to list contacts

#parameter = {'sort_column':'last_name'}
#contact_api.get_contacts(parameter)

# to get a contact

test_contact = contact_api.get(first_contact.contact_id)
print("get contact using id = '"  + first_contact.contact_id + "' : " + test_contact.contact_id + " | " + test_contact.contact_name)


# to create contact

contact = Contact()
contact.set_company_name('Wayne Enterprises')
contact.set_contact_name('Bruce Wayne')
contact.set_email('batman@wayneent.com')
contact.set_payment_terms(15)
contact.set_payment_terms_label('Net 15')
contact.set_currency_id("276200000000044013")
contact.set_notes('thank you')
con_per = []
cp = ContactPerson()
cp.set_first_name('nivetha')
cp.set_salutation('ms')

con_per.append(cp)

v = ContactPerson()
v.set_first_name('varunaa')
v.set_salutation('mr')
v.set_is_primary_contact(True)
con_per.append(v)

#contact.set_contact_persons(con_per)

baddress = Address()
baddress.set_address('45, suite street')
baddress.set_city('California')
baddress.set_state('CA')
baddress.set_zip('9876')
baddress.set_fax('+1-925-924-9600')
#contact.set_billing_address(baddress)

saddress = Address()
saddress.set_address('45, suite street')
saddress.set_city('California')
saddress.set_state('CA')
saddress.set_zip('9876')
saddress.set_fax('+1-925-924-9600')
contact.set_shipping_address(saddress)

contact.set_notes('Payment option: Through check' )

new_contact = contact_api.create(contact)

print("company name:",new_contact.company_name)
print("contact id:",new_contact.contact_id)
contact_id = new_contact.contact_id

# to update a contact

contact = Contact()
contact.set_contact_name('New Name')
contact.set_payment_terms(15)
contact.set_payment_terms_label('Net 15')
contact.set_currency_id(276200000000044013)

con_per = []
cp = ContactPerson()
cp.set_first_name('nivetha')
cp.set_salutation('ms')

con_per.append(cp)

v = ContactPerson()
v.set_first_name('varun')
v.set_salutation('mr')
v.set_is_primary_contact(True)
con_per.append(v)

#contact.set_contact_persons(con_per)


baddress = Address()
baddress.set_address('Beverly Hills')
baddress.set_city('California')
baddress.set_state('CA')
baddress.set_zip('9876')
baddress.set_fax('+1-925-924-9600')
contact.set_billing_address(baddress)

saddress = Address()
saddress.set_address('45, suite street')
saddress.set_city('California')
saddress.set_state('CA')
saddress.set_zip('9876')
saddress.set_fax('+1-925-924-9600')
contact.set_shipping_address(saddress)

contact.set_notes('Payment option : Through check' )

print(contact_api.update(contact_id, contact));
print("company name:",new_contact.company_name)

# to delete a contact

print(contact_api.delete(contact_id))
