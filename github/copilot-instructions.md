# CONTEXT FILE:
# Context for Copilot

## Who we are
We're a pair of design students in HCDE 310, learning Python and Flask.

## How we work with AI (Stage 4: spec first)
- Don't write specs or checks for us. Before writing code, ask us for what it should do, its inputs and outputs, and 2 or 3 checks, then wait for our answer. After we write them, you may point out what's missing.
- Build in small pieces. Before you change files, tell us which ones. Don't commit.

## How we like to work
Create code only in small pieces, one function at a time based off our written specs and checks. Then, explain to us line by line what you did and why, keeping in mind we are still new to learning Python and Flask. If we give a specific line and ask for help, explain that line and other lines that are relevant to it. 

## Our project
Who it's for:
Our project is for young-adult music lovers who are comfortable with interacting with digital technology, and are trying to get back into reading but need motivation. 

What they're trying to do:
Users of our project would be trying to get their listening history analyzed through AI in order to learn a bit more about themselves through their "music vibes" and get poems tailored to their current music taste. 

APIs and their limits:
Our project would use Last.Fm's API to get the user's listening history and PoetryDB's API to get poems.

It's important to note that while Last.Fm's API does not have an exact number listed, it will not allow continous exessive calls or multiple calls per second. One must also use a User-Agent header on all requests, and a key is required for use of Last.Fm

PoetryDB's API has no stated limits, no API key, and no header needed. However, it does require crediting PoetryDB whenever their data is displayed. Semicolons (;) are used to separate multiple terms, so they cannot be used in search terms. Also 'poemcount' cannot be combined with 'random'.

## Not decided yet
(List what's still open.) AS of 11/21/26 1:30 am
To be updated after P2 Completion:
- AI API
- Refined Main user flow
- Data Model
- Tech Plan
- User Testers
- Success Criteria
- Priorities & Risks

## Wrap up
When we say "wrap up": add an entry to ai_use.md with the date and the files and functions you wrote or changed, one line each, starting with "AI draft: check me." Leave "Reflection:" blank. Suggest a commit message. Don't commit until we say yes.
