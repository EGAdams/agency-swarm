#ifndef ISCORE_CONTROLLER_H
#define ISCORE_CONTROLLER_H

class IScoreController {
public:
    virtual void updateScore(int score) = 0;
    virtual void displayScoreboard() = 0;
    virtual void playerScored(int playerId) = 0;
    virtual void undoLastScore() = 0;
};

#endif // ISCORE_CONTROLLER_H
