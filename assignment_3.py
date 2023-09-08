# Q : 1
class palindrom_or_balanced:
    def __init__(self):
        self.stack = []
        self.queue = []
    

    def is_palindrome(self, input_str):
        input_str = input_str.lower()

        for char in input_str:# O(n) n being the length of the input_str
            if char.isalnum(): # found this on https://www.digitalocean.com/community/tutorials/python-string-isalnum to check if the charcter is valid or not
                self.stack.append(char) 
                self.queue.insert(0, char)
# we will empty both stack and queue while checking for mismatchings , this way we can compare the first charcter with the last on
        while self.stack and self.queue: #O(n) n also the length of the input-str 'the stack in this case'
            if self.stack.pop() != self.queue.pop(0):
                return False

        return True
    def is_balanced(self,exp):
        ob = "({["
        cb = ")}]"

        for char in exp: # O(n) n being the size of the exp
            if char in ob: #if the char is an oppening bracket append it to the stack
                self.stack.append(char)
            elif char in cb: # if it was a closing bracket 
                if not self.stack : #check if the stack is empty first if so then it's invalid bracket 
                    return False  
                if ob.index(self.stack.pop()) != cb.index(char): #check if the last item in the stack has a valid closing bracket and remove it from the stack if so
                    return False  

        return len(self.stack) == 0  
    