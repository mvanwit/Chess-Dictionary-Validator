exampleBoard = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}

exampleBoard2 = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'zbishop', '9z': 'bking', '3c': 'bpawn', '4c': 'bpawn'}



def isValidChessBoard(someDict):
    
    errorLog = []
    #Initialization of piece counters
    kingCount = {'b': 0, 'w':0}
    piecesCount = {'b': 0, 'w':0}
    pawnsCount = {'b': 0, 'w':0}

    #List of valid chess pieces denomination and colors
    validPiecesName = ['king', 'queen', 'bishop', 'rook', 'knight', 'pawn']
    validColors = {'b':'black', 'w':'white'}
    validSpace = []
  
    #Construction of a list of valid spaces on a chess board  
    for num in range(1,9):
        for letter in 'abcdefgh':
            validSpace.append(str(num)+letter)
            
    #Check if every key of the dictionary are valid chess board spaces
    for k in someDict.keys():
        if k not in validSpace:
            errorLog.append(str(k) + ' is not a valid chess space.')
    
    
    for v in someDict.values():
        #Count white pieces
        if v[0] == 'w':
            piecesCount['w'] += 1
            if v[1:] == 'king':
                kingCount['w'] += 1 
            elif v[1:] == 'pawn':
                pawnsCount['w'] += 1 
            elif v[1:] not in validPiecesName:
                errorLog.append(str(v) + ' is not a valid chess piece.') #Error message if not a valid chess piece denomination
        #Count black pieces
        elif v[0] == 'b':
            piecesCount['b'] += 1 
            if v[1:] == 'king':
                kingCount['b'] += 1 
            elif v[1:] == 'pawn':
                pawnsCount['b'] += 1
            elif v[1:] not in validPiecesName:
                errorLog.append(str(v) + ' is not a valid chess piece.') #Error message if not a valid chess piece denomination
                
        #Error message if neither a black or white piece
        else:
            errorLog.append(str(v) + ' is not a valid chess piece.') 



    #Check if there's one and only one king per player
    if kingCount['w'] == 0:
        errorLog.append('There must be ONE white king.') 
    elif kingCount['w'] > 1:
        errorLog.append('There can only be ONE white king. This board contains ' + str(kingCount['w']) + ' white kings.') 
    if kingCount['b'] == 0:
        errorLog.append('There must be ONE black king') 
    elif kingCount['b'] > 1:
        errorLog.append('There can only be ONE black king. This board contains ' + str(kingCount['b']) + ' black kings.')

    #Check if there's not too many pieces ( 16 pieces 8 pawns max per player )
    if piecesCount['b'] > 16:
        errorLog.append('Black player has too many pieces: ' + str(piecesCount['b']) + ' black pieces. (max : 16).')
    if piecesCount['w'] > 16:
        errorLog.append('White player has too many pieces: ' + str(piecesCount['w']) + ' white pieces. (max : 16).')
    if pawnsCount['b'] > 8:
        errorLog.append('Black player has too many pawns: ' + str(pawnsCount['b']) + ' black pawns. (max : 8).')
    if pawnsCount['w'] > 8:
        errorLog.append('White player has too many pawns: ' + str(pawnsCount['w']) + ' white pawns. (max : 8).')

    #Return result and error log 
    if errorLog == []:
        return True
    else:
        print('Error Log:')
        for error in errorLog:
            print(error)
        return False
