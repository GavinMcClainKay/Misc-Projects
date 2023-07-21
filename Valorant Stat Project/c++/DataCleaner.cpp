#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>

int RemoveDuplicates(std::ifstream& input_file) {
    std::map<std::string, bool> all_strings;


    std::cout << "\tGun1\t\t" << "Gun2\t\t" << "Gun3\t   " << "Damage/Round\t\t" << "K/D\t\t" << "HS%\t\t" << "WIN%\t\t" << "Wins\t\t" << "KAST%\t  " << "AVG DMG Dealt\t\t" << "Kills\t\t" << "Deaths\t\t" << "Assists\t\t" << "ACS\t\t" << "KAD\t   " << "Kills/Round\t   " << "First Bloods\t   " << "Flawless Rounds    " << "Aces" << std::endl; 
    std::string current_line;
    int num_lines_removed = 0;
    bool current_line_exists = false;
    while(!input_file.eof()) {
        std::getline(input_file, current_line);
        current_line_exists = all_strings[current_line];
        if(current_line_exists) {
            //do nothing
            num_lines_removed++;
            continue;
        }else {
            //add current_line to new file
            all_strings[current_line] = true;
            if(current_line[0] <= '9' && current_line[0] >= 48) {
                std::cout << ":\t";
                for(char c : current_line){
                    if(c == ' ') std::cout << '\t';
                    else std::cout << c;
                }
                std::cout << std::endl;

            }
        }
    }

    return num_lines_removed;
}

int main(void) {
    std::ifstream playerDataFileStream;
    playerDataFileStream.open("C:/Users/Gavin/Desktop/Valorant Stat Project/JavaScript/PlayerData.txt", std::ifstream::in);
    if(playerDataFileStream.is_open()) RemoveDuplicates(playerDataFileStream);
    else std::cout << "Error: Could not open PlayerData.txt" << std::endl;
    playerDataFileStream.close();
    return 0;
}