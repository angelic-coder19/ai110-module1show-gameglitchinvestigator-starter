# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
  1. The hints are backwards, it recommends you to go higher when the geuess is too high, and lower when the guess is too low 

  2. The enter button doesn't work, it doesn't register the guess and doesn't give any feedback to the user
  
  3. The range of target number is always displayed as 1-100, even when a different difficulty level is selected. It is always static and doesn't update based on the difficulty level chosen by the user.
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
Answer: I used GitHub Copilot.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
Answer: One example of a correct AI suggestion was when I was trying to fix the scoring system. It noticed that the scoring functions was assymetrical and suggested a more balanced approach. Speficically, it noticed that when the attempt number was even and the guess was too high, the score would get a 5 point boost and a 5 point penalty otherwise. However, when the guess was too low, it would simply get a 5 point penalty regardless of the attempt number. The AI suggested that the scoring system should be consistent, so it recommended that the score should get a 5 point boost when the attempt number is even and the guess is too low, and a 5 point penalty otherwise. I verified the result by running the game and testing different scenarios to see if the scoring system was working as expected.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
Answer: One example of an incorrect AI suggestions was when I was trying to fix the issue with the dislay of the range of the target number. The AI suggested that I should change the code to update the range based on the difficulty level selected by the user. However, it did not provide a specific solution on how to implement this change. I tried to follow the suggestion, but I was not able to figure out how to update the range dynamically based on the user's selection. After some trial and error, I realized that I needed to use Streamlit's session state to store the selected difficulty level and update the range accordingly. This was not something that the AI had suggested, and I had to come up with this solution on my own.


---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

Answer: For each bug, I ran streamlit and tested the specific functionality that was affected by the bug. For example, when I fixed the issue with the hints being backwards, I ran the game and made guesses that were too high and too low to see if the hints were now giving the correct feedback. I also tested different difficulty levels to see if the range of the target number was updating correctly. If the game behaved as expected and provided the correct feedback based on my interactions, I considered the bug to be fixed.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.

Answer: One test I ran was a manual test to check if the scoring system was working correctly after I implemented the changes suggested by the AI. I played the game and made guesses that were too high and too low, while keeping track of the attempt number. I observed how the score changed based on my guesses and the attempt number. This test showed me that the scoring system was now consistent and working as expected, with the correct boosts and penalties being applied based on whether the guess was too high or too low and whether the attempt number was even or odd.

- Did AI help you design or understand any tests? How?
Answer: Yes, AI helped me design the tests by suggesting scenarios to test based on the changes I made to the code. For example, when I fixed the error with the hints being backwards, the AI suggested that I should test both scenarios of making a guess that is too high and a guess that is too low to ensure that the hints were providing the correct feedback.
---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
Answer: The secret number bug was fixed even before this assignment was assigned. During the initial breakout room March 4th. I asked the TF to clarify why this reflection.md file did not reflect the actual bugs in the game. He did confirm that this file was an older version and that some bugs cited here were fixed prior to the assignment. 

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Answer: reruns refer to the way Streamlit automatically re-executes the entire script every time a user interacts with the app, such as clicking a button or changing a slider. This means that any changes in the app's state can cause the script to run again from the top. 
Session state is a feature in Streamlit that allows you to store and manage data across these reruns. It helps you maintain the state of variables, user inputs, and other data even when the script is re-executed, ensuring that your app behaves consistently and retains important information throughout the user's interaction.

- What change did you make that finally gave the game a stable secret number?
Answer: The change I made to give the game a stable secret number was to generate the secret number once and store it in Streamlit's session state. This way, the secret number is generated only once when the game starts and remains consistent throughout the user's interaction with the app, even as they make guesses and interact with the game.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?

Answer: One strategy I will use from this project is making small incremental changes with smaller scope at each time, and testing the changes immediately after implementing them.

- What is one thing you would do differently next time you work with AI on a coding task?

Answer: Next time I work with AI, I will start by asking it to critically analyze the entire codebase in its initial state to understand the overall structure and identify potential issues before I start making changes. This way, I can have a better understanding of the code and be more strategic in how I use AI suggestions.

- In one or two sentences, describe how this project changed the way you think about AI generated code.
Answer: AI can be powerfull when given very specific prompts, and smaller scope changes. When given vague prompts and larger scope, the results are underwhemlming and imperfect.
