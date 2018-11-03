class stack:
	def __init__(self):
		self.items=[]
	def isEmpty(self):
		return self.items == []
	def push(self,item):
		self.items.append(item)
	def pop(self):
		return self.items.pop()
	def peek(self):
		return self.items[-1]
	def size(self):
		return len(self.items)
	
ip=list(input('Enter the infix expression: '))
print (ip)
operators=stack()
operands=stack()

def operatorsPriority(x):
	if x=='^':
		return 4
	if x=='*' or x=='/':
		return 3
	if x=='+' or x=='-':
		return 2
	if x=='(':
		return 1
			
def infixToPrefixConverter(xList):	
	for item in xList:
		#print (operators.show())
		#print (operands.show())	
		if item ==' ':
			continue
		if item in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz' or item in '0123456789':
			operands.push(item)
		elif item == '(':
			operators.push(item)
		elif item == ')':
			temp=operators.pop()
			while temp != '(':
				operand2=operands.pop()
				operand1=operands.pop()
				operands.push(temp+operand1+operand2)
				temp=operators.pop()
		else:
			while (not operators.isEmpty()) and operatorsPriority(item)<=operatorsPriority(operators.peek()):
				operand2=operands.pop()
				operand1=operands.pop()
				operands.push(operators.pop()+operand1+operand2)

			operators.push(item)
	#print ('done')
	while not operators.isEmpty():
		#print (operators.show())
		#print (operands.show())
		operand2=operands.pop()
		operand1=operands.pop()
		operands.push(operators.pop()+operand1+operand2)

	return (operands.pop())

print (infixToPrefixConverter(ip))