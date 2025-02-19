# Database Documentation

## Schema public

--------------------------------------------------

### Table order_items

**Fields:**

- **id** | integer

  Description: Primary key identifier.

- **order_id** | integer

  Description: Reference to Order table.

- **product_id** | integer

  Description: Reference to Product table.

- **quantity** | integer

  Description: The quantity of the order_item.

--------------------------------------------------

### Table orders

**Fields:**

- **id** | integer

  Description: Primary key identifier.

- **user_id** | integer

  Description: Reference to User table.

- **order_date** | timestamp without time zone

  Description: Order date.

--------------------------------------------------

### Table payments

**Fields:**

- **id** | integer

  Description: Primary key identifier.

- **order_id** | integer

  Description: Reference to Order table.

- **amount** | numeric

  Description: The amount of the payment.

- **payment_date** | timestamp without time zone

  Description: Payment date.

--------------------------------------------------

### Table products

**Fields:**

- **id** | integer

  Description: Primary key identifier.

- **name** | character varying

  Description: Product name.

- **price** | numeric

  Description: The price of the product.

--------------------------------------------------

### Table users

**Fields:**

- **id** | integer

  Description: Primary key identifier.

- **name** | character varying

  Description: User name.

- **email** | character varying

  Description: Email address.

--------------------------------------------------
