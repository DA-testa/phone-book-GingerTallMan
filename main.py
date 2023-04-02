# python3
# 221RDB254 Artūrs Adrians Zaharovs - Ploriņš 6. grupa
class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    if not 1 <= n <= 10**5:
        raise ValueError("Invalid number of queries")
    queries = []
    for i in range(n):
        query = input().strip().split()
        if query[0] not in ['add', 'del', 'find']:
            raise ValueError("Invalid query type")
        if not 1 <= len(query[1]) <= 7 or not query[1].isdigit():
            raise ValueError("Invalid phone number")
        if query[0] == 'add' and not 1 <= len(query[2]) <= 15:
            raise ValueError("Invalid name")
        queries.append(Query(query))
    return queries

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    # Use a dictionary to store the phone numbers and names
    contacts = {}
    for cur_query in queries:
        if cur_query.type == 'add':
            # Add or update the contact
            contacts[cur_query.number] = cur_query.name
        elif cur_query.type == 'del':
            # Remove the contact if it exists
            contacts.pop(cur_query.number, None)
        else:
            # Find the name for the given number or return "not found"
            response = contacts.get(cur_query.number, "not found")
            result.append(response)
    return result

if __name__ == '__main__':
    try:
        queries = read_queries()
        result = process_queries(queries)
        write_responses(result)
    except Exception as e:
        print("Error:", e)
