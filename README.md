## **ZohoBooks Python Client Library**
=========================================
The python library for integrating with ZohoBooks. It is the python wrapper for Zoho Books Api.

## Installation
---------------
Download `books` from repository and add those files to your project.

## Documentation
----------------
The documentation for using Zoho Books API is given [here](https://www.zoho.com/books/api/v3/)

## Usage
--------
If you want to use all our Zoho books services API you should have a valid Zoho username, password and a valid authtoken.

How to generate your authtoken? [Refer Here](https://www.zoho.com/books/api/v3/) 

### How to access ZohoBooks Api through python wrapper classes?
------------------------------------------------------------------ 

Here is a sample example code for accessing Zoho Books API through Python wrapper class.

You have to import these classes:

        from books.model.Organization import Organization
        from books.model.Address import Address
        from books.api.OrganizationsApi import OrganizationsApi
        from books.service.ZohoBooks import ZohoBooks
		
There are two ways to create an instance for OrganizationsAPI

 - Create an instance for organizations API by passing authtoken and organization id:

        organizations_api = OrganizationsApi({"authtoken"}, {"organization_id"})
			
 - Create an instance for ZohoBooks by passing authtoken and organization id and get the instance for Organizations api.
     
        zoho_books = ZohoBooks({"authtoken"}, {"organization_id"})

        organizations_api = zoho_books.get_organizations_api()
			
			
#### **Get the list of organizations:**
			
To get list of organizations you need to call the get_organizations() method.

        print organizations_api.get_organizations()

#### **Get details of an organization**
    
        print organizations_api.get({"organization_id"})

#### **Create an organization**
        
        organization = Organization()
        organization.set_name("Jony and co")

        address = Address()
        address.set_street_address1("2/65")
        address.set_street_address2("vignesh plaza")
        address.set_city("MDU")
        address.set_state("TN")
        address.set_country("India")
        address.set_zip("322")
        organization.set_address(address)

        organization.set_industry_type("")
        organization.set_industry_size("")
        organization.set_fiscal_year_start_month("january")
        organization.set_currency_code("USD")
        organization.set_time_zone("Asia/Calcutta")
        organization.set_date_format("dd MMM yyyy")
        organization.set_field_separator("")
        organization.set_language_code("en")
        organization.set_tax_basis("accrual")
        organization.set_tax_type("tax")
        organization.set_org_address("")
        organization.set_remit_to_address("")
        print organizations_api.create(organization)

#### **Update an existing Organization**
 
        organization = Organization()
        organization.set_name("Jony and co")

        address = Address()
        address.set_street_address1("2/65")
        address.set_street_address2("vignesh plaza")
        address.set_city("MDU")
        address.set_state("TN")
        address.set_country("India")
        address.set_zip("322")

        organization.set_address(address)
        organization.set_industry_type("")
        organization.set_industry_size("")
        organization.set_fiscal_year_start_month("january")
        organization.set_currency_code("INR")
        organization.set_time_zone("Asia/Calcutta")
        organization.set_date_format("dd MMM yyyy")
        organization.set_field_separator("")
        organization.set_language_code("en")
        organization.set_tax_basis("accrual")
        organization.set_tax_type("tax")
        organization.set_org_address("")
        organization.set_remit_to_address("")
        print organizations_api.update(organization_id, organization)

#### **Get the parameters of an organization**

        organization = organizations_api.get({"organization_id"})
        currency_code = organization.get_currency_code()
        organization_address = organization.get_address()
        organization_name = organization.get_name()

#### **Exception Handling**

If there is any error while calling Zoho Books API then `BooksException` will be thrown. So `try` and `exception` statements must be included in your classes.

        try:
            organization = organizations_api.get({"organization_id"})
        except BooksException as b_e:
            print "Error Code:" + b_e.get_code() + "\nError Message:" + b_e.get_message()

See [Here](../../tree/master/test) for full examples.
      

