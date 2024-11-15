## 1. Prompts Used



Write some python code in this file that shows finding new insights when printing results from analysis

Write some python code in this file that shows finding new insights when printing results from analyzing two different lists of numbers

Write some python code in this file that shows finding new insights when printing results from analyzing two different lists of words



## 2. Prompting Strategy

I decided to start of vague with both Copilot and GPT, and found that they both analyzed lists of numbers, even when I didn't provide that specification. I wanted more variety without making it few-shot, so I got more specific on what they should use, first clarifying that they need numbers and second making it be words instead.

## 3. Output Evaluation

For each generated code output, consider:
    - Narrative Structure: How does the organization reflect the theme? Is there a clear flow that resembles a narrative?
    - Commentary and Documentation: How do Copilot’s comments contribute to the narrative? Do they add meaning to the code?
    - Design Choices: Evaluate how Copilot's naming conventions, variable usage, and logic choices enhance or detract from the narrative.

### Copilot

It seems to get the job done, and while I only used it for generating and not editing existing code, it definetly seems to be useful. I noticed that in terms of code, it uses less comments less flashy print statements than other LLM's like GPT. There is a clear flow though on data analysis and presenting the findings. In terms of naming/variables, copilot seems to name variables what was done to them to creat them. For instance, the variable sorted_numbers was made by, you guessed it, sorting the numbers.

### Other Single LLM

GPT-4 did fine generating code, making the narrative very clear with a lot of descriptive comments and print statements. It did lack narration in terms of variable naming, as it named the initial data as unique_to_a which proves it already concluced analysis by the time this code was generated.

## 4. Reflection

 How did your prompt iterations impacted the narrative quality of the generated code? How did Copilot's suggestions supported or hindered the story within the code? 
I got more descriptive with what I wanted them to analyze which drastically affected the generated code, and in this example copilot helped me more then OpenAI, which I have a lot more experience with.