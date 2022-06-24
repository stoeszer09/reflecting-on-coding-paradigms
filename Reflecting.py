"""
Functional Prompt
Implement a function that will flatten and sort an array of integers in ascending order, and which adheres to a functional programming paradigm.
"""
def my_list_sorter(the_list):
  new_list = list()
  return new_list

"""
How does this solution ensure data immutability?
Is this solution a pure function? Why or why not?
Is this solution a higher order function? Why or why not?
Would it have been easier to solve this problem using a different programming style?
Why in particular is functional programming a helpful paradigm when solving this problem?
"""



"""
Object Oriented Prompt
Watto needs a new system for organizing his inventory of podracers. Help him do this by implementing an Object Oriented solution according to the following criteria.

First, he'll need a general Podracer class defined with max_speed, condition (perfect, trashed, repaired) and price attributes.
Define a repair() method that will update the condition of the podracer to "repaired".
Define a new class, AnakinsPod that inherits the Podracer class, but also contains a special method called boost that will multiply max_speed by 2.
Define another class that inherits Podracer and call this one SebulbasPod. This class should have a special method called flame_jet that will update the condition of another podracer to "trashed".
"""

class Podracer:
  def __init__(self, max_speed, condition, price):
    self.max_speed = max_speed
    self.condition = condition
    self.price = price
  def repair(self):
    self.condition = 'repaired'
  def set_condition(self, condition):
    self.condition = condition

class AnakinsPod(Podracer):
  def __init__(self, max_speed, condition, price):
    super().__init__(max_speed, condition, price)
  def boost(self):
    self.max_speed = self.max_speed * 2

class SebulbasPod(Podracer):
  def __init__(self, max_speed, condition, price):
    super().__init__(max_speed, condition, price)
  def flame_jet(self, other_pod):
    other_pod.set_condition('trashed')

my_first_pod = Podracer(4, 'trashed', 20000)
my_first_pod.repair()
print(my_first_pod.condition)

new_pod = AnakinsPod(2, 'perfect', 10000)
new_pod.boost()
print(new_pod.max_speed)

third_pod = SebulbasPod(2, 'perfect', 25000)
third_pod.flame_jet(third_pod)    ####### Acceptance says it should trash itself, BUT directions said update the condition of ANOTHER podracer
print(third_pod.condition)


"""
How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)
Encapsulation
Abstraction
Inheritance
Polymorphism
Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?
How in particular did Object Oriented Programming assist in the solving of this problem?
"""



"""
Reflection

Is one of these coding paradigms "better" than the other? Why or why not?
Given the opportunity to work predominantly using either of these coding paradigms, which seems more appealing? Why?
Now being more familiar with these coding paradigms, what tasks/features/pieces of logic would be best handled using functional programming? Object Oriented Programming?
Personally, which of these styles takes more work to understand? What should be done in order to deepen understanding related to this paradigm?

"""