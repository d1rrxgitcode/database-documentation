# Database Documentation

## Schema public

--------------------------------------------------

### Table order_items

**Fields:**

- **id** (integer)

  Primary key identifier.

- **order_id** (integer)

  Reference to Order table.

- **product_id** (integer)

  Reference to Product table.

- **quantity** (integer)

  The quantity of the order_item.

--------------------------------------------------

### Table orders

**Fields:**

- **id** (integer)

  Primary key identifier.

- **user_id** (integer)

  Reference to User table.

- **order_date** (timestamp without time zone)

  Order date.

--------------------------------------------------

### Table payments

**Fields:**

- **id** (integer)

  Primary key identifier.

- **order_id** (integer)

  Reference to Order table.

- **amount** (numeric)

  The amount of the payment.

- **payment_date** (timestamp without time zone)

  Payment date.

--------------------------------------------------

### Table products

**Fields:**

- **id** (integer)

  Primary key identifier.

- **name** (character varying)

  Product name.

- **price** (numeric)

  The price of the product.

--------------------------------------------------

### Table users

**Fields:**

- **id** (integer)

  Primary key identifier.

- **name** (character varying)

  User name.

- **email** (character varying)

  Email address.

--------------------------------------------------
