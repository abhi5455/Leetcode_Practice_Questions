class Solution(object):
    def defangIPaddr(self, address):
        return address.replace('.', '[.]')

# class Solution(object):
#     def defangIPaddr(self, address):
#         newAddr = address.split('.')
#         return '[.]'.join(newAddr)
