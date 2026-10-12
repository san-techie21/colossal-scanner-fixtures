import sqlite3

from openai import OpenAI

client = OpenAI()
conn = sqlite3.connect("analytics.db")


def answer(question: str):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": "Translate the question into one SQL WHERE clause."},
                  {"role": "user", "content": question}],
    )
    where = completion.choices[0].message.content
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM sales WHERE {where}")
    return cursor.fetchall()
