import anthropic

client = anthropic.Anthropic()


def answer(question: str, store) -> str:
    docs = store.similarity_search(question, k=3)
    context = "\n".join(d.page_content for d in docs)
    reply = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=600,
        system=f"You are the policy assistant. Reference material:\n{context}",
        messages=[{"role": "user", "content": question}],
    )
    return reply.content[0].text
