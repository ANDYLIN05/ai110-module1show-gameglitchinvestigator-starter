# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
A: The UI of the game looked fine at first. But after I continued between each mode I realized the easy mode gave you less attempts than the normal one. Also when playing the game itself the hints were not helping when you got closer to the secret number. 
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
A: Beside the two bugs I mention above there was a problem with toggling the hint button. Once you start toggling the "Show hint" the hint would not come back unless you restart the entire game. In addition the "New Game" button does not work. 

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
A: I used Copilot and Claude Code.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
A: The AI agreed with me that the "New Game" button needed to be fixed and gave me a solution to fix it. The Solution worked. 
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
A: When I was fixing the Type Comparison Error the AI was oversaw the fact that the hint messages were swap. As a result I had to switch them myself. 

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
A: I looked over the tests cases first. Then I checked if that test case would fail or pass depending on my app.py. After that I ran pytest.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
A: I ran the "test_negative_numbers" which would test what the hint would output if the user guess a negative number. This is passed because I looked in the "check_guess" function where the if condition would output the correct message. 
- Did AI help you design or understand any tests? How?
A: Yes AI help come up with many different testes. I had to make sure if those testes were helpful for me or not. 

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
A: The secret number did not change with the original app instead the problem was a state issue when the user started a new game state. The "New Game" button would never changed the state of the game and therefore the secret number would not have change. 
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
A: Streamlit reruns the entire script every time you interact with it. It's like when you click a button, type text, or change a dropdown. Without session state, all your variables would reset on every rerun, so your game would forget the secret number, your score, and how many attempts you've made. 
- What change did you make that finally gave the game a stable secret number?
A: I didn't make any changes to the secret number stability. The original code already had the if 'secret' not in st.session_state: check that prevented it from regenerating on every rerun. The bugs I actually fixed were the New Game button (which wasn't resetting the game state properly), the attempts count for different difficulties, and the hint messages that were backwards.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
A: Starting new chat for the project. Also double checking what the AI give as an answer. In addition asking the AI for test cases that fits to the application I am doing.
- What is one thing you would do differently next time you work with AI on a coding task?
A: I would try to add more detail to my prompt for a better answer.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
A: After using Claude Code with Copilot, making project like this feel a lot better than starting from scratch.

