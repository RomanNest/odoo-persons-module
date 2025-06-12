# Odoo-persons-module

## Description

This module implements a **Persons catalog** for Odoo 16. It was created as a test task for the **Odoo Fullstack Developer** position and includes both backend and frontend functionality.

The module depends on the `website` module.

---

## 🔧 Features

### 1. Backend

- A new model `persons.person` with the following fields:
  - `first_name` (required)
  - `last_name` (required)
  - `full_name` (computed)
  - `birthday`
  - `age` (computed)
  - `sex` (male, female, non-binary)
  - `company_id` (required, defaults to the current user's company)

### 2. Frontend (Website)

- The `/persons` page displays the 5 most recent records from the model as cards.
- Each card includes:
  - Full name
  - Gender (if specified)
  - Age
  - Company name

### 3. Web Form

- Available at `/persons/new`
- Allows the public to create a new record through a website form

---

## 📁 Module Structure

```
persons/
├── __init__.py
├── __manifest__.py
├── controllers/
│   ├── __init__.py
│   └── website_persons.py
├── models/
│   ├── __init__.py
│   └── person.py
├── templates/
│   ├── persons_template.xml
│   └── persons_form_template.xml
├── views/
│   ├── persons_views.xml
│   └── persons_menu.xml
```

---

## ⚙️ Installation

1. Copy the module to your custom addons directory.

2. Make sure your `odoo.conf` file includes the path to that directory:

3. Start Odoo with module update:
   ```bash
   python odoo-bin -c odoo.conf -u persons
   ```

4. Open the backend and check: **Website > Persons**

5. Visit the website page: [http://localhost:8069/persons](http://localhost:8069/persons)
---
