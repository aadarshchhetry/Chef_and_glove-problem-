def check_gside(T):

    for a in range(0,T):
        
        L = []
        G = []
        side = []
        Front = True
        Back = True
        Both = False
        non = False

        N = int(input('Enter the number of Fingers on chef fingers:')) 

        #input the length of each fingers
        for i in range(0,N):
            L.append(int(input(f'Enter the len of Finger{i+1}: ')))

        #input the lenth of each gloves
        for i in range(0,N):
            G.append(int(input(f'Enter the Glove len of Finger{i+1}: ')))

        #comparing the len of glove to fingers
        for i in range(0,N):

            if L[i] > G[i]:
                Front = False

            if L[i] > G[-(i+1)]:
                Back = False

        if Front ==True and Back == True:
            Both  = True
        elif Front == False and Back == False:
            non = True

        if Both:
            side.append('Both')
        elif non:
            side.append('None')
        elif Back:
            side.append('Back')
        elif Front:
            side.append('Front')
            

    for k in range(0,T):
        print(f'The prefered side to wear gloves on Turn {k+1} will be : {side[k]}')

turn = int(input('Enter the number of turns: ')) 
check_gside(turn)