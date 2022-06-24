# Functional Prompt

def my_list_sorter(the_list):
  new_list = list()
  for item in the_list:
    if type(item) == list:
      new_list = new_list + my_list_sorter(item)
    else:
      new_list.append(item)
  return sorted(new_list)

print(my_list_sorter([4, [3, [12, 14], 5, 7, [50, 20]], 2, 1]))

"""
How does this solution ensure data immutability? It returns a new list instead of changing the original
Is this solution a pure function? Why or why not? Yes, it only depends on the input and nothing outside of itself
Is this solution a higher order function? Why or why not? No, it does not accept or return a higher order function. But it is recursive :)
Would it have been easier to solve this problem using a different programming style? Not on something as foundational as a list. It wouldn't make sense to make an object class for this.
Why in particular is functional programming a helpful paradigm when solving this problem? This function only has one job to focus on
"""



# Object Oriented Prompt

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

pod = Podracer(4, 'trashed', 20000)
pod.repair()
print(pod.condition)

new_pod = AnakinsPod(2, 'perfect', 10000)
new_pod.boost()
print(new_pod.max_speed)

third_pod = SebulbasPod(2, 'perfect', 25000)
third_pod.flame_jet(third_pod)    ####### Acceptance says it should trash itself, BUT directions said update the condition of ANOTHER podracer
print(third_pod.condition)


"""
How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)
Encapsulation - Maybe I'm thinking about this wrong, but that's what an object is. Information about one thing, bundled up into one object. So doing OOP without encapsulation doesn't seem possible.
Abstraction
Inheritance - The repair method was inherited to the other classes as well as setting the self attributes.
Polymorphism
Would it have been easier to implement a solution to this problem using a different coding style? Why or why not? No, even at this small amount, I think OOP was easiest
How in particular did Object Oriented Programming assist in the solving of this problem? OOP seems particularly useful when representing something in the real world.
"""




# Reflection

"""
Is one of these coding paradigms "better" than the other? Why or why not? No, it really depends on what the end goal is.
Given the opportunity to work predominantly using either of these coding paradigms, which seems more appealing? Why? I currently feel more comfortable with OOP because it feels more tangible.
Now being more familiar with these coding paradigms, what tasks/features/pieces of logic would be best handled using functional programming? Object Oriented Programming? Functional Programming seems to be better for handling abstract ideas and OOP is better at representing real world examples
Personally, which of these styles takes more work to understand? What should be done in order to deepen understanding related to this paradigm? At the moment I find the Functional Programming more difficult because I have questions with the prompts that are not answered. CodeWars and LeetCode seem to be more ideal for Functional Programming.

"""