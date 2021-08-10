
def read_queries():
    n = int(input())
    return [input().split() for _ in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process(queries):
    result = []
    contacts = [0 for _ in range(10**7)]
    for q in queries:
        if q[0] == 'add':
            contacts[int(q[1])] = q[2]
        elif q[0] == 'del':
            contacts[int(q[1])] = 0
        else:
            if contacts[int(q[1])]:
                result.append(contacts[int(q[1])])
            else:
                result.append('not found')
    return result

if __name__ == "__main__":
    write_responses(process(read_queries()))
