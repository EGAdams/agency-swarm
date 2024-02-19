#ifndef SCOREBOARDCONTROLLER_H
#define SCOREBOARDCONTROLLER_H

class ScoreboardController {
public:
    ScoreboardController();
    void initialize();
    void updateScore(int player, int score);
    void displayScoreboard();
    void resetScoreboard();
private:
    // Private member variables and functions
};

#endif // SCOREBOARDCONTROLLER_H