def isValid(s) :
    Open = ["(", "{", "["]
    Stack = []
    for item in list(s):
        if item in Open:
            Stack.append(item)
            Response = False
        else:
            if len(s) <2 or s[0] not in Open or len(Stack)<1:
                Response = False
                break
            elif item == ")" and Stack[-1] == "(":
                Response = True
                Stack.pop()
            elif item == "}" and Stack[-1] == "{":
                Response = True
                Stack.pop()
            elif item == "]" and Stack[-1] == "[":
                Response = True
                Stack.pop()
            else:
                Response = False
                break
    if len(Stack) >0:
        Response = False
    return Response
print(isValid("({}"))