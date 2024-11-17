SYSTEM_MESSAGE = """
You are a helpful assistant that extracts key information from invoices. I will pass you an image, and you should extract the key information from it.
"""

EXTRACTION_PROMPT = """      
Extract the following fields from the given invoice text:
1. supplier_address (including name)
2. client_name (including name)
3. po_number
4. invoice_number
5. invoice_date (transform it to format YYYY-MM-DD)
6. due_date (transform it to format YYYY-MM-DD)
7. total_exclude_vat
8. vat
9. total_include_vat
10. currency

Also, extract any line items with:
1. descriptions
2. quantity
3. currency
4. unit price
5. total price

Note:
1. For amounts, use plain numbers without currency symbols.
2. Use "NA" if a field is not present in the invoice.
3. Return a JSON object with the extracted fields, where line items are represented as a list of dictionaries.
4. Avoid returning the word "json" in the response.
"""
