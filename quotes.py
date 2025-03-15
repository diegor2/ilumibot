import wikiquote
import json

authors = ["John Locke", "David Hume",
           "Adam Smith", "Immanuel Kant", "Voltaire"]

database = []
for author in authors:
    quotes = wikiquote.quotes(author, lang='pt')
    database += [
        {
            "author": author,
            "quote": quote
        }

        for quote in quotes
    ]

with open('database.json', 'w', encoding='utf8') as f:
    json.dump({'database': database}, f, ensure_ascii=False, indent=2)
