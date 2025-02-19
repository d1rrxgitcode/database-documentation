import time

import markdown

from settings.db_connect import conn
from ai_generator import setup_local_ai, generate_ai_description


model = setup_local_ai()

query = """
    SELECT 
        c.table_schema,
        c.table_name, 
        c.column_name, 
        c.data_type, 
        pgd.description
    FROM 
        information_schema.columns c
    LEFT JOIN 
        pg_catalog.pg_statio_all_tables st ON c.table_schema = st.schemaname AND c.table_name = st.relname
    LEFT JOIN 
        pg_catalog.pg_description pgd ON pgd.objoid = st.relid AND pgd.objsubid = c.ordinal_position
    WHERE 
        c.table_schema NOT IN ('pg_catalog', 'information_schema')
    ORDER BY 
        c.table_schema, c.table_name, c.ordinal_position;
"""

cursor = conn.cursor()
cursor.execute(query)
columns = cursor.fetchall()

md_content = "# Database Documentation\n\n"
current_schema = None
current_table = None

for schema, table, column, data_type, comment in columns:
    if not comment:
        comment = generate_ai_description(model, table, column, data_type)
        time.sleep(0.1)
    
    if current_schema != schema:
        current_schema = schema
        if current_table is not None:
            md_content += "-" * 50 + "\n\n"
        md_content += f"## Schema {schema}\n\n"
    
    if current_table != table:
        current_table = table
        if current_table is not None and schema == current_schema:
            md_content += "-" * 50 + "\n\n"
        md_content += f"### Table {table}\n\n"
        md_content += "**Fields:**\n\n"
    
    md_content += f"- **{column}** | {data_type}\n\n"
    md_content += f"  Description: {comment}\n\n"

md_content += "-" * 50 + "\n"

with open("example.md", "w", encoding="utf-8") as file:
    file.write(md_content)

print("Documentation generated: example.md")

cursor.close()
conn.close()