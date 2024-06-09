import csv

def csv_to_sql_insert(csv_file_path, table_name, output_file_path):
    with open(csv_file_path, mode='r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        columns = next(csv_reader)  # Get column names from the first row
        insert_statements = []
        
        for row in csv_reader:
            values = [f"'{value}'" if value else 'NULL' for value in row]
            columns_str = ', '.join(columns)
            values_str = ', '.join(values)
            insert_statement = f"INSERT INTO {table_name} ({columns_str}) VALUES ({values_str});"
            insert_statements.append(insert_statement)
    
    with open(output_file_path, mode='w', encoding='utf-8') as output_file:
        for statement in insert_statements:
            output_file.write(statement + '\n')

csv_file_path = '/Users/joshuasegal/Coding/cs3200materials/political-profit-bros/app/src/assets/python/cleanedbilldata.csv'
table_name = 'legislation_mega'
output_file_path = '/Users/joshuasegal/Coding/cs3200materials/political-profit-bros/database/04_legislation.sql'
csv_to_sql_insert(csv_file_path, table_name, output_file_path)

print(f"SQL INSERT statements have been written to {output_file_path}")
