# Restructuring a Lathe Training Manual

## Objective:

The goal of this exercise is to restructure and modify the JSON data representing a lathe training manual for improved organization and readability.


## Exercise Instructions:

You are provided with a JSON file containing information about a "Lathe" machine operator training manual. Your tasks are as follows:

1. **Separate Glossary and Index:** Extract the "glossary" and "index" entries from the main JSON object and create two separate JSON objects named "glossary_json" and "index_json". 

2. **Nest Chapters:**  Create a new array called "chapters" within the main JSON object. Move all the data currently under the "chapters" key into this new "chapters" array. Each element in the "chapters" array should represent a single chapter.

3. **Add Chapter Numbering:** Within each chapter object, add a new field named "chapterNumber" and assign it a sequential number starting from 1.

4. **Consolidate Image and Video Information:**  For each section within the chapters, combine the "images" and "videos" arrays into a single array named "media".



By completing these steps, you will create a more organized and structured JSON representation of the lathe training manual.