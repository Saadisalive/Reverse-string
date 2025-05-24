class reverse_string:
    def __init__(self, string):
        self.string = string
    def reverse(self):
        reversed_string = ""
        for i in range(len(self.string) -1, -1, -1):
            reversed_string += self.string[i]
        return reversed_string
    def __str__(self):
        return self.reverse()
if __name__ == "__main__":
    #enter a string to reverse or enter a reversed string to print it back 
    string = input("Enter a string to reverse:")
    r = reverse_string(string)
    print("Reversed string is:", r)