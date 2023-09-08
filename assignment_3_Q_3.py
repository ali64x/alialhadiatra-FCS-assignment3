# Q : 3
class MIB :
    def init (self):
        self.stack = []
    def decode_message(self,message):
        self.stack=[]
        decoded_message = ""

        for char in message: # O(n) n is the length of the message 
            if char.isalpha() or char.isspace():
                self.stack.append(char)
            elif char == '*':
                if self.stack:
                    decoded_message += self.stack.pop()

        # After processing the message, pop any remaining characters from the stack
        while self.stack: # O(n) the number of the remaining charecters in the stack
            decoded_message += self.stack.pop()

        return decoded_message
