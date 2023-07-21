#include <iostream> 
#include <fstream>
#include <sstream>
#include <vector>

struct Player{
    int intstats[11];
    double doublestats[8];
} typedef Player;

std::vector<Player> fillPlayers(std::ifstream file){
    if(!file.is_open()){
        std::cout << "File not found" << std::endl;
        exit(1);
    }
    std::vector<Player> players;
    std::string line;
    std::getline(file, line); //first line of data file empty
    while(!file.eof()){
        Player p;
        std::getline(file, line);
        std::istringstream iss(line);
        for(int i = 0; i < 3; i++){
            iss >> p.intstats[i];
        }
        for(int i = 0; i < 4; i++){
            iss >> p.doublestats[i];
        }
        iss >> p.intstats[3];
        iss >> p.doublestats[4];
        for(int i = 4; i < 8; i++){
            iss >> p.intstats[i];
        }
        for(int i = 5; i < 7; i++){
        
    }

}

int main(void){
    //get data from file into vectors
    std::vector<Player> players = fillPlayers(std::ifstream("Data.txt"));  

    //give stats way to call back to player

    //get avg, median, and extrema from each vector
    
    //calculate gun usage disparity

    //look for correlation between delta damage and winrate
}