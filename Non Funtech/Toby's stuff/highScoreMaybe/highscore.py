high_scoreFile = open("HighScoreText", "r+")
HighScoreNum = high_scoreFile.read()
user_input = input("whats your score?: ")
if int(user_input) > int(HighScoreNum):
    del HighScoreNum
    HighScoreNum = user_input
    print("new highscore: " + HighScoreNum)
    test = open("HighScoreText", "w")
    test.write(HighScoreNum)
    test.close()
    high_scoreFile.close()
else:
    print("highscore: " + HighScoreNum)
    high_scoreFile.close()
