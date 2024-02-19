CXX = g++
CXXFLAGS = -std=c++11 -Wall

scoreboard_controller: ScoreboardController.o
	$(CXX) $(CXXFLAGS) -o scoreboard_controller ScoreboardController.o

ScoreboardController.o: ScoreboardController.cpp
	$(CXX) $(CXXFLAGS) -c ScoreboardController.cpp

clean:
	rm -f scoreboard_controller ScoreboardController.o
