# Sonam Crumière

I build the systems that go and get that knowledge where it actually lives, from
the people doing the work, and make it usable by everyone else. Right now I do
that at **Schneider Electric**, where I built the analysis tooling for a PhD
project that was drowning in documents. The rest of the time I do it for
companies, through [Peakn8](https://peakn8.com).

## Take one and run it

Clone any of the four below, open a terminal in it, and type:

```bash
claude          # or codex, or whatever you run
> set this up for me
```

Every repo ships an `AGENTS.md`, the convention any coding agent reads. It
installs what is missing, asks you for the one key it cannot invent, and hands
back the single command that starts the thing. No README archaeology, no
half-documented step that only worked on my machine.

---

You know the file exists. You know roughly what it says. But Ctrl+F gives you
nothing, because you're not typing the exact words someone chose two years ago.
**[pdf-rag](https://github.com/scrumier/pdf-rag)** takes the question the way
you'd say it out loud, and comes back with the answer and the document it was
sitting in.

---

Twenty invoices land in the mailbox. Someone opens them one by one, squints at
the total, types it into a spreadsheet, and does it again next week.
**[invoice-processor](https://github.com/scrumier/invoice-processor)** watches a
folder: you drop the PDF in, the line is already filled. Number, date, supplier,
amounts, VAT, IBAN, due date.

---

Nobody read page 34. The contract renewed on its own and you're in for another
year. **[contract-analyzer](https://github.com/scrumier/contract-analyzer)** goes
through the whole stack and hands you the dates, the amounts, the penalties and
the exit terms, with the clauses worth arguing about already flagged.

---

It's the 3rd of the month, you're scrolling 400 lines of expenses, mostly hoping
something jumps out at you. Nothing jumps out.
**[expense-analyzer](https://github.com/scrumier/expense-analyzer)** picks the
odd ones (the duplicate, the round number on a Sunday, the supplier nobody
recognises) and tells you in one sentence why it picked them.

---

These are level one on purpose. They run on your machine, on your key, on a
folder you choose, and you can read every line of them in an afternoon. What I
do for companies starts where these stop: the rules nobody wrote down, the
exceptions that only live in one person's head, and the daily use built on top.

## Proof I can code, security included

**[ft_transcendence](https://github.com/scrumier/ft_transcendence-prod)**
A 3D world you walk around to launch Pong, Tetris and Pacman off working retro
hardware. Team project, 11 months, graded 116/100.

**[cold-wallet](https://github.com/scrumier/cold-wallet)**
Air-gapped crypto wallet in Rust. Signs offline, talks only through QR codes.
The private key never touches a networked machine.

The C and C++ repositories are my 42 Lyon work: a shell, an IRC server, a
raycasting engine, my own libc. They are there because someone always asks
whether I can write things without a framework underneath.

## Stack

Python, C, C++, JavaScript, Rust · LLMs, RAG, embeddings, vector DBs,
scikit-learn · Flask, Django, React, Three.js · Docker, Nginx, PostgreSQL, Redis

## Want it done for you?

[sonam.me](https://sonam.me) · [Peakn8](https://peakn8.com) ·
[LinkedIn](https://www.linkedin.com/in/sonam-crumiere) · bonjour@sonam.me
