# Database Documentation

## Schema: public

### Table: order_items

**Fields:**

- **id**: integer

  Description: Id

- **order_id**: integer

  Description: Order id

- **product_id**: integer

  Description: Product id

- **quantity**: integer

  Description: Quantity

### Table: orders

**Fields:**

- **id**: integer

  Description: Id

- **user_id**: integer

  Description: User id

- **order_date**: timestamp without time zone

  Description: Order date

### Table: payments

**Fields:**

- **id**: integer

  Description: Id

- **order_id**: integer

  Description: Order id

- **amount**: numeric

  Description: Amount

- **payment_date**: timestamp without time zone

  Description: Payment date

### Table: products

**Fields:**

- **id**: integer

  Description: Id

- **name**: character varying

  Description: Name

- **price**: numeric

  Description: Price

### Table: users

**Fields:**

- **id**: integer

  Description: Id

- **name**: character varying

  Description: Name

- **email**: character varying

  Description: Email

