from google.cloud import bigquery

client = bigquery.Client()

query = """
    SELECT corpus AS title, COUNT(word) AS unique_words
    FROM `bigquery-public-data.samples.shakespeare`
    GROUP BY title
    ORDER BY unique_words
    DESC LIMIT 10
"""
results = client.query(query)

for row in results:
    print("There was a result")
    print(row)
