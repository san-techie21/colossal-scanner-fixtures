import sqlite3

from openai import OpenAI

client = OpenAI()
conn = sqlite3.connect("analytics.db")


def answer(question: str):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": "Name the sales region the question is about."},
                  {"role": "user", "content": question}],
    )
    region = completion.choices[0].message.content.strip()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sales WHERE region = ?", (region,))
    return cursor.fetchall()
