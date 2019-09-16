def get_user_input_list_and_print_even():
    counter = 0
    user_input_list = []
    while counter < 6:

        user_input_list += int(input("Give me your number: "))
        counter +=1
    
    even_list = [aa for aa in user_input_list if aa % 2 == 0]

    print(even_list)
    print("Hello")

get_user_input_list_and_print_even()

