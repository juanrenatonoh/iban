from pydantic import BaseModel

'''
Represents the IbanRegistry
'''
class Registry(BaseModel):
    name_of_country: str | None = None
    iban_prefix_country_code_iso: str | None = None
    country_code_includes_other_countries_territories: str | None = None
    sepa_country: str | None = None
    sepa_country_also_includes: str | None = None
    domestic_account_number_example: str | None = None
    bban: str | None = None
    bban_structure: str | None = None
    bban_length: str | None = None
    bank_identifier_position_within_the_bban: str | None = None
    bank_identifier_pattern: str | None = None
    branch_identifier_position_within_the_bban: str | None = None
    branch_identifier_pattern: str | None = None
    bank_identifier_example: str | None = None
    branch_identifier_example: str | None = None
    bban_example: str | None = None
    iban: str | None = None
    iban_structure: str | None = None
    iban_length: str | None = None
    effective_date: str | None = None
    iban_electronic_format_example: str | None = None
    iban_print_format_example: str | None = None
    contact_details: str | None = None
    organisation: str | None = None
    department: str | None = None
    street_address: str | None = None
    city_postcode: str | None = None
    department_generic_email: str | None = None
    department_tel: str | None = None
    primary_contact: str | None = None
    name: str | None = None
    first_name: str | None = None
    title: str | None = None
    email: str | None = None
    tel: str | None = None
    secondary_contact: str | None = None
    name_2: str | None = None
    first_name_2: str | None = None
    title_2: str | None = None
    email_2: str | None = None
    tel_2: str | None = None
    updates: str | None = None
    last_update_date: str | None = None
