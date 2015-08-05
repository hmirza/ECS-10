
def insert_grade(grade_book):
  """
  Requests that the use enter name of grade of a student.
  If the student is not in the grade_book it adds the student
  to the grade_book and sets their grade to the grade given.
  If the student is in the grade_book it sets their grade
  to the grade given.
  @grade_book: a dictionary mapping student names to their grades.
    This dictionary is modified based on the student name and grade
    entered.
  @returns:None
  """
  grade_prompt = "Enter name and points (Ex. 'Bob 95'): "
  name, grade = input(grade_prompt).split()
  grade_book[name] = int(grade) #store name and grade
  
#end insert_grade
  
def delete_student(grade_book):
  """
  Requests that the user enters a student's name and then removes them
  from the grade_book if they are present. If the student is not present
  then then the grade_book is not modified.
  @grade_book: a dictionary mapping student names to their grades.
    This dictionary is modified based on the name of the student entered.
  @returns: None
  """
  delete_prompt = "Enter a name to be removed (Ex. Bob): "
  name = input(delete_prompt).lower().strip() # get name
  grade_book.pop(name, None)#and remove if they exist    
  
#end delete_student


def display_grades(grade_book):
  """
  Display the students' names along with their grades in alphabetical order
  @grade_book: a dictionary mapping student names to their grades.
  @returns: None
  """
  print('\n-----Displaying Grades-----')
  #displays the students in alphabetical order
  for (student, grade) in sorted(grade_book.items()):    
    print('{:<10s} : {:>3d}'.format(student,grade))
  print('-----Done Displaying Grades-----\n')
#end display_grades
  
def mean(numbers):
  """
  Calculates the mean of a set of numbers.
  @numbers: an interable of numbers
  @returns: the mean of numbers
  """
  #calcualtes the mean
  mean = sum(numbers) / len(numbers)
  return mean
  

#end mean

def median(numbers):
  """
  Caculates the median of a set of numbers
  @numbers: an iterable of numbers
  @returns: the median of numbers
  """
  #calculates the median
  median = sorted(numbers)[len(numbers)//2]
  return median
  
#end median

def mode(numbers):
  """
  Calculates the mode of a set of numbers.
  @numbers: an iterable of numbers
  @returns: the mode of those numbers
  """
  #calculates the mode
  mode_dict = {} #have to keep track of counts for each value so use a dict
                 #that maps values to counts
  #fills out the dict
  for grade in numbers:
    if grade in mode_dict:
      mode_dict[grade] += 1
    else:
      mode_dict[grade] = 1
    #finds the value that occured the most
    mode = max(mode_dict.items(), key = lambda x: x[1])[0]
  return mode

#end_mode

def display_statistics(grade_book):
  """
  Display the mean, median, and mode of the grades
  contained in the grade_book.
  @grade_book: a dictionary mapping student names to their grades.
  @returns: None
  """
  #displays statistics  
  grades = grade_book.values()
  print('\n-----Displaying Statistics-----')
  print('Mean   : {:>6.2f}'.format(mean(grades)))
  print('Median : {:>3d}'.format(median(grades))) 
  print('Mode   : {:>3d}'.format(mode(grades)))   
  print('-----Done Displaying Statistics-----\n')
#end_display_statistics

def numbers():
  list_num = list(grade_book.values())
  for num in list_num:
    numbers = int(num)



  
def main():
  grade_book = {} # the grade_book
  menu_prompt = ("1. Add/modify student grade\n"
                "2. Delete student grade\n"
                "3. Print student grades\n"
                "4. Display the course statistics\n"
                "5. Quit\n"
                "Your choice: ")
      
  while True:  # Exit when user enters choice 5
      command = input(menu_prompt).lower().strip() #read command
      if command == '1': #adds a student
        insert_grade(grade_book)             
      elif command == '2': #removes student from grade book
          delete_student(grade_book)
      elif command == '3':#displays grades
        display_grades(grade_book)
      elif command == '4': #displays statistics
        display_statistics(grade_book)
      elif command == '5': #done
          break
      else: #erroneous command
          print('Unrecognized command.')
#end main

if __name__ == '__main__': #if this is the main program run
  main() #run the main function
 
