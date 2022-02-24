'''
What is method overloading 

COWIN DATABASE MODEL:

Users(user_id,user_name,user_number,user_email)
patients(user_id,patient_id, patient _name, patient _age, patient_city, patient_state,patient _location,first_vacc_date, second_vacc_date),
Vaccine(vaccine_name, vaccine_price ,number_of_doses_reqd,number_of_days_gap,vaccine_quantity_left),
vaccination_status(patient _id, vaccine_name,first_vaccination_date,second_dose_due),
vaccination_centers(center_id,center_name,center_city,center_pincode,center_location,center_type, center_capacity,center_inventory),

Display all centers, center_capacity, center_type that are in a certain pincode. 
SELECT center_name,center_capacity,center_type 
FROM vaccination_centers
WHERE center_pincode = pin

Find all the patients who have defaulted (crossed due date).
GROUP BY patient_state,patient_id
FROM patients
HAVING second_vacc_date < today.date()
'''
#Write a code to insert into a linkedlist.
class Node:
    def __init__(self,value):
        self.val = value
        self.next = None
class LinkedList:
    def __init__(self,node):
        self.head = node
        self.size = 1
    def append(self,node):
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = node
        self.size += 1
    def insert(self,index,node):
        curr = self.head
        if index > self.size:
            return "error"
        while curr and index > 0:
            curr = curr.next
            index -= 1
        temp = curr.next
        curr.next = node
        node.next = temp
        self.size += 1

head = LinkedList(Node(3))

#largest 1-squared array
grid = [[0,1,1,1,1,0],[1,1,0,1,1,0],[1,1,0,1,0,1],[1,1,0,1,1,1],[1,1,0,1,1,1],[1,1,1,1,1,1],[1,0,1,1,1,1],[0,0,1,1,1,1],[1,1,1,1,1,1]]
n = len(grid)
m = len(grid[0])
hor = [[0]*m for i in range(n)]
ver = [[0]*m for i in range(n)]
for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            hor[i][j] = grid[i][j]
            ver[i][j] = grid[i][j]
        elif i == 0:
            if grid[i][j] == 1:
                hor[i][j] = hor[i][j-1] + grid[i][j]
            ver[i][j] = grid[i][j]
        elif j == 0:
            if grid[i][j] == 1:
                ver[i][j] = ver[i-1][j] + grid[i][j]
            hor[i][j] = grid[i][j]
        else:
            if grid[i][j] == 1:
                hor[i][j] = hor[i][j-1] + grid[i][j]
                ver[i][j] = ver[i-1][j] + grid[i][j]
ans = 0
#print(hor,ver)
for i in range(n-1,-1,-1):
    for j in range(m-1,-1,-1):
        if grid[i][j] == 0:
            continue
        
        length = min(hor[i][j],ver[i][j])
        while (length > ans):
            #print(length,i,j)
            if ver[i][j-length+1] >= length and hor[i-length+1][j] >= length:
                ans = length
            length -= 1
print(ans*ans)
