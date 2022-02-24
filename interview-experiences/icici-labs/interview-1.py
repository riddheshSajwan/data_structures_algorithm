class Solution:
    res = []
    def all_possible_emails(self,idx,user,n):
        if idx >= n-1:
            return
        new_user = user[:idx+1] + '.' + user[idx+1:]
        self.res.append(new_user)
        self.all_possible_emails(idx+2,new_user,n+1)
        self.all_possible_emails(idx+1,user,n)
        return
    def main(self,username):
        self.res.clear()
        self.res.append(username)
        self.all_possible_emails(0,username,len(username))
        return self.res
    
print(Solution().main("abcde"))
    
    