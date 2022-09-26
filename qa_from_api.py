# Avoid adding a block of code for each question & answer by iterating the conditional statement through a single randomized list of lists.
# Randomize the list of lists using .shuffle() method. The order inside the nested lists won't change, so for example L[0][0] is the question and L[0][1] is the answer of the first element of the randomized list.
# Make the input case-insensitive with .lower() method.
# Optional: add a count of right and wrong answers.

import requests

attempt = 0 
while attempt < 2:  
    category = 'geography'
    api_url = 'https://api.api-ninjas.com/v1/trivia?category={}'.format(category)
    response = requests.get(api_url, headers={'X-Api-Key': 'ijPUMy8+lGRW1u+piM4+kg==z7yWeQo4stnSSmmL'})
    if response.status_code == requests.codes.ok:
        d = response.json()[0]
    
    L = [] 
    for key, val in d.items(): 
        L.append([key, val]) 
    print(L)

    # # L = [['category', 'geography'], ['question', 'In which city is the Wailing Wall'], ['answer', 'Jerusalem']]
    
    r = 0 # right answers count
    w = 0 # wrong answers count

    
    
    
    attempt = attempt + 1
    user_input = input(L[1][1])
    if user_input.lower() == L[2][1].lower():
        r = r + 1 and print("That's right !")   
    else:
        w = w + 1 and print("Wrong answer")
    print(str(r) + " right and " + str(w) + " wrong answers)")




