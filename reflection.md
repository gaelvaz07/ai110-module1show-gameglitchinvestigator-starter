# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|  Guess of 2   | No points, not the right guess |  Rewards you for a wrong guess on even numbers | No Console error |

|  Guess of 30   | Hint says "Too Low! Guess Higher" | Hint is mistaken and says "Too High! Guess Lower" | No Console error |
 
| Change difficulty to hard  | Game is supposed to show a higher range of answer possibilites  | The range of possible answers shortens, making the game easier instead of harder | No Console error |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

For the tools that I used, I utilized GeminiPRO and Claude

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

Initially I asked Claude how to fix the backwards hints bug in app.py. It correctly identified that "Go HIGHER!" and "Go LOWER!" were swapped in the check_guess function. I verified this was correct by reading the code myself and confirming that when guess > secret, the player should go lower and not higher

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

When I asked Gemini "How do I keep a variable from resetting in Streamlit when I click a button?" I tried this and the AI gave a general explanation about st.session_state, but it didn't point me directly to the specific bug in my code, the line where secret was being converted to a string on even attempts. I had to go back and read the code carefully myself to find the real issue

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
