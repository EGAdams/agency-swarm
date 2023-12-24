#include "scoreboard_controller.h"
#include <iostream>

ScoreboardController::ScoreboardController() {
    // Constructor
}

void ScoreboardController::updateScore(int score) {
    // Update the scoreboard with the given score
    std::cout << "Score updated: " << score << std::endl;
}

void ScoreboardController::displayScoreboard() {
    // Display the current scoreboard
    std::cout << "Displaying Scoreboard" << std::endl;
}
