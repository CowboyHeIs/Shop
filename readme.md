Questions :
1. Explain why we need data delivery in implementing a platform.
2. In your opinion, which is better, XML or JSON? Why is JSON more popular than XML?
3. Explain the functional usage of `is_valid()` method in Django forms. Also explain why we need the method in forms.
4. Why do we need `csrf_token` when creating a form in Django? What could happen if we did not use `csrf_token` on a Django form? How could this be leveraged by an attacker?
5. Explain how you implemented the checklist above step-by-step (not just following the tutorial).

Answers :
1. Ensures accuracy and efficiency on data transfer between systems.
2. JSON
-- Simple
-- Smaller
-- Faster parsing
3. Ensures data integrity and error handling by validating form data.
4. Prevents attackers that exploit from submissions by verifying requests.
5. 
-- Added id in `Products.csv`
-- Added `ProductForm` in `main/forms.py`
-- Added `add_product`, `all_objects_xml`, `all_objects_json`, `object_by_id_xml`, `object_by_id_json` views
-- Updated `main/urls.py`
-- Due to warning message, consulted with my uncle, thus added `static` directory.
-- Added `add_product.html`

## Screenshots

### SC JSON
![JSON ID:ALL](sc_json)

### SC XML
![XML ID:ALL](sc_xml)

### SC XML 001
![XML ID:001](sc_xml_001)

### SC JSON 101
![JSON ID:101](sc_json_101)
