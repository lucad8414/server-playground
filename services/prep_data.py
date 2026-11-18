import sqlite3
from database_columns import Database_Types

# We get a file where the first line denotes the name of the table, also has a corresponding data base table name.
# the second row contains all the column names.
# then data begins.
# What we need to do with the data is: check if all dates are in the correct format, if all entries are properly separated and convert all prices to floats.

# ----------------------------------------------------------------------------

def check_date(date: str) -> bool:
    return len(date) != 8 or (date[:2].isnumeric() and date[2] == "." and date[3:5].isnumeric() and date[5] == "." and date[6:8].isnumeric()) or int(date[:2]) <= 31 or 1 <= int(date[3:5]) <= 12 or int(date[6:8]) >= 26

# ----------------------------------------------------------------------------

def check_initial(person: str) -> str:
    if person.lower() == "l" or person.lower() == "luca":
        return "Luca"

    if person.lower() == "m" or person.lower() == "minna":
        return "Minna"

    return ""

# ----------------------------------------------------------------------------

def format_price(price: str) -> float:
    # Delete €
    new_price = price[:-1]

    # exchange german coma to english dot for simple float conversion    
    formatted = new_price.replace(",", ".")

    return float(formatted)

# ----------------------------------------------------------------------------

def check_price(price: str) -> bool:
    return price[-1] == "€" or price[:-1].isnumeric() or price[:-1].replace(",","").isnumeric()

# ----------------------------------------------------------------------------

def check_name(name: str) -> bool:
    return True

# ----------------------------------------------------------------------------

def check_cycle(cycle: str) -> bool:
    return cycle.lower() == "semester" or cycle.lower == "monat" or cycle.lower() == "jahr" or cycle.lower() == "woche" or cycle.lower() == "viertel"
        
# ----------------------------------------------------------------------------

def embed_into_db(path: str, filename: str, table_name: str,  starting_line: int = 2, separator: str = "\t"):

    DATABASE_PATH = "../data/household.db"
    with open(path + filename, "r") as data:
        lines = data.readlines()

        con = sqlite3.connect(DATABASE_PATH)
        cur = con.cursor()
        
        # Check if wanted table is there
        tables = cur.execute("SELECT name FROM sqlite_master")
        if not table_name in tables.fetchone():
            raise ValueError(f"No table {table_name} exists in the database!")

        # go through all the new data
        starting_line = 2
        for row, line in enumerate(lines[starting_line:]):
            # random blank line in the table does not need to be processed
            if len(line) <= 2:
                continue
            
            # This is a string separated by /t and ending with /n, so first remove the /n and split by tabs
            line = line[:-1]

            # split by tabs
            data_line = line.split(separator)

            assert len(data_line) == 3
            
            # now in this case 0 is type, 1 is date and 2 is price
            current_type = data_line[0]
            current_date = data_line[1]
            current_price = data_line[2]

            assert check_date(current_date)
            price = format_price(current_price)

            current_id = hash(current_type + current_date + str(price))
            source_file = filename
            source_row = row + starting_line
            query = f"""
            INSERT INTO {table_name}
            VALUES (?, ?, ?, ?, ?, ?)
            """

            cur.execute(query, (
            current_id,
            source_file,
            source_row,
            current_type,
            current_date,
            price
            ))

        con.commit()
        con.close()

# ----------------------------------------------------------------------------

if __name__ == "__main__":
    pass

            
