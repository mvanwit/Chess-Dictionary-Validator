exampleBoard = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}

exampleBoard2 = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'zbishop', '9z': 'bking', '3c': 'bpawn', '4c': 'bpawn'}

exampleBoard3 = {'1a': 'bking','2a': 'bqueen','3a': 'brook','4a': 'brook',
'5a': 'bknight','6a': 'bknight','7a':'bbishop','8a': 'bbishop',
'1b': 'bpawn','2b': 'bpawn','3b': 'bpawn','4b':'bpawn',
'5b': 'bpawn','6b': 'bpawn','7b': 'bpawn','8b': 'bpawn',
'1c': '','2c': 'wqueen','3c': 'wrook','4c': 'wrook',
'5c': 'wbishop','6c': 'wbishop','7c': 'wknight','8c':'wknight',
'1e': 'wpawn','2e': 'wpawn','3e': 'wpawn','4e': 'wpawn',
'5e': 'wpawn','6e': 'wpawn','7e': 'wpawn','8e': 'wpawn',
'1f': 'bking','2f': 'bking','3f': 'wpawn','4f': 'zqueen','5f': 'wpawn','6f': 'bpawn','7f': 'bpiece','8f': 'zpiece',
'1g': '','2g': '','3g': '','4g': '','5g': '','6g': '','7g': '','8g': '',
'1h': '','2h': '','3h': '','4h': '','5h': '','6684': '','7z': '','9h': ''}



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
        #Error message if neither a black or white piece
        if v == '':
            pass
        elif v[0] not in validColors.keys():
            errorLog.append(str(v) + ' is not a valid chess piece.')
        else:
            for color in validColors.keys():                
                #Count white pieces
                if v[0] == color:
                    piecesCount[color] += 1
                    if v[1:] == 'king':
                        kingCount[color] += 1 
                    elif v[1:] == 'pawn':
                        pawnsCount[color] += 1 
                    elif v[1:] not in validPiecesName:
                        errorLog.append(str(v) + ' is not a valid chess piece.') #Error message if not a valid chess piece denomination

                


    for color in validColors.keys():
        #Check if there's one and only one king per player
        if kingCount[color] == 0:
            errorLog.append('There must be ONE ' + validColors[color] + ' king.')
        elif kingCount[color] > 1:
            errorLog.append('There can only be ONE ' + validColors[color] +' king. This board contains ' + str(kingCount[color]) + ' ' + validColors[color] + ' kings.') 

        #Check if there's not too many pieces ( 16 pieces 8 pawns max per player )
        if piecesCount[color] > 16:
            errorLog.append(validColors[color] + ' player has too many pieces: ' + str(piecesCount[color]) + ' ' + validColors[color] + ' pieces. (max : 16).')
        if pawnsCount[color] > 8:
            errorLog.append(validColors[color] + ' player has too many pawns: ' + str(pawnsCount[color]) + ' ' + validColors[color] + ' pawns. (max : 8).')
        

    #Return result and error log 
    if errorLog == []:
        return True
    else:
        print('Error Log:')
        for error in errorLog:
            print(error)
        return False
