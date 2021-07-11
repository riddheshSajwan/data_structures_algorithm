def generateParenthesis(n):
    result = []
    if n == 0:
        return [""]

    def _genPar(S = "", open = n, close = n):
        if open == 0 and close == 0:
            result.append(S)
            return
        if open > 0:
            _genPar(S+"(",open-1,close)
        if open < close:
            _genPar(S+")",open,close-1)
    _genPar()
    return result
print(generateParenthesis(4))