import gradio as gr
"""
This will compare the words given in lexicographic value.
If main word value is less than the previous then it will
compare the main word if its greater than the previous it will return false.
other way returns true

@param main word: the main index the word is being compared
@param previous word : the previous index the word is being compared
@return True or False
"""
def compare_names(main_word, prev_word):
  #intial start
  index = 0

  #This will check each character on the word for the lexicographic value and compare which one is greater
  while index < len(main_word) and index < len(prev_word):
    if main_word[index] < prev_word[index]:
      return True
    elif main_word[index] > prev_word[index]:
      return False
    index += 1
  #if all charcters matchs then it will check for the shorter lengths
  return len(main_word) < len(prev_word)


"""
This is the instertion sort that will sort the
names of the list given in alphabetical order

@param List:  list of names of the given
@return a New List of names in alphabetical order
"""
def alphabetical_sort(list_names):
  #check if there a list
    if len(list_names) <= 0:
        return list_names

    for index in range(1, len(list_names)):
        #intial hold of the word being compared
        main_word = list_names[index]
        prev_index = index - 1

        # Moving the word to the right until its find a word that is smaller than its
        while prev_index >= 0 and compare_names(main_word, list_names[prev_index]):
            list_names[prev_index + 1] = list_names[prev_index]
            prev_index -= 1

        # Insert the word
        list_names[prev_index + 1] = main_word

    return list_names

"""
Takes a string from the textbox: "apple, orange, honey"
Converts it to a list, sorts it, then returns a string.

@Param input_text: This is the user given list from his inputs
@Return: the list order alphabetical
"""
def sort_interface(input_text):
 
    # convert into the list 
    if (not (word.strip() for word in input_text.split(",") if word.strip())):
      return "Wrong Input"
    
    names = [word.strip() for word in input_text.split(",") if word.strip()]

    # call sorting algorithm
    sorted_names = alphabetical_sort(names)

    # return as a string for output
    return ", ".join(sorted_names)



demo = gr.Interface(
    fn=sort_interface,
    inputs=gr.Textbox(
        label="Enter names separated by commas",
        placeholder="Example: apple, orange, honey"
    ),
    outputs=gr.Textbox(label="Sorted Result"),
    title="Alphabetical Sorting (Insertion Sort + Lexicographic Comparison)",
    description="Enter any number of names and the app will sort them alphabetically using insertion sort."
)

demo.launch()